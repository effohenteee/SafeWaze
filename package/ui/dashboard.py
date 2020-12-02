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
Modified: November 30, 2020
Add map to project
Modified: December 2, 2020
Integrate risk analysis

The Dashboard is where the everything is displayed for the user including:
COVID-19 statistics, risk factors, mapping, and directions.
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow
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

        self.pushButton.clicked.connect(lambda: self.update_risk())

        self.lcdNumber_risk.display(0)
        self.risk_barometer.setValue(100)

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
        self.engine.load(QUrl.fromLocalFile('package/ui/main.qml'))

        return

    def update_risk(self):
        index_box0 = self.comboBox_0.currentIndex()
        index_box1 = self.comboBox_1.currentIndex()
        index_box2 = self.comboBox_2.currentIndex()
        index_box3 = self.comboBox_3.currentIndex()

        # type of place
        if index_box0 == 0:
            risk_place = 1
            time_spent = 1
        elif index_box0 == 1:
            risk_place = 2
            time_spent = 3
        elif index_box0 == 2:
            risk_place = 4
            time_spent = 3
        elif index_box0 == 3:
            risk_place = 9
            time_spent = 4
        elif index_box0 == 4:
            risk_place = 6
            time_spent = 4
        elif index_box0 == 5:
            risk_place = 10
            time_spent = 3
        elif index_box0 == 6:
            risk_place = 9
            time_spent = 2
        else:
            risk_place = 3  # other place.
            time_spent = 3

            # number of people interacted with
        if index_box1 == 0:
            risk_person = 0
        elif index_box1 == 1:
            risk_person = 1
        elif index_box1 == 2:
            risk_person = 3
        elif index_box1 == 3:
            risk_person = 5
        elif index_box1 == 4:
            risk_person = 7
        elif index_box1 == 5:
            risk_person = 9
        else:
            risk_person = 18

            # social distancing
        if index_box3 == 0:
            risk_multiplier = 1
        elif index_box3 == 1:
            risk_multiplier = 3
        else:
            risk_multiplier = 2

            # mask or shield
        if index_box2 == 0:
            risk_add = 1
        elif index_box2 == 1:
            risk_add = 12
        else:
            risk_add = (risk_place * risk_multiplier) + (risk_person / 2)

        risk_final = risk_add + (risk_place * time_spent) / 2 + risk_person + 28

        self.lcdNumber_risk.display(risk_final)
        bar_value = 100 - risk_final
        self.risk_barometer.setValue(bar_value)

        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec_())
