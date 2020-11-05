#!/usr/bin/env python3

import sys
from package.ui.mplwidget_ui import Ui_MplWidget

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
        self.fig = Figure()
        self.canvas = Canvas(self.fig)
        # self.ax = self.fig.add_subplot(111)  # Equivalent to 1, 1, 1

        self.vbox = QVBoxLayout(self.plotwidget)
        self.vbox.addWidget(self.canvas)

        self.plot()

    def plot(self):
        random.seed()
        data = [random.random() for i in range(25)]
        ax = self.fig.add_subplot(111)
        self.fig.tight_layout()
        self.fig.subplots_adjust(top=0.90)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mplwidget = MplWidget()
    mplwidget.show()
    sys.exit(app.exec_())
