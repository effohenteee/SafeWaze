# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/matplotlib_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MplWidget(object):
    def setupUi(self, MplWidget):
        MplWidget.setObjectName("MplWidget")
        MplWidget.resize(790, 617)
        self.plotwidget = QtWidgets.QWidget(MplWidget)
        self.plotwidget.setGeometry(QtCore.QRect(9, 9, 772, 521))
        self.plotwidget.setObjectName("plotwidget")
        # self.pushButton = QtWidgets.QPushButton(MplWidget)
        # self.pushButton.setGeometry(QtCore.QRect(690, 560, 89, 25))
        # self.pushButton.setObjectName("pushButton")

        self.retranslateUi(MplWidget)
        QtCore.QMetaObject.connectSlotsByName(MplWidget)

    def retranslateUi(self, MplWidget):
        _translate = QtCore.QCoreApplication.translate
        MplWidget.setWindowTitle(_translate("MplWidget", "Form"))
        # self.pushButton.setText(_translate("MplWidget", "PushButton"))
