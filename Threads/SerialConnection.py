import time
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QObject
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

from config import SerialBaudRate


class ArduinoChecker(QThread):
    device_disconnected_signal = pyqtSignal()

    def __init__(self, port_name):
        super().__init__()
        self.port_name = port_name
        self.running = True

    def run(self):
        # Хранение имени порта в начале # Укажите ваш порт

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
        self.serialPort.setBaudRate(SerialBaudRate)
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

    def stop(self): #завершение потока в случае отключения ардуино
        self.quit()
        self.wait()


class TenzoReader(QThread):
    dataReceived = pyqtSignal(object)
    def __init__(self, serial:SerialThread):
        super().__init__()
        self.serial = serial
    def run(self):
        while self.serial.worker.serialPort.canReadLine():
            line = self.serial.worker.serialPort.readLine().decode('utf-8').strip()
            self.dataReceived.emit(line)
    def stop(self): #завершение потока в случае отключения ардуино
        self.quit()
        self.wait()