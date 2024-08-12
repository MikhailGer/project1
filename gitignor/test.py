# SUCCESS
import sys
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QObject
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QTextEdit, QLabel
from PyQt5.QtSerialPort import QSerialPort


class QSerialPortWorker(QObject):
    dataReceived = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.serialPort = QSerialPort()

    @pyqtSlot(str)
    def openPort(self, portName):
        self.serialPort.setPortName(portName)
        self.serialPort.setBaudRate(115200)
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


class SerialThread(QThread):
    openPort = pyqtSignal(str)
    writeData = pyqtSignal(bytes)
    dataReceived = pyqtSignal(bytes)

    def __init__(self):
        super().__init__()
        self.worker = QSerialPortWorker()

    def run(self):
        self.openPort.connect(self.worker.openPort)
        self.writeData.connect(self.worker.writeData)
        self.worker.dataReceived.connect(self.dataReceived)
        self.exec_()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.serialThread = SerialThread()
        self.serialThread.start()
        self.serialThread.dataReceived.connect(self.handleDataReceived)

    def initUI(self):
        layout = QVBoxLayout()

        self.statusLabel = QLabel("Not Connected")
        layout.addWidget(self.statusLabel)

        self.textEdit = QTextEdit()
        layout.addWidget(self.textEdit)

        self.connectButton = QPushButton("Connect")
        self.connectButton.clicked.connect(self.connectToDevice)
        layout.addWidget(self.connectButton)

        self.sendConnectCommandButton = QPushButton("Send Connect Command")
        self.sendConnectCommandButton.clicked.connect(self.sendConnectCommand)
        layout.addWidget(self.sendConnectCommandButton)

        self.setLayout(layout)
        self.setWindowTitle("Serial Port Connection")

    def connectToDevice(self):
        portName = "/dev/ttyUSB0"  # Измените на ваше имя порта
        print(f"Attempting to open port: {portName}")
        self.serialThread.openPort.emit(portName)

    def sendConnectCommand(self):
        command = b"connect\n"
        print(f"Sending command: {command}")
        self.serialThread.writeData.emit(command)

    def handleDataReceived(self, data):
        response = data.data().decode('utf-8')
        print(f"Handling received data: {response}")
        self.textEdit.append(response)

        if "connected" in response:
            self.statusLabel.setText("Successful Connection")
            print("Successful Connection")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
#################################################################################################
# import sys
# import time
#
# from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QObject
# from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QTextEdit, QLabel
# from PyQt5.QtSerialPort import QSerialPort
#
#
# class QSerialPortWorker(QObject):
#     dataReceived = pyqtSignal(object)
#
#     def __init__(self):
#         super().__init__()
#         self.serialPort = QSerialPort()
#
#     @pyqtSlot(str)
#     def openPort(self, portName):
#         self.serialPort.setPortName(portName)
#         self.serialPort.setBaudRate(115200)
#         if self.serialPort.open(QSerialPort.ReadWrite):
#             print(f"Port {portName} opened successfully")
#             self.serialPort.readyRead.connect(self.readData)
#         else:
#             print(f"Failed to open port {portName}")
#
#     @pyqtSlot(bytes)
#     def writeData(self, data):
#         if self.serialPort.isOpen():
#             print(f"Writing data: {data}")
#             self.serialPort.write(data)
#         else:
#             print("Port is not open")
#
#     @pyqtSlot()
#     def readData(self):
#         if self.serialPort.isOpen():
#             data = self.serialPort.readAll()
#             print(f"Data received: {data}")
#             self.dataReceived.emit(data)
#
#     @pyqtSlot()
#     def closePort(self):
#         if self.serialPort.isOpen():
#             self.serialPort.close()
#             print("Port closed")
#
#
# class SerialThread(QThread):
#     openPort = pyqtSignal(str)
#     writeData = pyqtSignal(bytes)
#     dataReceived = pyqtSignal(bytes)
#     closePort = pyqtSignal()
#
#     def __init__(self):
#         super().__init__()
#         self.worker = QSerialPortWorker()
#
#     def run(self):
#         self.openPort.connect(self.worker.openPort)
#         self.writeData.connect(self.worker.writeData)
#         self.worker.dataReceived.connect(self.dataReceived)
#         self.closePort.connect(self.worker.closePort)
#         self.exec_()
#
#     def stop(self): #завершение потока в случае отключения ардуино
#         self.quit()
#         self.wait()
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#         self.serialThread = SerialThread()
#         self.serialThread.start()
#         self.serialThread.dataReceived.connect(self.handleDataReceived)
#
#     def initUI(self):
#         layout = QVBoxLayout()
#
#         self.statusLabel = QLabel("Not Connected")
#         layout.addWidget(self.statusLabel)
#
#         self.textEdit = QTextEdit()
#         layout.addWidget(self.textEdit)
#
#         self.connectButton = QPushButton("Connect")
#         self.connectButton.clicked.connect(self.connectToDevice)
#         layout.addWidget(self.connectButton)
#
#         self.setLayout(layout)
#         self.setWindowTitle("Serial Port Connection")
#
#     def connectToDevice(self):
#         portName = "/dev/ttyUSB0"  # Измените на ваше имя порта
#         print(f"Attempting to open port: {portName}")
#         self.serialThread.openPort.emit(portName)
#         time.sleep(3) #время на запуск платы
#         self.serialThread.writeData.emit(b"connect\n")
#
#     def handleDataReceived(self, data):
#         response = data.data().decode('utf-8')
#         print(f"Handling received data: {response}")
#         self.textEdit.append(response)
#
#         if "connected" in response:
#             self.statusLabel.setText("Successful Connection")
#             print("Successful Connection")
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#
#     mainWindow = MainWindow()
#     mainWindow.show()
#
#     sys.exit(app.exec_())
