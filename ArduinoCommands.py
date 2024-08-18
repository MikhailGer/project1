from SettingGUI.ControlPanelWindow import App

class ArduinoCommands:
    def __init__(self, main_window: App):  # принимает подключение к ардуино из главного окна
        self.serial = main_window.serial

    def tenzo_off(self):
        self.serial.writeData.emit(f"1")

    def tenzo_on(self):
        self.serial.writeData.emit(f"2")

    def set_tenzo_updaterate(self, tenzo):
        self.serial.writeData.emit(f"3,{str(tenzo)}")

    def tenzo_tare(self):  # тарироание датчика, в dev mode скорее всего использоваться не будет
        self.serial.writeData.emit(f"4")

    def move_base(self, steps, speed, acceleration, max_speed):
        self.serial.writeData.emit(f"5,{str(speed)},{str(acceleration)},{str(max_speed)},{str(steps)}")

    def move_head(self, steps, speed, acceleration, max_speed):
        self.serial.writeData.emit(f"6,{str(speed)},{str(acceleration)},{str(max_speed)},{str(steps)}")

    def pressure(self, base_max_speed, base_acceleration, returning_speed, returning_acceleration, pressure):
        self.serial.writeData.emit(f"7,{str(base_max_speed)},{str(base_acceleration)},{str(returning_speed)},{str(returning_acceleration)},{str(pressure)}")

    def steppers_on(self):
        self.serial.writeData.emit(f"8")

    def steppers_off(self):
        self.serial.writeData.emit(f"9")

    def return_head(self):
        self.serial.writeData.emit(f"10")

    def set_head_working_pos(self, steps):
        self.serial.writeData.emit(f"11,{str(steps)}")

    def return_base(self):
        self.serial.writeData.emit(f"12")
