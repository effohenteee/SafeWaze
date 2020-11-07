#!/usr/bin/env python3

import random
import sys
import package.util.dbhelper as dbhelper

from PyQt5.QtCore import QMargins, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtChart import QBarCategoryAxis, QBarSeries, \
    QBarSet, QChart, QChartView
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget


class ChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initialize_ui()

    def initialize_ui(self):
        self.chart_view = QChartView(self)
        self.chart_view.setMinimumHeight(300)
        self.chart_view.resize(800,600)
        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.chart_view)

    def plot_random(self):
        random.seed()
        data = [random.randint(0, 30) for i in range(20)]
        set0 = QBarSet('Random Result')

        for x in data:
            set0 << x

        series = QBarSeries()
        series.append(set0)

        chart = QChart(flags=Qt.Widget)
        chart.addSeries(series)
        chart.setTitle("Random Numbers")

        legend = chart.legend()
        legend.setAlignment(Qt.AlignBottom)

        chart.createDefaultAxes()
        chart.axisX().setLabelsAngle(-90)
        chart.axisX().setTitleText('Iteration')
        chart.axisY().setTitleText('Result')
        chart.setMargins(QMargins(0, 0, 0, 0))

        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setChart(chart)

    def update_chart(self, num_ticks=10):
        self.db = dbhelper.DBHelper()
        results = self.db.get_results_database()
        new_cases_list, dates_list = [], []

        if results.count() + 1 < num_ticks:
            return None

        for i in range(num_ticks):
            current_date = results[i]['report_date']
            current_date = current_date.strftime(format='%m/%d')
            next_cases = int(results[i]['number_of_cases'])
            previous_cases = int(results[i + 1]['number_of_cases'])
            new_cases = next_cases - previous_cases

            dates_list.insert(0, current_date)
            new_cases_list.insert(0, new_cases)

        self.chart_view.chart().deleteLater()

        set0 = QBarSet('Daily COVID Cases')

        for x in new_cases_list:
            set0 << x

        series = QBarSeries()
        series.append(set0)

        chart = QChart(flags=Qt.Widget)
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setTitle("New Blacksburg COVID Cases by Date")

        legend = chart.legend()
        legend.setAlignment(Qt.AlignBottom)

        categories = dates_list
        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.setAxisX(axis, series)
        chart.axisX().setLabelsAngle(-90)
        chart.setMargins(QMargins(0, 0, 0, 0))

        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setChart(chart)

        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mplwidget1 = ChartWidget()
    mplwidget2 = ChartWidget()
    mplwidget1.plot_random()
    mplwidget2.update_chart()
    mplwidget1.show()
    mplwidget2.show()
    sys.exit(app.exec_())
