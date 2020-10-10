# This Python file uses the following encoding: utf-8
import sys

from PyQt5.QtWidgets import QApplication
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from test import Ui_main
from package.ui.logingui import LoginGUI


# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
#
#         self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginGUI()
    # mainwindow = MainWindow()
    sys.exit(app.exec_())
