from PyQt5.QtCore import QThread, pyqtSignal
from Logic.Managers.discManager import DiscManager


class DiscThread(QThread):
    update_signal = pyqtSignal(object)

    def __init__(self, method_name, *args, **kwargs):
        super().__init__()
        self.bd_manager = DiscManager()
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

    def DowloadDiscList(self, mode):
        return self.bd_manager.getDiscsList(mode)

    def CreateNewDiscWithName(self, name, param_id):
        return self.bd_manager.createNewDiscWithName(name, param_id)

    def CreateNewDiscWithID(self, id, name, param_id):
        return self.bd_manager.createNewDiscWithID(id, name, param_id)

    def DeleteDisc(self, id_or_name, mode):
        return self.bd_manager.deleteDisc(id_or_name, mode)
