#!/usr/bin/env python3

"""
Course: ECE 4574
Team: fCsGsU - SafeWaze
Author: Fonte Clanton
Date: October 11, 2020

Modified: November 10, 2020
Add documentation
Modified: November 22, 2020
Add RSS feed to widget

The Dahsboard is where the everything is displayed for the user including:
COVID-19 statistics, risk factors, mapping, and directions.
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow, \
    QVBoxLayout
from PySide2.QtCore import QUrl
from PySide2.QtQml import QQmlApplicationEngine

import package.util.rsshelper as rsshelper
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

        self.engine = QQmlApplicationEngine()

        self.frame_graph.deleteLater()
        self.chart = ChartWidget()
        self.chart.update_chart(14)
        self.vbox_tab_1.addWidget(self.chart)
        self._center_window()

        # TODO: Implement text scaling?
        url = 'https://tools.cdc.gov/api/v2/resources/media/404952.rss'
        self.rss = rsshelper.RSSHelper(url)
        title = self.rss[0]['title']
        link = self.rss[0]['link']
        ahref = f"<a href=\"{link}\">{title}</a>"
        date = self.rss[0]['published']
        summary = self.rss[0]['summary']
        self.label_rss_title.setText(ahref)
        self.label_rss_date.setText(date)
        self.textBrowser_summary.setText(summary)

        # Connections for changing displayed RSS feed article
        self.radioButton_1.clicked.connect(lambda: self._select_feed())
        self.radioButton_2.clicked.connect(lambda: self._select_feed())
        self.radioButton_3.clicked.connect(lambda: self._select_feed())
        self.radioButton_4.clicked.connect(lambda: self._select_feed())
        self.radioButton_5.clicked.connect(lambda: self._select_feed())
        self.radioButton_6.clicked.connect(lambda: self._select_feed())
        self.radioButton_7.clicked.connect(lambda: self._select_feed())

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

    def _select_feed(self):
        title, link, date, summary = ('', '', '', '')
        rb_list = [self.radioButton_1, self.radioButton_2, self.radioButton_3,
                   self.radioButton_4, self.radioButton_5, self.radioButton_6,
                   self.radioButton_7]

        for index, button in enumerate(rb_list):
            if button.isChecked():
                title = self.rss[index]['title']
                link = self.rss[index]['link']
                date = self.rss[index]['published']
                summary = self.rss[index]['summary']
                break

        ahref = f"<a href=\"{link}\">{title}</a>"
        self.label_rss_title.setText(ahref)
        self.label_rss_date.setText(date)
        self.textBrowser_summary.setText(summary)

        return

    def show_map(self):
        self.engine.load(QUrl.fromLocalFile('main.qml'))

        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec_())
