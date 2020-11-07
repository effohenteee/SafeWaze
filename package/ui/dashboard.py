#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow
from PyQt5.QtCore import Qt

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
