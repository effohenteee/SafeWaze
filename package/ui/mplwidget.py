#!/usr/bin/env python3

import package.util.dbhelpers as dbhelpers
import sys
from package.ui.mplwidget_ui import Ui_MplWidget

from PyQt5.QtCore import QMargins, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtChart import QBarCategoryAxis, QBarSeries, \
    QBarSet, QChart, QChartView
from PyQt5.QtWidgets import QApplication, QSizePolicy, QVBoxLayout, QWidget

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas

import random


class MplWidget(QWidget, Ui_MplWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.initialize_ui()

    def initialize_ui(self):
        # self.fig = Figure()
        # self.canvas = Canvas(self.fig)
        # self.ax = self.fig.add_subplot(111)  # Equivalent to 1, 1, 1

        # self.vbox = QVBoxLayout(self.plotwidget)
        # self.vbox.addWidget(self.canvas)
        self.chart_view = QChartView(self)
        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.chart_view)

    def plot(self):
        random.seed()
        data = [random.randint(0, 30) for i in range(20)]
        set0 = QBarSet('COVID Cases')

        for x in data:
            set0 << x

        series = QBarSeries()
        series.append(set0)

        chart = QChart(flags=Qt.Widget)
        chart.addSeries(series)
        chart.setTitle("Blacksburg COVID Cases")

        legend = chart.legend()
        legend.setAlignment(Qt.AlignBottom)

        # categories = list(str(range(25)))
        # axis = QBarCategoryAxis()
        # axis.append(categories)
        chart.createDefaultAxes()
        chart.axisX().setLabelsAngle(-90)
        chart.axisX().setTitleText('Date')
        # chart.setAxisX(axis, series)
        chart.axisY().setTitleText('Cases')
        chart.setMargins(QMargins(0, 0, 0, 0))
        # chart.layout().setContentsMargins(0, 0, 0, 0)

        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setChart(chart)



def update_chart(self, num_ticks=10):
    results = dbhelpers.get_results_database()
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

    self.fig.clear()
    self.fig.add_axes(xlabel='Date')
    ax = self.fig.add_subplot(111)
    ax.plot(dates_list, new_cases_list)
    ax.set_title('Number of New COVID-19 Cases in Blacksburg by Date')
    self.canvas.draw()

    return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mplwidget = MplWidget()
    mplwidget.plot()
    mplwidget.show()
    sys.exit(app.exec_())
