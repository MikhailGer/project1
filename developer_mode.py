from Threads.SerialConnection import TenzoReader

from config import Default_Device_Configuration

from PyQt5.QtCore import QStringListModel

from SettingGUI.ControlPanelWindow import App
from ArduinoCommands import ArduinoCommands


class DevMode:
    def __init__(self, main_window: App):
        self.send_command = ArduinoCommands(main_window)
        self.main_window = main_window
        self.main_window.pushButton_base_motor.connect(self.move_base)
        self.main_window.pushButton_stand_motor.connect(self.move_head)

        self.model = QStringListModel()
        self.model.setStringList([])
        self.main_window.listView_tenzo.setModel(self.model)

        self.tenzo_reader_thread = TenzoReader(self.main_window.serial)
        self.tenzo_reader_thread.dataReceived.connect(self.handle_data)
        self.data_list = []

        self.base_motor_steps = 0
        self.base_motor_speed = 0
        self.base_motor_acceleration = 0
        self.base_MaxSpeed = 0

        self.stand_motor_steps = 0
        self.stand_motor_speed = 0
        self.stand_motor_acceleration = 0
        self.stand_MaxSpeed = 0
        
    def start_mode(self):
        self.send_command.tenzo_on()
        self.send_command.set_tenzo_updaterate(Default_Device_Configuration.tenzo_update_rate_default)
        self.send_command.steppers_on()

    def handle_data(self, data):
        if len(self.data_list) >= 100:
            self.data_list.pop(0)
        self.data_list.append(data)
        self.model.setStringList(self.data_list)

    def move_base(self):
        
        if self.is_float(self.main_window.lineEdit_base_motor_steps.text().strip()):
            self.base_motor_steps = self.main_window.lineEdit_base_motor_steps.text().strip()
        
        if self.is_float(self.main_window.lineEdit_base_motor_speed.text().strip()):
            self.base_motor_speed = self.main_window.lineEdit_base_motor_speed.text().strip()
            
        if self.is_float(self.main_window.lineEdit_base_acceleration.text().strip()):
            self.base_motor_acceleration = self.main_window.lineEdit_base_acceleration.text().strip()
            
        if self.is_float(self.main_window.lineEdit_base_MaxSpeed.text().strip()):
            self.base_MaxSpeed = self.main_window.lineEdit_base_MaxSpeed.text().strip()
        
        self.send_command.move_base(self.base_motor_steps, self.base_motor_speed, self.base_motor_acceleration, self.base_MaxSpeed)
            
    def move_head(self):
        if self.is_float(self.main_window.lineEdit_stand_motor_steps.text().strip()):
            self.stand_motor_steps = self.main_window.lineEdit_stand_motor_steps.text().strip()

        if self.is_float(self.main_window.lineEdit_stand_motor_speed.text().strip()):
            self.stand_motor_speed = self.main_window.lineEdit_stand_motor_speed.text().strip()

        if self.is_float(self.main_window.lineEdit_head_acceleration.text().strip()):
            self.stand_motor_acceleration = self.main_window.lineEdit_head_acceleration.text().strip()

        if self.is_float(self.main_window.lineEdit_head_MaxSpeed.text().strip()):
            self.stand_MaxSpeed = self.main_window.lineEdit_head_MaxSpeed.text().strip()

        self.send_command.move_head(self.stand_motor_steps, self.stand_motor_speed, self.stand_motor_acceleration,
                                    self.stand_MaxSpeed)

    def stop_mode(self):
        try:
            self.main_window.pushButton_base_motor.disconnect(self.move_base)
        except Exception:
            pass

        try:
            self.main_window.pushButton_stand_motor.disconnect(self.move_head)
        except Exception:
            pass
        self.send_command.tenzo_off()
        self.send_command.steppers_off()
        self.send_command.return_head()
        self.send_command.return_base()

        self.model.setStringList([])
        self.data_list.clear()

        self.tenzo_reader_thread.stop()

    def is_float(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False