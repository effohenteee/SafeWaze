#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from test import Ui_main
from package.ui.dashboard import Dashboard
from package.ui.loginform import LoginForm


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginForm()
    login.show()

    if login.exec_() is not None:
        main_window = Dashboard()
        main_window.show()

    sys.exit(app.exec_())
