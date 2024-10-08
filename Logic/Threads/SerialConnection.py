import time
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QObject
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import threading

from config import DB_DATA

class PortChecker(QThread):
    port_list_signal = pyqtSignal(object)
    finished = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.portlist = None
        self.running = True
        self.paused = False
        self.condition = threading.Condition()

    # def run(self):
    #     self.running = True
    #     while self.running:
    #         ports = QSerialPortInfo().availablePorts()
    #         self.portlist = [port.portName() for port in ports]
    #         self.port_list_signal.emit(self.portlist)
    #         time.sleep(1) #обновление портов раз в какое-то время

    def run(self):
        while self.running:
            with self.condition:
                if self.paused:
                    self.condition.wait()  # Ожидание, пока поток не будет возобновлен

            ports = QSerialPortInfo().availablePorts()
            self.portlist = [port.portName() for port in ports]
            self.port_list_signal.emit(self.portlist)
            time.sleep(1)

        self.finished.emit()
    def pause(self):
        with self.condition:
            self.paused = True

    def resume(self):
        with self.condition:
            self.paused = False
            self.condition.notify()  # Пробуждение потока

    def stop(self):
        self.running = False
        self.wait()

class ArduinoChecker(QThread):
    device_disconnected_signal = pyqtSignal()

    def __init__(self, port_name):
        super().__init__()
        self.port_name = port_name
        self.running = True

    def run(self):
        # Хранение имени порта в начале #Укажите ваш порт

        while self.running:
            available_ports = QSerialPortInfo.availablePorts()
            ports = [port.portName() for port in available_ports]

            if self.port_name not in ports:
                self.device_disconnected_signal.emit()
                break

            time.sleep(1)  # Пауза перед следующей проверкой

    def stop(self):
        self.running = False
        self.wait()


class QSerialPortWorker(QObject):
    dataReceived = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.serialPort = QSerialPort()

    @pyqtSlot(str)
    def openPort(self, portName):
        self.serialPort.setPortName(portName)
        self.serialPort.setBaudRate(int(DB_DATA.SerialBaudRate))
        if self.serialPort.open(QSerialPort.ReadWrite):
            print(f"Port {portName} opened successfully")
            self.serialPort.readyRead.connect(self.readData)
        else:
            print(f"Failed to open port {portName}")

    @pyqtSlot(bytes)
    def writeData(self, data):
        if self.serialPort.isOpen():
            print(f"Writing data: {data}")
            self.serialPort.write(data)
        else:
            print("Port is not open")

    @pyqtSlot()
    def readData(self):
        if self.serialPort.isOpen():
            data = self.serialPort.readAll()
            print(f"Data received: {data}")
            self.dataReceived.emit(data)

    @pyqtSlot()
    def closePort(self):
        if self.serialPort.isOpen():
            self.serialPort.close()
            print("Port closed")

    def isOpen(self):
        return self.serialPort.isOpen()


class SerialThread(QThread):
    openPort = pyqtSignal(str)
    writeData = pyqtSignal(bytes)
    dataReceived = pyqtSignal(bytes)
    closePort = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.worker = QSerialPortWorker()

    def run(self):
        self.openPort.connect(self.worker.openPort)
        self.writeData.connect(self.worker.writeData)
        self.worker.dataReceived.connect(self.dataReceived)
        self.closePort.connect(self.worker.closePort)
        self.exec_()

    def is_port_open(self):
        return self.worker.isOpen()

    def stop(self):  #завершение потока в случае отключения ардуино
        self.quit()
        self.wait()


