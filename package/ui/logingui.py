#!/usr/bin/env python3

import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QBrush, QImage, QMovie, QPalette
from PyQt5.QtWidgets import QDesktopWidget, QLabel, QMessageBox
from package.ui.loginform import Ui_LoginWidget as LoginWidget

PRODUCTION = False
DEBUG = False

PASSWORD_NEEDED = False
PASSWORD_GOOD = False


# noinspection PyAttributeOutsideInit
class LoginGUI(QtWidgets.QWidget, LoginWidget):
    password_good = pyqtSignal()
    password_bad = pyqtSignal()

    if not PASSWORD_NEEDED:
        start_wait = pyqtSignal()
        stop_wait = pyqtSignal()

    def __init__(self, parent=None):
        super(LoginGUI, self).__init__(parent)
        self.setupUi(self)
        self.initialize_ui()
        self.show()

    def initialize_ui(self):
        # TODO: Docs
        # Custom widgets have stylesheets disabled by default, so enable it
        # https://stackoverflow.com/a/57786338
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.center_window()

        # Connections
        if PRODUCTION:
            # TODO: (Stretch goal) Eventually, I would like to get a loading
            #  animation while authenticating the user. I am able to get the
            #  animation to start and stop correctly when using signals and
            #  slots but doesn't seem to work by just calling the functions
            #  the old fashioned way.
            self.button_sign_in.clicked.connect(
                lambda: self.start_load_animation()
            )
        else:
            if DEBUG:
                self.button_sign_in.clicked.connect(
                    lambda: self.start_load_animation()
                )
                self.button_sign_up.clicked.connect(
                    lambda: self.stop_load_animation()
                )
            if not PASSWORD_NEEDED:
                if PASSWORD_GOOD:
                    self.button_sign_in.clicked.connect(
                        lambda: self._password_always_good()
                    )
                else:
                    self.button_sign_in.clicked.connect(
                        lambda: self._password_always_bad()
                    )

    def center_window(self):
        rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center_point)
        self.move(rectangle.topLeft())

    def start_load_animation(self):
        # TODO: Docs
        self.label_loading = QLabel(self)
        self.label_loading.setGeometry(140, 300, 200, 140)
        self.movie_loading = QMovie(
            '../../Resources/Loading-Animations/small_loading.gif')
        self.label_loading.setMovie(self.movie_loading)
        self.label_loading.show()
        self.movie_loading.start()  # Non-blocking

    def stop_load_animation(self):
        # TODO: Docs
        self.movie_loading.stop()
        self.label_loading.deleteLater()
        del self.movie_loading

    def _password_always_good(self):
        # This always returns emits password_good
        # TESTING PURPOSES ONLY
        self.password_good.emit()

    def _password_always_bad(self):
        # Error message from Twitter.
        # It's friendly, but still gets the message across.
        error = ('The username and password you entered did not match our '
                 'records. Please double-check and try again.')
        QMessageBox.warning(self, 'Sign in', error,
                            QMessageBox.Ok, QMessageBox.Ok)
        self.password_bad.emit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = LoginGUI()
    sys.exit(app.exec_())


