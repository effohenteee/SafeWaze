# This Python file uses the following encoding: utf-8
#!/usr/bin/env python

import os
import sys
import urllib, json
import PySide2.QtQml
from OpenGL import GL
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QAbstractListModel, Qt, QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtCore import *
from PySide2.QtGui import *
from PyQt5.QtWidgets import *

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

def display():
    engine.load(QUrl.fromLocalFile('main.qml'))

if __name__ == "__main__":
    print("Hello")
    app = QApplication(sys.argv)

    # Create the QML user interface.
#    view = QDeclarativeView()
#    view.setSource(QUrl('main.qml'))
#    view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
#    view.setGeometry(100, 100, 400, 240)
#    view.show()

#    app.exec_()

    engine = QQmlApplicationEngine()
    #engine.rootContext().setContextProperty("backend", backend)
    #engine.load(QUrl.fromLocalFile('main.qml'))
    display()

    app.exec_()
#     pass
