from Logic.Managers.DataBaseManager import DBManager
from config import Default_Device_Configuration, Device_Configuration

class Device_Configuration_Manager():
    def __init__(self):
        self.db_connection = DBManager()
        self.default_config = Default_Device_Configuration() #подтягиваем дефолтные значения из конфига и используем их
    #     в случае если не были переданы необходимые данные


    def getConfigsIDList(self):
        sql = "SELECT id FROM public.device_configs;"
        try:
            result = self.db_connection.fetch_all(sql)
            id_list = [row[0] for row in result]  # Преобразование списка кортежей в список значений
            return id_list
        except Exception as e:
            print(f"Ошибка при получении списка id: {e}")
            return None
    def create_new_config(self, config:Device_Configuration): #конфиг создается в любом случае, если переданные данные неверные, то они подтягиваются из конфига
        config.base_diameter = config.base_diameter if config.base_diameter is not None else self.default_config.base_diameter_default
        config.motor_speed_base = config.motor_speed_base if config.motor_speed_base is not None else self.default_config.motor_speed_base_default
        config.motor_accel_base = config.motor_accel_base if config.motor_accel_base is not None else self.default_config.motor_accel_base_default
        config.motor_MaxSpeed_base = config.motor_MaxSpeed_base if config.motor_MaxSpeed_base is not None else self.default_config.motor_MaxSpeed_base_default

        config.motor_speed_head = config.motor_speed_head if config.motor_speed_head is not None else self.default_config.motor_speed_head_default
        config.motor_accel_head = config.motor_accel_head if config.motor_accel_head is not None else self.default_config.motor_accel_head_default
        config.motor_MaxSpeed_head = config.motor_MaxSpeed_head if config.motor_MaxSpeed_head is not None else self.default_config.motor_MaxSpeed_head_default
        config.motor_returning_speed_head = config.motor_returning_speed_head if config.motor_returning_speed_head is not None else self.default_config.motor_returning_speed_head_default
        config.motor_returning_accel_head = config.motor_returning_accel_head if config.motor_returning_accel_head is not None else self.default_config.motor_returning_accel_head_default

        config.tenzo_update_rate_default = config.tenzo_update_rate_default if config.tenzo_update_rate_default is not None else self.default_config.tenzo_update_rate_default

        sql = """INSERT INTO public.device_configs(
            tenzo_update_rate, base_diameter, motor_speed_base, motor_accel_base, motor_maxspeed_base, motor_speed_head, motor_accel_head,
         motor_maxspeed_head, motor_returning_speed_head, motor_returning_accel_head, is_current)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        params = (
            config.tenzo_update_rate_default,
            config.base_diameter,
            config.motor_speed_base,
            config.motor_accel_base,
            config.motor_MaxSpeed_base,
            config.motor_speed_head,
            config.motor_accel_head,
            config.motor_MaxSpeed_head,
            config.motor_returning_speed_head,
            config.motor_returning_accel_head,
            False
        )
        try:
            return self.db_connection.execute_query(sql, params)
        except Exception as e:
            print(f"Ошибка при создании нового конфига: {e}")
            return False
    def get_current_config(self, id):
        sql = """SELECT id, tenzo_update_rate, base_diameter, motor_speed_base, motor_accel_base, motor_maxspeed_base, motor_speed_head, motor_accel_head, motor_maxspeed_head, motor_returning_speed_head, motor_returning_accel_head
	FROM public.device_configs WHERE id = %s;"""
        try:
            results = self.db_connection.fetch_one(sql, (id,))
            return_config = Device_Configuration()
            return_config.config_id = results[0]
            return_config.tenzo_update_rate = results[1]
            return_config.base_diameter = results[2]
            return_config.motor_speed_base = results[3]
            return_config.motor_accel_base = results[4]
            return_config.motor_MaxSpeed_base = results[5]
            return_config.motor_speed_head = results[6]
            return_config.motor_accel_head = results[7]
            return_config.motor_MaxSpeed_head = results[8]
            return_config.motor_returning_speed_head = results[9]
            return_config.motor_returning_accel_head = results[10]
            return return_config
        except Exception as e:
            print(f"Ошибка при выводе конфига: {e}")

    def make_config_current(self, id):
        sql = """UPDATE public.device_configs
	SET is_current=%s WHERE id=%s;
        """
        params = (True, id,)
        try:
            return self.db_connection.execute_query(sql, params)
        except Exception as e:
            print(f"Ошибка при установлени япараметра текущим: {e}")
            return False

    def reset_current_config(self):
        sql = """
        UPDATE public.device_configs
        SET is_current = %s;
        """
        params = (False,)
        try:
            return self.db_connection.execute_query(sql, params)

        except Exception as e:
            print(f"Ошибка при сбросе конфигураций: {e}")
            return False

    def update_current_config(self, config: Device_Configuration):
        # Заполнение значений по умолчанию
        config.base_diameter = config.base_diameter if config.base_diameter is not None else self.default_config.base_diameter_default
        config.motor_speed_base = config.motor_speed_base if config.motor_speed_base is not None else self.default_config.motor_speed_base_default
        config.motor_accel_base = config.motor_accel_base if config.motor_accel_base is not None else self.default_config.motor_accel_base_default
        config.motor_MaxSpeed_base = config.motor_MaxSpeed_base if config.motor_MaxSpeed_base is not None else self.default_config.motor_MaxSpeed_base_default

        config.motor_speed_head = config.motor_speed_head if config.motor_speed_head is not None else self.default_config.motor_speed_head_default
        config.motor_accel_head = config.motor_accel_head if config.motor_accel_head is not None else self.default_config.motor_accel_head_default
        config.motor_MaxSpeed_head = config.motor_MaxSpeed_head if config.motor_MaxSpeed_head is not None else self.default_config.motor_MaxSpeed_head_default
        config.motor_returning_speed_head = config.motor_returning_speed_head if config.motor_returning_speed_head is not None else self.default_config.motor_returning_speed_head_default
        config.motor_returning_accel_head = config.motor_returning_accel_head if config.motor_returning_accel_head is not None else self.default_config.motor_returning_accel_head_default

        config.tenzo_update_rate_default = config.tenzo_update_rate_default if config.tenzo_update_rate_default is not None else self.default_config.tenzo_update_rate_default

        sql = """
            UPDATE public.device_configs
            SET tenzo_update_rate=%s, base_diameter=%s, motor_speed_base=%s, motor_accel_base=%s, motor_maxspeed_base=%s,
                motor_speed_head=%s, motor_accel_head=%s, motor_maxspeed_head=%s, motor_returning_speed_head=%s, motor_returning_accel_head=%s
            WHERE is_current = TRUE
            """
        params = (
            config.tenzo_update_rate_default,
            config.base_diameter,
            config.motor_speed_base,
            config.motor_accel_base,
            config.motor_MaxSpeed_base,
            config.motor_speed_head,
            config.motor_accel_head,
            config.motor_MaxSpeed_head,
            config.motor_returning_speed_head,
            config.motor_returning_accel_head,
        )

        try:
            return self.db_connection.execute_query(sql, params)
        except Exception as e:
            print(f"Ошибка при создании нового конфига: {e}")
            return False

    def delete_current_config(self):
        sql = "DELETE FROM public.device_configs WHERE is_current = TRUE"

        try:
            return self.db_connection.execute_query(sql)
        except Exception as e:
            print(f"Ошибка при удалении текущего конфига: {e}")
            return False

    def find_current_config(self):
        sql = """SELECT tenzo_update_rate, base_diameter, motor_speed_base, motor_accel_base, motor_maxspeed_base, motor_speed_head, motor_accel_head, motor_maxspeed_head, motor_returning_speed_head, motor_returning_accel_head
	FROM public.device_configs WHERE is_current = TRUE;"""
        try:
            result = self.db_connection.fetch_all(sql)
            output_list = [row[0] for row in result]  # Преобразование списка кортежей в список значений
            return output_list
        except Exception as e:
            print(f"Ошибка при получении текущих параметров: {e}")
            return None

    def close(self):
        self.db_connection.close()
