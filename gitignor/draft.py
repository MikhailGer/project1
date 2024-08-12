#реализация подтягивания файла конфига из бд
from Threads.device_configThread import DeviceConfigThread
from Threads.SerialConnection import SerialThread
from config import Default_Device_Configuration

class DevMode:
    def __init__(self, serial:SerialThread):
        self.serial = serial

        self.current_config_thread = DeviceConfigThread('find_current_config')
        self.current_config_thread .update_signal.connect(self.get_current_config)
        self.current_config_thread.start()

        self.tenzo_update_rate = None
        self.base_diameter = None
        self.motor_speed_base = None
        self.motor_accel_base = None
        self.motor_maxspeed_base = None
        self.motor_speed_head = None
        self.motor_accel_head = None
        self.motor_maxspeed_head = None
        self.motor_returning_speed_head = None
        self.motor_returning_accel_head = None
    #     что нам нужно: 1.получить конфиг, если нет - использовать дефолт; 2.Собрать данные из лайн эдитов. 3. кинуть на плату. 4. Получить данные с тензодатчикаб вывести их


    def get_current_config(self, response):
        if response is None or len(response) < 10:
            self.tenzo_update_rate = Default_Device_Configuration.tenzo_update_rate_default
            self.base_diameter = Default_Device_Configuration.base_diameter_default
            self.motor_speed_base = Default_Device_Configuration.motor_speed_base_default
            self.motor_accel_base = Default_Device_Configuration.motor_accel_base_default
            self.motor_maxspeed_base = Default_Device_Configuration.motor_MaxSpeed_base_default
            self.motor_speed_head = Default_Device_Configuration.motor_speed_head_default
            self.motor_accel_head = Default_Device_Configuration.motor_accel_head_default
            self.motor_maxspeed_head = Default_Device_Configuration.motor_MaxSpeed_head_default
            self.motor_returning_speed_head = Default_Device_Configuration.motor_returning_speed_head_default
            self.motor_returning_accel_head = Default_Device_Configuration.motor_returning_accel_head_default
        else:
            self.tenzo_update_rate = response[0]
            self.base_diameter = response[1]
            self.motor_speed_base = response[2]
            self.motor_accel_base = response[3]
            self.motor_maxspeed_base = response[4]
            self.motor_speed_head = response[5]
            self.motor_accel_head = response[6]
            self.motor_maxspeed_head = response[7]
            self.motor_returning_speed_head = response[8]
            self.motor_returning_accel_head = response[9]