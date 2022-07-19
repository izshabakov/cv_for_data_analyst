import openpyxl

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self, excel_list):
        super().__init__()
        rows = len(excel_list)
        columns = 2
        self.checked_list = 0
        self.table = QTableWidget(rows, columns, self)

        for row in range(rows):
            widget = QWidget()
            checkbox = QCheckBox()
            checkbox.setCheckState(Qt.Unchecked)
            layoutH = QHBoxLayout(widget)
            layoutH.addWidget(checkbox)
            layoutH.setAlignment(Qt.AlignCenter)
            layoutH.setContentsMargins(0, 0, 0, 0)

            self.table.setCellWidget(row, 0, widget)
            self.table.setItem(row, 1, QTableWidgetItem(str(excel_list[row])))

        self.button1 = QPushButton("Сброс(будут обнаружены любые объекты)")
        self.button = QPushButton("Сохранить настройки ")
        self.button.clicked.connect(self.ButtonClicked)
        self.button1.clicked.connect(self.checkbox_restart)
        layoutV = QVBoxLayout(self)
        layoutV.addWidget(self.table)
        layoutV.addWidget(self.button)
        layoutV.addWidget(self.button1)

    def checkbox_restart(self):
        for i in range(self.table.rowCount()):
            self.table.cellWidget(i, 0).findChild(type(QCheckBox())).setChecked(False)

    def ButtonClicked(self):
        self.checked_list = [self.table.item(i, 1).text() for i in range(self.table.rowCount()) if
                             self.table.cellWidget(i, 0).findChild(type(QCheckBox())).isChecked()]
        print(self.checked_list)
        Window.close(self)
