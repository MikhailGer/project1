from PyQt5.QtCore import QThread, pyqtSignal
from Managers.device_configManager import Device_Configuration_Manager


class DeviceConfigThread(QThread):
    update_signal = pyqtSignal(object)

    def __init__(self, method_name, *args, **kwargs):
        super().__init__()
        self.bd_manager = Device_Configuration_Manager()
        self.method_name = method_name
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            if hasattr(self, self.method_name):
                method = getattr(self, self.method_name)
                answer = method(*self.args, **self.kwargs)
                # print(answer)
                self.update_signal.emit(answer)
            else:
                raise AttributeError(f"Method {self.method_name} not found")
        except Exception as e:
            print(f"Error fetching parameters: {e}")
            self.update_signal.emit([])  # В случае ошибки отправляем пустой список или обрабатываем ошибку другим способом
        finally:
            self.bd_manager.close()

    def getConfigsIDList(self):
        return self.bd_manager.getConfigsIDList()

    def create_new_config(self, config):
        return self.bd_manager.create_new_config(config)

    def get_current_config(self,id):
        return self.bd_manager.get_current_config(id)

    def make_config_current(self, config_id):
        return self.bd_manager.make_config_current(config_id)

    def reset_current_config(self):
        return self.bd_manager.reset_current_config()

    def update_current_config(self, config):
        return self.bd_manager.update_current_config(config)

    def delete_current_config(self):
        return self.bd_manager.delete_current_config()

    def find_current_config(self):
        return self.bd_manager.find_current_config()

    def close(self):
        self.quit()
        self.wait()
