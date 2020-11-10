#!/usr/bin/env python3

"""
Course: ECE 4574
Team: fCsGsU - SafeWaze
Author: Fonte Clanton
Date: September 21, 2020

Modified: November 10, 2020
Add documentation

Allows the user to log in or sign up with a new account.
"""


import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QDesktopWidget, QDialog, QLabel, QMessageBox

from package.ui.loginform_ui import Ui_LoginWidget
from package.ui.signupdialog import SignUpDialog
from package.util.dbhelper import DBHelper

# Flags for debugging and production testing
PRODUCTION = False
LOAD_ANIMATION = False

PASSWORD_NEEDED = False
PASSWORD_GOOD = True


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
        """
        Initialize the UI based on the flags: PRODUCTION, and PASSWORD_GOOD.

        PRODUCTION: If true, the user must log in with a valid email and
        password. Sign up widget is enabled. If false, no password is needed
        and sign up widget is disabled.

        PASSWORD_GOOD: If true, no password is needed to proceed to the
        dashboard. Useful for developers and debugging.

        PRODUCTION is mutually exclusive with PASSWORD_GOOD. This should
        prevent releasing code that performs no authentication to users.

        Logical combinations are:

        - PRODUCTION == True (Release code)

        - PRODUCTION == False && PASSWORD_GOOD == True (Will always proceed to
        dashboard)

        - PRODUCTION == False && PASSWORD_GOOD == False (Will always error on
        login attempt)

        :return: None
        """
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
        """
        Use the email and password field text to attempt to authenticate the
        user.

        :return: None
        """
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()

        self._credentials = self.db.authenticate_user(email, password)

        if not self._credentials:
            self._show_failed_login_message()
        else:
            self.password_good.emit()

        return

    def _center_window(self):
        """
        Center the dashboard window on the screen.

        :return: None
        """
        rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center_point)
        self.move(rectangle.topLeft())

    def _open_signup_dialog(self):
        """
        The sign up dialog box is always instantiated in the main program,
        but hidden until the sign up button is clicked. This method sets the
        focus to the top username field and shows the widget.

        :return: None
        """
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
        """
        Emit password_good signal.

        :return: None
        """
        # This always returns emits password_good
        # TESTING PURPOSES ONLY
        self.password_good.emit()

    def _password_always_bad(self):
        """
        Emit password_base signal and show error message.

        :return: None
        """
        self._show_failed_login_message()
        self.password_bad.emit()

    def _show_failed_login_message(self):
        """
        Displays error message about failed login attempt.

        Error message from Twitter.

        It's friendly, but still gets the message across.

        :return: None
        """
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
