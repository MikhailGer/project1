from PyQt5.QtCore import QThread, pyqtSignal
from Managers.bladeManager import BladeManager


class DiscScanThread(QThread):
    update_signal = pyqtSignal(object)

    def __init__(self, method_name, *args, **kwargs):
        super().__init__()
        self.bd_manager = BladeManager()
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
            self.update_signal.emit(
                [])  # В случае ошибки отправляем пустой список или обрабатываем ошибку другим способом
        finally:
            self.bd_manager.close()

    def addBlade(self, disc_scan_id, num, scan, prediction):
        return self.bd_manager.addBlade(disc_scan_id, num, scan, prediction)

    def getBladeList(self, disc_scan_id):
        return self.bd_manager.getBladeList(disc_scan_id)

    def getBlade(self, blade_id):
        return self.bd_manager.getBlade(blade_id)

