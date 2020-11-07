#!/usr/bin/env python3

import re
import sys

import PyQt5.QtCore as QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

import package.util.dbhelper as dbhelper
from package.ui.signupdialog_ui import Ui_SignUpDialog


class SignUpDialog(QDialog, Ui_SignUpDialog):
    account_created = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._initialize_ui()

    def _initialize_ui(self):
        self._db = dbhelper.DBHelper()

        self.rejected.connect(lambda: self._reset_all())
        self.account_created.connect(lambda: self._reset_all())

    # Overrides QDialog.accept() method
    def accept(self):
        self._verify_user_info()

    def _verify_user_info(self):
        error_string = 'The following issues were found:\n\n'
        sign_up_error = False

        self._set_border_color_all('black')
        if not self._valid_username(self.lineEdit_username.text()):
            error_string += 'Invalid username:\nMust be between four (4) and ' \
                            'thirty-two (32) alphanumeric characters and ' \
                            'begin with a letter.\n\n'
            self._set_border_color(self.label_username, 'red')
            sign_up_error = True

        if not self._valid_email(self.lineEdit_email.text()):
            error_string += 'Invalid email address.\n\n'
            self._set_border_color(self.label_email, 'red')
            sign_up_error = True

        if not self._valid_password(self.lineEdit_password.text()):
            error_string += 'Invalid password:\nMust be between eight (8) and ' \
                            'thirty-two (32) alphanumeric characters.\n\n'
            self._set_border_color(self.label_password, 'red')
            self._set_border_color(self.label_confirm_password, 'red')
            sign_up_error = True

        # Check if both passwords match
        password = self.lineEdit_password.text()
        confirm_password = self.lineEdit_confirm_password.text()
        if password != confirm_password:
            error_string += 'Passwords must match.\n\n'
            self._set_border_color(self.label_confirm_password, 'red')
            sign_up_error = True

        # Check if username is in password
        username = self.lineEdit_username.text()
        username_in_password = username in password and password != ''
        if username_in_password:
            error_string += 'Password must not contain the username.'
            sign_up_error = True
            self._set_border_color(self.label_password, 'red')
            self._set_border_color(self.label_confirm_password, 'red')

        if sign_up_error:
            QMessageBox.critical(self, 'Error', error_string)
        else:
            new_username = self.lineEdit_username.text().lower()
            new_email = self.lineEdit_email.text().lower()
            user_added = self._db.add_user(
                new_username,
                new_email,
                self.lineEdit_password.text()
            )

            if not user_added:
                email_error = 'That email address is already in use.'
                QMessageBox.critical(self, 'Error', email_error)
                self._set_border_color(self.label_email, 'red')
            else:
                QMessageBox.information(self, 'Success',
                                        'Account creation successful!')
                self.account_created.emit(self.lineEdit_email.text())
                self.close()

        return

    def _reset_all(self):
        self.lineEdit_username.clear()
        self.lineEdit_email.clear()
        self.lineEdit_password.clear()
        self.lineEdit_confirm_password.clear()

        self._set_border_color(self.label_username, 'black')
        self._set_border_color(self.label_email, 'black')
        self._set_border_color(self.label_password, 'black')
        self._set_border_color(self.label_confirm_password, 'black')

    def _set_border_color_all(self, color):
        self._set_border_color(self.label_username, color)
        self._set_border_color(self.label_email, color)
        self._set_border_color(self.label_password, color)
        self._set_border_color(self.label_confirm_password, color)

    @staticmethod
    def _valid_username(username):
        p = re.compile('^[A-Za-z][A-Za-z0-9]{3,32}$')

        return p.match(username)

    @staticmethod
    def _valid_email(email):
        p = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$')

        return p.match(email)

    @staticmethod
    def _valid_password(password):
        p = re.compile('^[A-Za-z0-9]{8,32}$')

        return p.match(password)
        pass

    @staticmethod
    def _set_border_color(widget, color):
        widget.setStyleSheet(
            f'color: {color};'
        )




if __name__ == '__main__':
    app = QApplication(sys.argv)
    sign_up_dialog = SignUpDialog()
    sign_up_dialog.show()
    sys.exit(app.exec_())
