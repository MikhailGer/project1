import sys

from PyQt5.QtWidgets import QApplication

from SettingGUI.ControlPanelWindow import App


def main():
    app = QApplication(sys.argv)
    mainWindow = App()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
