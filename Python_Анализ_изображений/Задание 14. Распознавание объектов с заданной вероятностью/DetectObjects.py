# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DetectObjects.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 446)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(350, 240, 111, 28))
        self.openButton.setObjectName("openButton")
        self.resButton = QtWidgets.QPushButton(self.centralwidget)
        self.resButton.setEnabled(False)
        self.resButton.setGeometry(QtCore.QRect(350, 280, 111, 28))
        self.resButton.setObjectName("resButton")
        self.optionBox = QtWidgets.QGroupBox(self.centralwidget)
        self.optionBox.setGeometry(QtCore.QRect(310, 30, 271, 171))
        self.optionBox.setObjectName("optionBox")
        self.name_checkBox = QtWidgets.QCheckBox(self.optionBox)
        self.name_checkBox.setGeometry(QtCore.QRect(20, 20, 221, 20))
        self.name_checkBox.setObjectName("name_checkBox")
        self.prob_checkBox = QtWidgets.QCheckBox(self.optionBox)
        self.prob_checkBox.setGeometry(QtCore.QRect(20, 50, 241, 20))
        self.prob_checkBox.setObjectName("prob_checkBox")
        self.minProb_text = QtWidgets.QTextEdit(self.optionBox)
        self.minProb_text.setGeometry(QtCore.QRect(20, 80, 41, 31))
        self.minProb_text.setObjectName("minProb_text")
        self.label = QtWidgets.QLabel(self.optionBox)
        self.label.setGeometry(QtCore.QRect(70, 80, 151, 16))
        self.label.setObjectName("label")
        self.fps_text = QtWidgets.QTextEdit(self.optionBox)
        self.fps_text.setEnabled(False)
        self.fps_text.setGeometry(QtCore.QRect(20, 120, 41, 31))
        self.fps_text.setObjectName("fps_text")
        self.label_2 = QtWidgets.QLabel(self.optionBox)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 201, 16))
        self.label_2.setObjectName("label_2")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 10, 261, 192))
        self.table.setObjectName("table")
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.sourceButton = QtWidgets.QPushButton(self.centralwidget)
        self.sourceButton.setEnabled(False)
        self.sourceButton.setGeometry(QtCore.QRect(350, 320, 111, 28))
        self.sourceButton.setObjectName("sourceButton")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setEnabled(False)
        self.startButton.setGeometry(QtCore.QRect(480, 240, 93, 28))
        self.startButton.setObjectName("startButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 26))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openButton.setText(_translate("MainWindow", "Загрузить файл"))
        self.resButton.setText(_translate("MainWindow", "Результат"))
        self.optionBox.setTitle(_translate("MainWindow", "Опции:"))
        self.name_checkBox.setText(_translate("MainWindow", "Отобразить названия объектов"))
        self.prob_checkBox.setText(_translate("MainWindow", "Отобразить точность"))
        self.label.setText(_translate("MainWindow", "Минимальная точность"))
        self.label_2.setText(_translate("MainWindow", "Кадров в секунду(только видео)"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Объекты"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Количество"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Номер кадра"))
        self.sourceButton.setText(_translate("MainWindow", "Исходный файл"))
        self.startButton.setText(_translate("MainWindow", "Запуск"))
        self.menuExit.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
