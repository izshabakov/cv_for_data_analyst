from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self, excel_list):
        super().__init__()
        self.excel_list = excel_list
        rows = len(excel_list)
        columns = 5
        self.all_list=list(excel_list.values())
        print(self.all_list)
        self.checked_list = 0
        self.table = QTableWidget(rows, columns, self)
        self.table.setHorizontalHeaderLabels(['', 'Поиск', 'Условие', 'Количество', 'Правило'])
        row = 0

        for key in excel_list:
            print(row)
            widget = QWidget()
            checkbox = QCheckBox()
            checkbox.setCheckState(Qt.Unchecked)
            layoutH = QHBoxLayout(widget)
            layoutH.addWidget(checkbox)
            layoutH.setAlignment(Qt.AlignCenter)
            layoutH.setContentsMargins(0, 0, 0, 0)

            combo_widget = QWidget()
            combo_box = QComboBox()
            layoutY = QHBoxLayout(combo_widget)
            layoutY.addWidget(combo_box)
            layoutY.setAlignment(Qt.AlignCenter)
            layoutY.setContentsMargins(0, 0, 0, 0)

            widget2 = QWidget()
            checkbox2 = QCheckBox()
            checkbox2.setCheckState(Qt.Unchecked)
            layoutZ = QHBoxLayout(widget2)
            layoutZ.addWidget(checkbox2)
            layoutZ.setAlignment(Qt.AlignCenter)
            layoutZ.setContentsMargins(0, 0, 0, 0)

            widget3 = QWidget()
            text_edit = QTextEdit()
            layoutX = QHBoxLayout(widget3)
            layoutX.addWidget(text_edit)
            layoutX.setAlignment(Qt.AlignCenter)
            layoutX.setContentsMargins(0, 0, 0, 0)

            self.table.setCellWidget(row, 0, widget)
            self.table.setItem(row, 1, QTableWidgetItem(str(key)))
            self.table.setCellWidget(row, 2, combo_widget)
            self.table.setCellWidget(row, 3, widget3)
            self.table.setCellWidget(row, 4, widget2)

            self.table.cellWidget(row, 2).findChild(type(QComboBox())).addItem('>')
            self.table.cellWidget(row, 2).findChild(type(QComboBox())).addItem('=')
            row += 1

        self.button1 = QPushButton("Сброс(будут обнаружены любые объекты)")
        self.button = QPushButton("Сохранить настройки ")
        self.button.clicked.connect(self.ButtonClicked)
        self.button1.clicked.connect(self.checkbox_restart)
        layoutV = QVBoxLayout(self)
        layoutV.addWidget(self.table)
        layoutV.addWidget(self.button)
        layoutV.addWidget(self.button1)

    def checkbox_restart(self):
        QSound.play('bzzz.wav')
        print(self.table.cellWidget(0, 4).findChild(type(QCheckBox())).isChecked())
        print(self.table.cellWidget(0, 3).findChild(type(QTextEdit())).toPlainText())
        if self.table.cellWidget(0, 2).findChild(type(QComboBox())).currentText() == '>':
            print('чек')
        for i in range(self.table.rowCount()):
            self.table.cellWidget(i, 0).findChild(type(QCheckBox())).setChecked(False)

    def ButtonClicked(self):
        self.checked_list = [self.excel_list[self.table.item(i, 1).text()] for i in range(self.table.rowCount()) if
                             self.table.cellWidget(i, 0).findChild(type(QCheckBox())).isChecked()]
        print(self.checked_list)
        Window.close(self)
#        self.checked_list = [self.table.item(i, 1).text() for i in range(self.table.rowCount()) if
# self.table.cellWidget(i, 0).findChild(type(QCheckBox())).isChecked()]
