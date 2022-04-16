#no need to install anything
import sys
# pip install pyqt5, pip install pyqt5 tools
from PyQt5.QtWidgets import QApplication,QMainWindow
# just change the name
from test import Ui_MainWindow

class MainWindow:
    def __init__(self):
        # the way app working
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.Button_stop.clicked.connect(self.main_win.close)

    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    # run app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())