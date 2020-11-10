#!/usr/bin/env python3

"""
Course: ECE 4574
Team: fCsGsU - SafeWaze
Author: Fonte Clanton
Date: October 11, 2020

Modified: November 10, 2020
Add documentation

The Dahsboard is where the everything is displayed for the user including:
COVID-19 statistics, risk factors, mapping, and directions.
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow

from package.ui.chartwidget import ChartWidget
from package.ui.dashboard_ui import Ui_Dashboard


class Dashboard(QMainWindow, Ui_Dashboard):
    # TODO: Update stale data on login (medium priority)
    # TODO: Periodically check for new COVID data from Socrata (low priority)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._initialize_ui()
        return

    def _initialize_ui(self):
        """
        Enable minimize, maximize, and close buttons for the dashboard
        window. Replaces placeholder chart widget with a ChartWidget object.

        :return: None
        """
        self.setWindowFlags(
            Qt.WindowMinMaxButtonsHint |
            Qt.WindowCloseButtonHint
        )

        self.frame_graph.deleteLater()
        self.chart = ChartWidget()
        self.chart.update_chart(14)
        self.vbox_tab_1.addWidget(self.chart)
        self._center_window()

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

        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec_())
