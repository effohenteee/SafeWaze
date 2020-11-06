# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(800, 600)
        Dashboard.setMinimumSize(QtCore.QSize(800, 600))
        Dashboard.setStyleSheet("#centralwidget {background-color: rgb(131,34,65);}")
        self.centralwidget = QtWidgets.QWidget(Dashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.vbox_tabs = QtWidgets.QVBoxLayout()
        self.vbox_tabs.setObjectName("vbox_tabs")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.vbox_tab_1 = QtWidgets.QVBoxLayout()
        self.vbox_tab_1.setObjectName("vbox_tab_1")
        self.hbox_info = QtWidgets.QHBoxLayout()
        self.hbox_info.setSpacing(6)
        self.hbox_info.setObjectName("hbox_info")
        self.widget_left = QtWidgets.QWidget(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_left.sizePolicy().hasHeightForWidth())
        self.widget_left.setSizePolicy(sizePolicy)
        self.widget_left.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_left.setMaximumSize(QtCore.QSize(16777215, 360))
        self.widget_left.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.widget_left.setObjectName("widget_left")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_left)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.risk_barometer = QtWidgets.QProgressBar(self.widget_left)
        self.risk_barometer.setStyleSheet("QProgressBar {\n"
"border-image: url(:/Gauge/Resources/Risk-Gradient/V2/gradient-v2-600x600.png);\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 0 #fff\n"
"stop: 0.4999 #eee\n"
"stop: 0.5 #ddd,\n"
"stop: 1 #eee);\n"
"}")
        self.risk_barometer.setProperty("value", 20)
        self.risk_barometer.setTextVisible(False)
        self.risk_barometer.setOrientation(QtCore.Qt.Vertical)
        self.risk_barometer.setInvertedAppearance(True)
        self.risk_barometer.setObjectName("risk_barometer")
        self.horizontalLayout_4.addWidget(self.risk_barometer)
        self.lcdNumber_risk = QtWidgets.QLCDNumber(self.widget_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_risk.sizePolicy().hasHeightForWidth())
        self.lcdNumber_risk.setSizePolicy(sizePolicy)
        self.lcdNumber_risk.setMinimumSize(QtCore.QSize(60, 0))
        self.lcdNumber_risk.setDigitCount(3)
        self.lcdNumber_risk.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_risk.setProperty("intValue", 100)
        self.lcdNumber_risk.setObjectName("lcdNumber_risk")
        self.horizontalLayout_4.addWidget(self.lcdNumber_risk)
        self.vbox_risk_factors = QtWidgets.QVBoxLayout()
        self.vbox_risk_factors.setObjectName("vbox_risk_factors")
        self.label = QtWidgets.QLabel(self.widget_left)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.vbox_risk_factors.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.widget_left)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.vbox_risk_factors.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget_left)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.vbox_risk_factors.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget_left)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.vbox_risk_factors.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget_left)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.vbox_risk_factors.addWidget(self.label_7)
        self.horizontalLayout_4.addLayout(self.vbox_risk_factors)
        self.hbox_info.addWidget(self.widget_left)
        self.widget_right = QtWidgets.QWidget(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_right.sizePolicy().hasHeightForWidth())
        self.widget_right.setSizePolicy(sizePolicy)
        self.widget_right.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_right.setMaximumSize(QtCore.QSize(16777215, 360))
        self.widget_right.setStyleSheet("background-color: rgb(173, 127, 168);")
        self.widget_right.setObjectName("widget_right")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_right)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_right)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.hbox_info.addWidget(self.widget_right)
        self.vbox_tab_1.addLayout(self.hbox_info)
        self.frame_graph = QtWidgets.QFrame(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_graph.sizePolicy().hasHeightForWidth())
        self.frame_graph.setSizePolicy(sizePolicy)
        self.frame_graph.setMinimumSize(QtCore.QSize(758, 325))
        self.frame_graph.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.frame_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph.setObjectName("frame_graph")
        self.vbox_tab_1.addWidget(self.frame_graph)
        self.verticalLayout_6.addLayout(self.vbox_tab_1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.vbox_tabs.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.vbox_tabs, 0, 0, 1, 1)
        Dashboard.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dashboard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        Dashboard.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dashboard)
        self.statusbar.setObjectName("statusbar")
        Dashboard.setStatusBar(self.statusbar)

        self.retranslateUi(Dashboard)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)

    def retranslateUi(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Dashboard.setWindowTitle(_translate("Dashboard", "SafeWaze Dashboard"))
        self.label.setText(_translate("Dashboard", "Risk Factor"))
        self.label_4.setText(_translate("Dashboard", "Risk Factor"))
        self.label_5.setText(_translate("Dashboard", "Risk Factor"))
        self.label_6.setText(_translate("Dashboard", "Risk Factor"))
        self.label_7.setText(_translate("Dashboard", "Risk Factor"))
        self.label_2.setText(_translate("Dashboard", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Dashboard", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dashboard", "Tab 2"))
import package.ui.resources_rc