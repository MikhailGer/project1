from dataclasses import dataclass
from typing import Optional

#база данных
host = "127.0.0.1"
user = "postgres"
password = "87654321"
db_name = "discs"

#serial port
operating_port = "ttyUSB0"
SerialBaudRate = 115200  #на ардуино в скетче 115200


#параметры установки
@dataclass
class Default_Device_Configuration:
    base_diameter_default = 500.24  # в миллиметрах
    motor_speed_base_default = 1  # шаги двигателя в секунду (основание)
    motor_accel_base_default = 1
    motor_MaxSpeed_base_default = 1

    motor_speed_head_default = 1
    motor_accel_head_default = 1
    motor_MaxSpeed_head_default = 1
    motor_returning_speed_head_default = 1
    motor_returning_accel_head_default = 1

    head_working_pos = 300 #нужно будет замерить в ручную и сдлеать значение постоянным

    tenzo_update_rate_default = 10

@dataclass
class Device_Configuration:
    config_id: Optional[int] = None
    base_diameter: Optional[float] = None  # в миллиметрах
    motor_speed_base: Optional[int] = None  # шаги двигателя в секунду (основание)
    motor_accel_base: Optional[int] = None
    motor_MaxSpeed_base: Optional[int] = None

    motor_speed_head: Optional[int] = None
    motor_accel_head: Optional[int] = None
    motor_MaxSpeed_head: Optional[int] = None
    motor_returning_speed_head: Optional[int] = None
    motor_returning_accel_head: Optional[int] = None

    tenzo_update_rate: Optional[int] = None