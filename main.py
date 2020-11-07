#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication
from package.ui.dashboard import Dashboard
from package.ui.loginform import LoginForm


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginForm()
    login.show()

    # Dashboard is not shown until password_good signal is emitted
    main_window = Dashboard()

    login.password_good.connect(lambda: main_window.show())
    login.password_good.connect(lambda: login.deleteLater())

    sys.exit(app.exec_())
