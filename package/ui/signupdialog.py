#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from package.ui.signupdialog_ui import Ui_SignUpDialog


class SignUpDialog(QDialog, Ui_SignUpDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initialize_ui()

    def initialize_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sign_up_dialog = SignUpDialog()
    sign_up_dialog.show()
    sys.exit(app.exec_())


