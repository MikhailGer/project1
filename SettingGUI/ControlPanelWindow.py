import sys
import time
from traceback import print_tb

from config import DB_DATA

from SettingGUI.main_window import Ui_mainWindow

from Logic.Threads.Disc_Thread import DiscThread
from Logic.Threads.DiscScan_Thread import DiscScanThread
from Logic.Threads.SerialConnection import ArduinoChecker, SerialThread, PortChecker

from SettingGUI.create_sample_dialog_window import Create_Sample_Dialog
from SettingGUI.device_settings_dialog import Create_Settings_Dialog

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtSerialPort import QSerialPortInfo
from PyQt5.QtCore import QObject, pyqtSignal

from Logic.developer_mode import DevMode

class Signals(QObject):
    custom_signal = pyqtSignal(int)

class App(QMainWindow, Ui_mainWindow):
    connectionStatus = pyqtSignal(bool)
    def __init__(self):
        super().__init__()
        self.mode = None
        self.setupUi(self)
        # далее создается отдельный поток для связи с ардуино
        self.serial = SerialThread()
        self.serial.start()

        #запуск сканирования портов, выполняется раз в секунду(можно изменить в SerialConnection.py)
        self.portChecker = PortChecker()
        self.portChecker.port_list_signal.connect(self.auto_connect)
        self.connectionStatus.connect(self.on_connection_established)
        self.portChecker.start()

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
            0: 'name',
            1: 'id'
        }
        # self.comboBox_ports.currentIndexChanged.connect(self.ports_combobox_handler)
        self.comboBox_ID_name.currentIndexChanged.connect(self.update_disc_list)
        self.CreateDisc.clicked.connect(self.show_create_dialog_disc_param)
        self.pushButton_device_settings.clicked.connect(self.show_settings_dialog)
        self.DeleteDisc.clicked.connect(self.deleteDisc)
        self.loop_start.triggered.connect(self.mode_selection)
        self.comboBox_mods.currentIndexChanged.connect(self.enable_loop)
        self.comboBox_disc_selector.currentTextChanged.connect(self.enable_loop)

        # self.update_ports()
        # self.auto_connect()


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
        else:
            self.DeleteDisc.setEnabled(False)
            self.Results.setEnabled(False)

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

    #возможность выбора порта убрана
    # def update_ports(self):  # обновление портов
    #     try:
    #         self.comboBox_ports.blockSignals(True)
    #         self.comboBox_ports.clear()
    #         self.comboBox_ports.addItem('')
    #         ports = QSerialPortInfo().availablePorts()
    #         self.portlist = [port.portName() for port in ports]
    #         self.comboBox_ports.addItems(self.portlist)connectionFlag
    #         self.comboBox_ports.addItem("update")
    #         self.comboBox_ports.blockSignals(False)
    #     except Exception as e:
    #         print(f"Error in update_ports: {e}")

    def auto_connect(self, response):
        if DB_DATA.operating_port in response:
            if not self.serial.is_port_open():
                self.serial.openPort.emit(DB_DATA.operating_port)

            if self.serial.is_port_open():
                self.arduino_handshacke()
                #если порт после handshake не открыт, начать опять поиск портов(в методе handshake останавливается сканирование портов):

                # if not self.connectionFlag:
                #     try:
                #         self.portChecker.resume()
                #     except Exception:
                #         pass


            else:
                self.serial.closePort.emit()
                self.comboBox_mods.setEnabled(False)
                self.signal.custom_signal.emit(0)
        else:
            print("empty port list")
            self.serial.closePort.emit()
            self.comboBox_mods.setEnabled(False)
            self.signal.custom_signal.emit(0)


    # возможность выбора порта убрана
    # def ports_combobox_handler(self):
    #     try:
    #         self.comboBox_ports.currentIndexChanged.disconnect(self.ports_combobox_handler)
    #     except Exception:
    #         pass
    #     self.loop_start.setEnabled(False)
    #     self.comboBox_mods.setCurrentIndex(0)
    #
    #     if self.comboBox_ports.currentText() == "update":
    #         self.update_ports()
    #         self.auto_connect()
    #         # self.ports_combobox_handler()
    #
    #     elif self.comboBox_ports.currentText() == "":
    #         self.comboBox_mods.setEnabled(False)
    #         self.signal.custom_signal.emit(0)
    #
    #     else:
    #         if self.serial.is_port_open():
    #             self.serial.closePort.emit()
    #         self.serial.openPort.emit(self.comboBox_ports.currentText())
    #         print("ports_combobox_handler ELSE HANDLED")
    #
    #         if self.serial.is_port_open():
    #             self.arduino_handshacke()
    #
    #         else:
    #             self.serial.closePort.emit()
    #             self.comboBox_mods.setEnabled(False)
    #             self.signal.custom_signal.emit(0)
    #     try:
    #         self.comboBox_ports.currentIndexChanged.connect(self.ports_combobox_handler)
    #     except Exception:
    #         pass

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
        self.mode = DevMode(self)
        self.mode.start_mode()
        self.loop_stop.triggered.connect(self.stop_cycle)
        self.comboBox_ports.setEnabled(False)
        self.comboBox_mods.setEnabled(False)
        self.signal.custom_signal.emit(4)

    def stop_cycle(self):
        self.mode.stop_mode()
        self.mode = None
        self.loop_stop.triggered.disconnect(self.stop_cycle)
        self.comboBox_ports.setEnabled(True)
        self.comboBox_mods.setEnabled(True)
        self.start_window_mode()

    def arduino_disconected(self):
        if self.loop_stop.isEnabled():  #если было запущено сканирование кнопка стоп активна
            self.loop_stop.trigger()  #прирывание сканирования
        if self.mode != None:
            self.mode.stop_mode()
        self.start_window_mode()
        self.check_arduino.device_disconnected_signal.disconnect(self.arduino_disconected)
        # self.comboBox_ports.currentIndexChanged.disconnect(self.arduino_disconected)
        # self.comboBox_ports.currentIndexChanged.connect(self.ports_combobox_handler)
        self.check_arduino.start()
        self.serial.closePort.emit()
        self.connectionStatus.emit(False)
        self.label_0.setText("Подключите устройство и выберите режим работы установки")

        #методов больше не существует
        # self.update_ports()
        # self.ports_combobox_handler()

    def arduino_handshacke(self):
        print('handshacke called')
       #метода ports_combobox_handler больше нет, т.к. была убрана возможность выбирать порт, коннект происходит автоматически
        # try:
        #     self.comboBox_ports.currentIndexChanged.disconnect(self.ports_combobox_handler)
        # except Exception:
        #     pass
        self.label_0.setText("Устройство подключается, пожалуйста, подождите...")

        try:
            self.connectionStatus.emit(True)
        except Exception:
            pass
        time.sleep(3)  # время на запуск платы, намеренно добавленно в основном потоке, чтобы было возможно
        # дальнейшее взаимодействие с платой СРАЗУ(плата загружается около 2.5 секунд и в это время она мертва)
        try:
            self.serial.dataReceived.disconnect(self.handleDataReceived)
        except Exception:
            pass
        self.serial.dataReceived.connect(self.handle_handshake_receive)
        self.serial.writeData.emit(b"connect\n")

    def handle_handshake_receive(self, receive):
        try:
            response = receive.data().decode('utf-8')
        except Exception:
            print("Incorrect arduino callback")
            response = ""
        if "connected" in response:
            try:
                self.serial.dataReceived.disconnect(self.handle_handshake_receive)
            except Exception:
                pass
            # self.serial.dataReceived.connect(self.handleDataReceived)
            print("Arduino ready to work")
            self.check_arduino = ArduinoChecker(DB_DATA.operating_port)
            self.check_arduino.device_disconnected_signal.connect(self.arduino_disconected)

            # метода ports_combobox_handler больше нет, т.к. была убрана возможность выбирать порт, коннект происходит автоматически
            # try:
            #     self.comboBox_ports.currentIndexChanged.disconnect(self.ports_combobox_handler)
            # except Exception:
            #     pass
            # self.comboBox_ports.currentIndexChanged.disconnect(self.ports_combobox_handler)
            # self.comboBox_ports.currentIndexChanged.connect(self.arduino_disconected)
            self.check_arduino.start()
            self.start_window_mode()

        else:

            # try:
            #     self.comboBox_ports.currentIndexChanged.connect(self.ports_combobox_handler)
            # except Exception:
            #     pass
            print("Arduino isn't ready to work")
            self.serial.closePort.emit()
            self.comboBox_mods.setEnabled(False)
            self.signal.custom_signal.emit(0)
            self.connectionStatus.emit(False)
        try:
            self.serial.dataReceived.disconnect(self.handle_handshake_receive)
        except Exception:
            pass

    def on_connection_established(self, status):
        if not status:
            print("callsed resume")
            self.portChecker.resume()
        else:
            print("callsed pause")

            self.portChecker.pause()

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
