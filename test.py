# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(800, 600)
        self.lineEdit = QLineEdit(main)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 60, 113, 25))
        self.browser = QWebEngineView(main)
        self.browser.setObjectName(u"browser")
        self.browser.setGeometry(QRect(259, 149, 211, 191))
        self.browser.load(QUrl("https://www.vt.edu"))

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
    # retranslateUi

