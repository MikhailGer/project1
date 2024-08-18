import sys
import time

from main_window import Ui_mainWindow

from Threads.Disc_Thread import DiscThread
from Threads.DiscScan_Thread import DiscScanThread
from Threads.SerialConnection import ArduinoChecker, SerialThread

from create_sample_dialog_window import Create_Sample_Dialog
from device_settings_dialog import Create_Settings_Dialog
from config import Device_Configuration

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort
from PyQt5.QtCore import QObject, pyqtSignal


class Signals(QObject):
    custom_signal = pyqtSignal(int)


class App(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # далее создается отдельный поток для связи с ардуино
        self.serial = SerialThread()
        self.serial.start()
        # self.serial.dataReceived.connect(self.handleDataReceived)

        self.init_signals()
        self.init_ui()
        self.currentDisc = str
    def init_signals(self):
        self.signal = Signals()
        self.signal.custom_signal.connect(self.stackedWidget.setCurrentIndex)

    def init_ui(self):

        self.mode_actions = {
            1: self.full_disc_mode,
            2: self.half_disc_mode,
            3: self.training_mode,
            4: self.developer_mode
        }
        self.display_disc_mode = {
            0: 'id',
            1: 'name'
        }
        self.comboBox_ports.currentIndexChanged.connect(self.operating_port_chosen)
        self.comboBox_ID_name.currentIndexChanged.connect(self.update_disc_list)
        self.CreateDisc.clicked.connect(self.show_create_dialog_disc_param)
        self.pushButton_device_settings.clicked.connect(self.show_settings_dialog)
        self.DeleteDisc.clicked.connect(self.deleteDisc)
        self.loop_start.triggered.connect(self.mode_selection)
        self.comboBox_mods.currentIndexChanged.connect(self.enable_loop)
        self.comboBox_disc_selector.currentTextChanged.connect(self.enable_loop)

        self.update_ports()
        self.operating_port_chosen()

    def show_settings_dialog(self):
        settings_dialog = Create_Settings_Dialog()
        result = settings_dialog.exec_()

    def show_create_dialog_disc_param(self):
        create_dialog = Create_Sample_Dialog()
        result = create_dialog.exec_()
        if result == QDialog.Accepted:
            self.update_disc_list()
        else:
            print("Rejected")

    def update_disc_list(self):
        mode = self.display_disc_mode.get(self.comboBox_ID_name.currentIndex())
        self.DowloadDiscListThread = DiscThread('DowloadDiscList', mode)
        self.DowloadDiscListThread.update_signal.connect(self.addList)
        self.DowloadDiscListThread.start()

    def addList(self, result):
        self.comboBox_disc_selector.clear()
        self.comboBox_disc_selector.addItems(map(str, result))
        if self.comboBox_disc_selector.currentText():
            self.DeleteDisc.setEnabled(True)
            self.Results.setEnabled(True)
            # self.loop_start.setEnabled(True)
        else:
            self.DeleteDisc.setEnabled(False)
            self.Results.setEnabled(False)
            # self.loop_start.setEnabled(False)

    def deleteDisc(self):
        id_or_data = self.comboBox_disc_selector.currentText()
        mode = self.display_disc_mode.get(self.comboBox_ID_name.currentIndex())
        self.DeleteDiscThread = DiscThread('DeleteDisc', id_or_data, mode)
        self.DeleteDiscThread.update_signal.connect(self.delete_status)
        self.DeleteDiscThread.start()

    def delete_status(self, result):
        if result:
            self.update_disc_list()
        else:
            print("deleting error, try again")

    def update_ports(self):  # обновление портов
        try:
            self.comboBox_ports.blockSignals(True)
            self.comboBox_ports.clear()
            self.comboBox_ports.addItem('')
            ports = QSerialPortInfo().availablePorts()
            portlist = [port.portName() for port in ports]
            self.comboBox_ports.addItems(portlist)
            self.comboBox_ports.addItem("update")
            self.comboBox_ports.blockSignals(False)
        except Exception as e:
            print(f"Error in update_ports: {e}")

    def operating_port_chosen(self):
        self.loop_start.setEnabled(False)
        self.comboBox_mods.setCurrentIndex(0)

        if self.comboBox_ports.currentText() == "update":
            self.update_ports()
            self.operating_port_chosen()

        elif self.comboBox_ports.currentText() == "":
            self.comboBox_mods.setEnabled(False)
            self.signal.custom_signal.emit(0)

        else:
            if self.serial.is_port_open():
                self.serial.closePort.emit()
            self.serial.openPort.emit(self.comboBox_ports.currentText())
            if self.serial.is_port_open():
                self.arduino_handshacke()
                # self.check_arduino = ArduinoChecker(self.comboBox_ports.currentText())
                # self.check_arduino.device_disconnected_signal.connect(self.arduino_disconected)
                # self.comboBox_ports.currentIndexChanged.disconnect(self.operating_port_chosen)
                # self.comboBox_ports.currentIndexChanged.connect(self.arduino_disconected)
                # self.check_arduino.start()
                # self.start_window_mode()
                # else:
                #     self.serial.closePort.emit()
                #     self.comboBox_mods.setEnabled(False)
                #     self.signal.custom_signal.emit(0)
            else:
                self.serial.closePort.emit()
                self.comboBox_mods.setEnabled(False)
                self.signal.custom_signal.emit(0)

    def signal_handle(self, signal):
        print(f"Connection status: {signal}")

    def mode_selection(self):
        self.currentDisc = self.comboBox_disc_selector.currentText()
        action = self.mode_actions.get(self.comboBox_mods.currentIndex())
        if action:
            action()
        else:
            self.loop_stop.trigger()

    def enable_loop(self):
        if self.comboBox_mods.currentIndex() != 0 and self.comboBox_disc_selector.currentText() != '':
            self.loop_start.setEnabled(True)
        else:
            self.loop_start.setEnabled(False)

    def start_window_mode(self):
        # print('mode 0')
        # if self.comboBox_disc_selector.currentText():
        #     self.loop_start.setEnabled(True)
        # else:
        #     self.loop_start.setEnabled(False)

        self.comboBox_mods.setEnabled(True)
        self.update_disc_list()
        self.signal.custom_signal.emit(1)

    def full_disc_mode(self):  # режим полного диска
        print('mode 1')
        self.loop_stop.triggered.connect(self.stop_cycle)
        self.comboBox_ports.setEnabled(False)
        self.comboBox_mods.setEnabled(False)
        self.signal.custom_signal.emit(2)
        is_current = True
        self.DiscScaningThread = DiscScanThread('getCurrentScanID')
        self.DiscScaningThread.update_signal.connect(self.showCurrentScan)
        self.DiscScaningThread.start()

    def showCurrentScan(self, answer):
        current_scan = str(answer)
        self.lineEdit_sampleID_scaning.setText(current_scan)

    def half_disc_mode(self):  # режим часть диска
        print('mode 2')
        self.signal.custom_signal.emit(2)

    def training_mode(self):  # режим обучения
        print('mode 3')
        self.signal.custom_signal.emit(3)

    def developer_mode(self):  # режим отладки
        print("mode 4")
        self.loop_stop.triggered.connect(self.stop_cycle)
        self.comboBox_ports.setEnabled(False)
        self.comboBox_mods.setEnabled(False)
        self.signal.custom_signal.emit(4)

    def stop_cycle(self):
        # self.currentScan =
        self.loop_stop.triggered.disconnect(self.stop_cycle)
        self.comboBox_ports.setEnabled(True)
        self.comboBox_mods.setEnabled(True)
        self.start_window_mode()

    def arduino_disconected(self):
        if self.loop_stop.isEnabled():  #если было запущено сканирование кнопка стоп активна
            self.loop_stop.trigger()  #прирывание сканирования
        self.check_arduino.device_disconnected_signal.disconnect(self.arduino_disconected)
        self.comboBox_ports.currentIndexChanged.disconnect(self.arduino_disconected)
        self.comboBox_ports.currentIndexChanged.connect(self.operating_port_chosen)
        self.check_arduino.stop()
        self.serial.closePort.emit()
        self.update_ports()
        self.operating_port_chosen()

    def arduino_handshacke(self):
        print('called')
        time.sleep(3)  # время на запуск платы, намеренно добавленно в основном потоке, чтобы было возможно
        # дальнейшее взаимодействие с платой СРАЗУ(плата загружается около 2.5 секунд и в это время она мертва)
        try:
            self.serial.dataReceived.disconnect(self.handleDataReceived)
        except Exception:
            pass
        self.serial.dataReceived.connect(self.handle_handshake_receive)
        self.serial.writeData.emit(b"connect\n")

    def handle_handshake_receive(self, receive):
        response = receive.data().decode('utf-8')
        if "connected" in response:
            try:
                self.serial.dataReceived.disconnect(self.handle_handshake_receive)
            except Exception:
                pass
            # self.serial.dataReceived.connect(self.handleDataReceived)
            print("Arduino ready to work")
            self.check_arduino = ArduinoChecker(self.comboBox_ports.currentText())
            self.check_arduino.device_disconnected_signal.connect(self.arduino_disconected)
            self.comboBox_ports.currentIndexChanged.disconnect(self.operating_port_chosen)
            self.comboBox_ports.currentIndexChanged.connect(self.arduino_disconected)
            self.check_arduino.start()
            self.start_window_mode()
        else:
            try:
                self.serial.dataReceived.disconnect(self.handle_handshake_receive)
            except Exception:
                pass
            # self.serial.dataReceived.connect(self.handleDataReceived)
            print("Arduino isn't ready to work")
            self.serial.closePort.emit()
            self.comboBox_mods.setEnabled(False)
            self.signal.custom_signal.emit(0)

    def handleDataReceived(self, data):
        response = data.data().decode('utf-8')
        print(f"Handling received data: {response}")


def main():
    app = QApplication(sys.argv)
    mainWindow = App()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
