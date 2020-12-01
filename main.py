#!/usr/bin/env python3

"""
Course: ECE 4574
Team: fCsGsU - SafeWaze
Author: Fonte Clanton
Date: September 24, 2020

Modified: November 10, 2020
Add documentation

Main program that instantiates the login form and dashboard. Signals are
connected to prevent the dashboard from showing any data until the login is
authenticated.
"""

from PyQt5.QtWidgets import QApplication
from package.ui.dashboard import Dashboard
from package.ui.loginform import LoginForm

import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginForm()
    login.show()

    # Dashboard is not shown until password_good signal is emitted
    main_window = Dashboard()

    login.password_good.connect(lambda: main_window.show())
    login.password_good.connect(lambda: login.deleteLater())
    login.password_good.connect(lambda: main_window.show_map())

    sys.exit(app.exec_())
