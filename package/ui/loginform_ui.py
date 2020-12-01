# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/loginform.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        LoginWidget.setObjectName("LoginWidget")
        LoginWidget.setEnabled(True)
        LoginWidget.resize(480, 640)
        LoginWidget.setMinimumSize(QtCore.QSize(480, 640))
        LoginWidget.setMaximumSize(QtCore.QSize(480, 640))
        LoginWidget.setStyleSheet("QWidget#LoginWidget {\n"
"background-image: url(:/Wallpaper/Resources/Wallpapers/Login/login-gradient-alpha-100-480x640.png);\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color: rgba(255, 255, 255, 25%);\n"
"}\n"
"\n"
"QPushButton#button_sign_up,#button_sign_in {\n"
"color: rgb(134, 31, 65);\n"
"border: 0px;\n"
"background: transparent;\n"
"}\n"
"\n"
"QPushButton.pressed {\n"
"background: transparent;\n"
"}")
        self.lineEdit_email = QtWidgets.QLineEdit(LoginWidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(90, 320, 300, 25))
        self.lineEdit_email.setClearButtonEnabled(True)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_password = QtWidgets.QLineEdit(LoginWidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(90, 380, 300, 25))
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setClearButtonEnabled(True)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_logo = QtWidgets.QLabel(LoginWidget)
        self.label_logo.setGeometry(QtCore.QRect(30, 120, 420, 105))
        self.label_logo.setStyleSheet("image: url(:/Logo/Resources/Logo/SafeWaze-Logo-420x105.png);")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayoutWidget = QtWidgets.QWidget(LoginWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 510, 261, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.h_box = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.h_box.setContentsMargins(0, 0, 0, 0)
        self.h_box.setSpacing(10)
        self.h_box.setObjectName("h_box")
        self.label_sign_up = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_sign_up.setStyleSheet("font: italic 12pt \"Ubuntu\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgba(255, 255, 255, 150);")
        self.label_sign_up.setObjectName("label_sign_up")
        self.h_box.addWidget(self.label_sign_up)
        self.button_sign_up = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_sign_up.setFont(font)
        self.button_sign_up.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_sign_up.setFlat(False)
        self.button_sign_up.setObjectName("button_sign_up")
        self.h_box.addWidget(self.button_sign_up)
        self.button_sign_in = QtWidgets.QPushButton(LoginWidget)
        self.button_sign_in.setGeometry(QtCore.QRect(170, 440, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_sign_in.setFont(font)
        self.button_sign_in.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_sign_in.setDefault(True)
        self.button_sign_in.setFlat(True)
        self.button_sign_in.setObjectName("button_sign_in")

        self.retranslateUi(LoginWidget)
        QtCore.QMetaObject.connectSlotsByName(LoginWidget)
        LoginWidget.setTabOrder(self.lineEdit_email, self.lineEdit_password)
        LoginWidget.setTabOrder(self.lineEdit_password, self.button_sign_in)
        LoginWidget.setTabOrder(self.button_sign_in, self.button_sign_up)

    def retranslateUi(self, LoginWidget):
        _translate = QtCore.QCoreApplication.translate
        LoginWidget.setWindowTitle(_translate("LoginWidget", "SafeWaze Login"))
        self.lineEdit_email.setPlaceholderText(_translate("LoginWidget", "Email address"))
        self.lineEdit_password.setPlaceholderText(_translate("LoginWidget", "Password"))
        self.label_sign_up.setText(_translate("LoginWidget", "Don\'t have an account?"))
        self.button_sign_up.setText(_translate("LoginWidget", "SIGN UP"))
        self.button_sign_in.setText(_translate("LoginWidget", "LOG IN"))
import package.ui.resources_rc