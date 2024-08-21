# from SettingGUI.ControlPanelWindow import App

class ArduinoCommands:
    # def __init__(self, main_window:App):
    def __init__(self, main_window):  # принимает подключение к ардуино из главного окна
        self.serial = main_window.serial

    def tenzo_off(self):
        self.serial.writeData.emit(f"1;".encode())

    def tenzo_on(self):
        self.serial.writeData.emit(f"2;".encode())

    def set_tenzo_updaterate(self, tenzo):
        self.serial.writeData.emit(f"3,{str(tenzo)};".encode())

    def tenzo_tare(self):  # тарироание датчика, в dev mode скорее всего использоваться не будет
        self.serial.writeData.emit(f"4;".encode())

    def move_base(self, steps, speed, acceleration, max_speed):
        self.serial.writeData.emit(f"5,{str(speed)},{str(acceleration)},{str(max_speed)},{str(steps)};".encode())

    def move_head(self, steps, speed, acceleration, max_speed):
        self.serial.writeData.emit(f"6,{str(speed)},{str(acceleration)},{str(max_speed)},{str(steps)};".encode())

    def pressure(self, base_max_speed, base_acceleration, returning_speed, returning_acceleration, pressure):
        self.serial.writeData.emit(f"7,{str(base_max_speed)},{str(base_acceleration)},{str(returning_speed)},{str(returning_acceleration)},{str(pressure)};".encode())

    def steppers_on(self):
        self.serial.writeData.emit(f"8;".encode())

    def steppers_off(self):
        self.serial.writeData.emit(f"9;".encode())

    def return_head(self):
        self.serial.writeData.emit(f"10;".encode())

    def set_head_working_pos(self, steps):
        self.serial.writeData.emit(f"11,{str(steps)};".encode())

    def return_base(self):
        self.serial.writeData.emit("12;".encode())
