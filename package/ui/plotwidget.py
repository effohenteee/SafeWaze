
from package.ui.mplwidget import Ui_MplWidget as MplWidget

# *****************************************************************
import sys
import random
# *****************************************************************
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QSizePolicy, QWidget)
# *****************************************************************
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas


class PlotWidget(QWidget, MplWidget):
    def __init__(self):
        super(PlotWidget, self).__init__()
        self.initialize_ui()
        self.show()

    def initialize_ui(self):
        self.canvas = MplCanvas()


class MplCanvas(Canvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)  # Equivalent to 1, 1, 1

        Canvas.__init__(self, self.fig)
        self.setParent(self)

        Canvas.setSizePolicy(self, QSizePolicy.Expanding,
                             QSizePolicy.Expanding)
        Canvas.updateGeometry(self)
        self.plot()

    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = PlotWidget()
    sys.exit(app.exec_())
