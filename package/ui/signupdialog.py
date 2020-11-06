#!/usr/bin/env python3

import package.util.dbhelper as dbhelper
import re
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from package.ui.signupdialog_ui import Ui_SignUpDialog


class SignUpDialog(QDialog, Ui_SignUpDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initialize_ui()

    def initialize_ui(self):
        self._db = dbhelper.DBHelper()

    def accept(self):
        self.verify_user_info()

    def verify_user_info(self):
        error_string = 'The following issues were found:\n\n'
        sign_up_error = False

        if self.verify_username(self.lineEdit_username.text()):
            self.set_border_color(self.label_username, 'black')
        else:
            error_string += 'Invalid username\n'
            self.set_border_color(self.label_username, 'red')
            sign_up_error = True

        if self.verify_email(self.lineEdit_email.text()):
            self.set_border_color(self.label_email, 'black')
        else:
            error_string += 'Invalid email address\n'
            self.set_border_color(self.label_email, 'red')
            sign_up_error = True

        if self.verify_password(self.lineEdit_password.text()):
            self.set_border_color(self.label_password, 'black')
            self.set_border_color(self.label_confirm_password, 'black')
        else:
            error_string += 'Invalid password\n'
            self.set_border_color(self.label_password, 'red')
            self.set_border_color(self.label_confirm_password, 'red')
            sign_up_error = True

        password = self.lineEdit_password.text()
        confirm_password = self.lineEdit_confirm_password.text()
        if password != confirm_password:
            error_string += 'Passwords must match\n'
            self.set_border_color(self.label_confirm_password, 'red')
            sign_up_error = True

        if sign_up_error:
            QMessageBox.critical(self, 'Error', error_string)

            return

        new_username = self.lineEdit_username.text().lower()
        new_email = self.lineEdit_email.text().lower()
        user_added = self._db.add_user(
            new_username,
            new_email,
            self.lineEdit_password.text()
        )

        if not user_added:
            email_error = 'This email address is already in use'
            QMessageBox.critical(self, 'Error', email_error)

            return

        QMessageBox.information(self, 'Success', 'Account creation successful')

        # TODO Close the log in window and insert the username into the field
        # emit a signal with the username??
        return

    def verify_username(self, username):
        p = re.compile('^[A-Za-z][A-Za-z0-9]{3,20}$')

        return p.match(username)

    def verify_email(self, email):
        p = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$')

        return p.match(email)

    def verify_password(self, password):
        p = re.compile('^[A-Za-z0-9]{8,32}$')

        return p.match(password)
        pass

    def set_border_color(self, widget, color):
        widget.setStyleSheet(
            f'color: {color};'
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sign_up_dialog = SignUpDialog()
    sign_up_dialog.show()
    sys.exit(app.exec_())


