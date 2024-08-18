from PyQt5.QtCore import QThread, pyqtSignal
from Logic.Managers.disc_scanManager import DiscScanManager


class DiscScanThread(QThread):
    update_signal = pyqtSignal(object)

    def __init__(self, method_name, *args, **kwargs):
        super().__init__()
        self.bd_manager = DiscScanManager()
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

    def addScan(self, disc_id, is_training=bool):
        return self.bd_manager.addScan(disc_id, is_training)

    def getCurrentScanID(self):
        return self.bd_manager.getCurrentScanID()

    def NotCurrentYet(self, disc_scan_id):
        return self.bd_manager.NotCurrentYet()

    def getScanIDList(self, disc_id):
        return  self.bd_manager.getScanIDList(disc_id)

    def deleteScan(self, disc_id):
        return self.bd_manager.deleteScan(disc_id)

    def deleteCurrentScan(self):
        return self.bd_manager.deleteCurrentScan()