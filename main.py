# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2.QtWidgets import QApplication, QWidget, QMainWindow
from PySide2.QtCore import QFile, QUrl
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWebEngineWidgets import QWebEngineView
#from test import Ui_main


class main(QWidget):
    def __init__(self):
        super(main, self).__init__()
        self.load_ui()

        self.browser = self.findChild(QWebEngineView, "browser")

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
    my_web = QWebEngineView()
    my_web.load(QUrl("https://www.stackoverflow.com"))
    my_web.show()
    widget = main()
    widget.show()
#    widget.browser = QWebEngineView()
    widget.browser.load(QUrl("www.vt.edu"))
    sys.exit(app.exec_())

"""
class MainWindow(QMainWindow, Ui_main):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.browser.load(QUrl("www.stackoverflow.com"))
        self.setWindowTitle("Hello Python World!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.retranslateUi(mainWindow)
#    mainWindow.setupUi(mainWindow)
    mainWindow.show()
    mainWindow.browser.load(QUrl("www.stackoverflow.com"))
    sys.exit(app.exec_())
"""
