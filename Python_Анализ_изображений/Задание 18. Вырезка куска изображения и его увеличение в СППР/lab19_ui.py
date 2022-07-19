# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab19.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(509, 347)
        self.gray_checkbox = QtWidgets.QCheckBox(Form)
        self.gray_checkbox.setGeometry(QtCore.QRect(10, 10, 341, 23))
        self.gray_checkbox.setObjectName("gray_checkbox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.gray_checkbox.setText(_translate("Form", "Перевод изображения в оттенки серого"))

