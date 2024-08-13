#реализация подтягивания файла конфига из бд
from Threads.SerialConnection import SerialThread
from config import Default_Device_Configuration
from PyQt5.QtWidgets import QListView
from PyQt5.QtCore import QStringListModel

class DevMode:
    def __init__(self, serial:SerialThread):
        self.serial = serial

        self.tenzo_update_rate = Default_Device_Configuration.tenzo_update_rate_default

    def move_base(self, steps, speed, acceleration, max_speed):
        self.serial.writeData.emit(f"1,{str(speed)},{str(acceleration)},{str(max_speed)},{str(steps)}")

    def move_head(self, steps, speed, acceleration, max_speed):
        self.serial.writeData.emit(f"2,{str(speed)},{str(acceleration)},{str(max_speed)},{str(steps)}")

    def tenzo_on(self):
        self.serial.writeData.emit(f"0,1,{str(self.tenzo_update_rate)}")

    def tenzo_off(self):
        self.serial.writeData.emit(f"0,0")

    def tenzo_tare(self): #тарироание датчика, в dev mode скорее всего использоваться не будет
        self.serial.writeData.emit(f"0,2")
    #     что нам нужно: 1.получить конфиг, если нет - использовать дефолт; 2.Собрать данные из лайн эдитов. 3. кинуть на плату. 4. Получить данные с тензодатчикаб вывести их

