#!/usr/bin/env python3

import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QDesktopWidget, QDialog, QLabel, QMessageBox

from package.ui.loginform_ui import Ui_LoginWidget
from package.ui.signupdialog import SignUpDialog
from package.util.dbhelper import DBHelper

PRODUCTION = True
LOAD_ANIMATION = False

PASSWORD_NEEDED = False
PASSWORD_GOOD = False


class LoginForm(QDialog, QtWidgets.QWidget, Ui_LoginWidget):
    password_good = pyqtSignal()
    password_bad = pyqtSignal()

    if not PASSWORD_NEEDED:
        start_wait = pyqtSignal()
        stop_wait = pyqtSignal()

    def __init__(self, parent=None):
        super(LoginForm, self).__init__(parent)
        self.setupUi(self)
        self._initialize_ui()

    def _initialize_ui(self):
        # TODO: Docs
        # Custom widgets have stylesheets disabled by default, so enable it
        # https://stackoverflow.com/a/57786338
        # self.setAttribute(Qt.WA_StyledBackground, True)

        self.setWindowFlags(
            Qt.WindowMinimizeButtonHint |
            Qt.WindowCloseButtonHint
        )

        self.signup = SignUpDialog(self)
        self.db = DBHelper()
        self._center_window()

        self._credentials = None

        # Connections
        if PRODUCTION:
            # TODO: (Stretch goal) Eventually, I would like to get a loading
            #  animation while authenticating the user. I am able to get the
            #  animation to start and stop correctly when using signals and
            #  slots but doesn't seem to work by just calling the functions
            #  the old fashioned way.
            self.button_sign_in.clicked.connect(
                lambda: self._attempt_login())
            self.button_sign_up.clicked.connect(
                lambda: self._open_signup_dialog())
            self.signup.account_created.connect(
                lambda x: self.lineEdit_email.setText(x))
            self.signup.account_created.connect(
                lambda: self.lineEdit_password.setFocus())

        else:
            self.lineEdit_email.setText('NON PRODUCTION CODE')
            if LOAD_ANIMATION:
                self.button_sign_in.clicked.connect(
                    lambda: self._start_load_animation())
                self.button_sign_up.clicked.connect(
                    lambda: self._stop_load_animation())

            if not PASSWORD_NEEDED:
                self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Normal)
                if PASSWORD_GOOD:
                    self.lineEdit_password.setText('PASSWORD IS ALWAYS GOOD')
                    self.button_sign_in.clicked.connect(
                        lambda: self._password_always_good())
                else:
                    self.lineEdit_password.setText('PASSWORD IS ALWAYS BAD')
                    self.button_sign_in.clicked.connect(
                        lambda: self._password_always_bad())

    def _attempt_login(self):
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()

        self._credentials = self.db.authenticate_user(email, password)

        if not self._credentials:
            self._show_failed_login_message()
        else:
            self.password_good.emit()

        return

    def _center_window(self):
        rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center_point)
        self.move(rectangle.topLeft())

    def _open_signup_dialog(self):
        self.signup.lineEdit_username.setFocus()
        self.signup.show()

    def _start_load_animation(self):
        # TODO: Docs
        self.label_loading = QLabel(self)
        self.label_loading.setGeometry(140, 300, 200, 140)
        self.movie_loading = QMovie(
            '../../Resources/Loading-Animations/small_loading.gif')
        self.label_loading.setMovie(self.movie_loading)
        self.label_loading.show()
        self.movie_loading.start()  # Non-blocking

    def _stop_load_animation(self):
        # TODO: Docs
        self.movie_loading.stop()
        self.label_loading.deleteLater()
        del self.movie_loading

    def _password_always_good(self):
        # This always returns emits password_good
        # TESTING PURPOSES ONLY
        self.password_good.emit()

    def _password_always_bad(self):
        self._show_failed_login_message()
        self.password_bad.emit()

    def _show_failed_login_message(self):
        # Error message from Twitter.
        # It's friendly, but still gets the message across.
        error = ('The username and password you entered does not match our '
                 'records. Please double-check and try again.')
        QMessageBox.warning(self, 'Sign In', error,
                            QMessageBox.Ok, QMessageBox.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = LoginForm()
    login.show()
    sys.exit(app.exec_())
