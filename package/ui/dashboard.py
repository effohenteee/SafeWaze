#!/usr/bin/env python3

import sys
from pymongo import MongoClient
from datetime import datetime, timedelta
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, QWidget
from PyQt5.QtCore import Qt


from package.ui.dashboard_ui import Ui_Dashboard
from package.ui.mplwidget import MplWidget


class Dashboard(QMainWindow, Ui_Dashboard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initialize_ui()
        return

    def initialize_ui(self):
        self.setWindowFlags(
            Qt.WindowMinMaxButtonsHint |
            Qt.WindowCloseButtonHint
        )

        self.frame_graph.deleteLater()
        self.chart = MplWidget()
        self.vbox_tab_1.addWidget(self.chart)
        self.center_window()

        return

    def center_window(self):
        rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        rectangle.moveCenter(center_point)
        self.move(rectangle.topLeft())

        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec_())
