from PyQt5.QtCore import QThread, pyqtSignal
from Logic.Managers.paramManager import ParameterManager


class ParamsThread(QThread):
    update_signal = pyqtSignal(object)

    def __init__(self, method_name, *args, **kwargs):
        super().__init__()
        self.bd_manager = ParameterManager()
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

    def GetParamList(self):
        return self.bd_manager.getParamtersIDList()

    def GetParam(self, id):
        return self.bd_manager.getParam(id)

    def CreateNewParam(self, diameter, blade_distance, blade_force):
        return self.bd_manager.createNewParam(diameter, blade_distance, blade_force)

    def DeleteParam(self, id):
        return self.bd_manager.deleteParam(id)
