#!/usr/bin/env python3

"""
Course: ECE 4574
Team: fCsGsU - SafeWaze
Author: Fonte Clanton
Date: November 7, 2020

Modified: November 10, 2020
Add documentation

This module provides an implementation of the SignUpDialog class. This class
is used when the user is attempting to make a new account.
"""

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
        """
        Instantiates a DBHelper and sets up signal and slot connections.

        :return: None
        """
        self._db = dbhelper.DBHelper()

        self.rejected.connect(lambda: self._reset_all())
        self.account_created.connect(lambda: self._reset_all())

    # Overrides QDialog.accept() method
    def accept(self):
        """
        Attempts to verify information entered by the user to allow the
        creation of a new account. This method overrides the default
        QDialog.accept() method in order to keep the window open in the event
        where the user's information cannot be validated.

        :return: None
        """
        self._verify_user_info()

    def _verify_user_info(self):
        """
        Verify the data from the user. Ensures all fields are compliant to
        specifications. In the event that an error is found, a helpful
        error message is given and the text of label corresponding to that
        field will be set to red.

        Verifies the following conditions:
        Username: 4-32 alphanumeric characters and must begin with a letter
        Email: {user}@{domain}.{tld}
        Password: 8-32 alphanumeric characters
        Password text and confirmation password text match
        Username is not found within the password

        :return: None
        """
        error_string = 'The following issues were found:\n\n'
        sign_up_error = False

        # Assume no errors or errors have been corrected by setting label
        # colors to black
        self._set_label_color_all('black')
        if not self._valid_username(self.lineEdit_username.text()):
            error_string += 'Invalid username:\nMust be between four (4) and ' \
                            'thirty-two (32) alphanumeric characters and ' \
                            'begin with a letter.\n\n'
            self._set_widget_color(self.label_username, 'red')
            sign_up_error = True

        if not self._valid_email(self.lineEdit_email.text()):
            error_string += 'Invalid email address.\n\n'
            self._set_widget_color(self.label_email, 'red')
            sign_up_error = True

        if not self._valid_password(self.lineEdit_password.text()):
            error_string += 'Invalid password:\nMust be between eight (8) and ' \
                            'thirty-two (32) alphanumeric characters.\n\n'
            self._set_widget_color(self.label_password, 'red')
            self._set_widget_color(self.label_confirm_password, 'red')
            sign_up_error = True

        # Check if password and password confirmation match
        password = self.lineEdit_password.text()
        confirm_password = self.lineEdit_confirm_password.text()
        if password != confirm_password:
            error_string += 'Passwords must match.\n\n'
            self._set_widget_color(self.label_confirm_password, 'red')
            sign_up_error = True

        # Check if username is in password
        username = self.lineEdit_username.text()
        username_in_password = username in password and password != ''
        if username_in_password:
            error_string += 'Password must not contain the username.'
            sign_up_error = True
            self._set_widget_color(self.label_password, 'red')
            self._set_widget_color(self.label_confirm_password, 'red')

        if sign_up_error:
            QMessageBox.critical(self, 'Error', error_string)
        else:
            new_username = self.lineEdit_username.text().lower()
            new_email = self.lineEdit_email.text().lower()
            new_password = self.lineEdit_password.text()
            # TODO: Figure out fields
            document = {
                "name": new_username,
                "email": new_email,
                "address": {
                    "street": "123 Main St.",
                    "city": "Richmond",
                    "state": "Virginia",
                    "zip_code": 23224
                },
                "dob": {
                    "month": 1,
                    "day": 31,
                    "year": 1996
                },
                "height": 68,
                "weight": 165,
                "healthy": True,
                "password": new_password
            }
            user_added = self._db.add_user(document)

            if not user_added:
                email_error = 'That email address is already in use.'
                QMessageBox.critical(self, 'Error', email_error)
                self._set_widget_color(self.label_email, 'red')
            else:
                QMessageBox.information(self, 'Success',
                                        'Account creation successful!')
                self.account_created.emit(self.lineEdit_email.text())
                self.close()

        return

    def _reset_all(self):
        """
        Clear all lineEdit text fields and set all label colors to black.
        The default behaviour of Qt is to keep the data from the lineEdit
        fields after closing the sign up dialog window. This method will
        ensure a clean start whenever the sign up button is clicked.

        :return: None
        """
        self.lineEdit_username.clear()
        self.lineEdit_email.clear()
        self.lineEdit_password.clear()
        self.lineEdit_confirm_password.clear()

        self._set_widget_color(self.label_username, 'black')
        self._set_widget_color(self.label_email, 'black')
        self._set_widget_color(self.label_password, 'black')
        self._set_widget_color(self.label_confirm_password, 'black')

    def _set_label_color_all(self, color):
        """
        Set all labels to the specified color.

        :param color: Choice of color to set the labels to
        :return: None
        """
        self._set_widget_color(self.label_username, color)
        self._set_widget_color(self.label_email, color)
        self._set_widget_color(self.label_password, color)
        self._set_widget_color(self.label_confirm_password, color)

    @staticmethod
    def _valid_username(username):
        """
        Perform regex matching to determine if the username is valid.
        Username must be 4-32 alphanumeric characters and must start with a
        letter.

        :param username: Username to be verified
        :return: True if valid, otherwise false
        """
        p = re.compile('^[A-Za-z][A-Za-z0-9]{3,32}$')

        return p.match(username)

    @staticmethod
    def _valid_email(email):
        """
        Perform regex matching to determine if the email address is valid.
        Email address must be of the form "{user}@{domain}.{tld}" without any
        special characters other than the "@" and ".".

        :param email: Email address to be verified
        :return: True if valid, otherwise false
        """
        p = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$')

        return p.match(email)

    @staticmethod
    def _valid_password(password):
        """
        Perform regex matching to determine if the password is valid.
        Password must be between 8-32 alphanumeric characters.

        :param password: Password to be verified
        :return: True if valid, otherwise false
        """
        p = re.compile('^[A-Za-z0-9]{8,32}$')

        return p.match(password)
        pass

    @staticmethod
    def _set_widget_color(widget, color):
        """
        Set a widget's color to the specified color.
        :param widget: Widget whose color will be modified
        :param color: The color to change to
        :return: None
        """
        widget.setStyleSheet(
            f'color: {color};'
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sign_up_dialog = SignUpDialog()
    sign_up_dialog.show()
    sys.exit(app.exec_())
