import sqlite3

from PIL import ImageEnhance as Enhance
import numpy as np
from PIL import Image as Img
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
import uispprbat
import uibdbat
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.path = 0
        self.image = 0
        self.ui = uispprbat.Ui_MainWindow()
        self.ui.setupUi(self)
        self.table = Table()
        # Передача данных из emit() сигнала в функцию
        self.table.add_combo.connect(self.addComboBox)
        # Передача данных из emit() сигнала в функцию
        self.table.del_combo.connect(self.deleteFromComboBox)

        self.ui.pushButton_3.clicked.connect(self.get_table)
        self.ui.comboBox.activated[str].connect(self.findIdx_combobox)

        self.ui.label_5.clicked.connect(self.picture_choose)
        self.ui.horizontalSlider.valueChanged.connect(self.set_transformed_frame)
        self.ui.horizontalSlider_2.valueChanged.connect(self.set_transformed_frame)
        self.ui.horizontalSlider_3.valueChanged.connect(self.set_transformed_frame)

        # Массив полученных данных из БД
        self.records = []
        # Чтение данных из БД
        self.read_sqlite_table()
        if len(self.records) != 0:
            rows = len(self.records)
            columns = len(self.records[0])
            # Вставка данных из БД в QTableWidgets
            self.tab(columns, rows, self.records)

    def set_transformed_frame(self):
        img = self.image
        img = Enhance.Contrast(img).enhance(self.ui.horizontalSlider.value() / 10)
        img = Enhance.Brightness(img).enhance(self.ui.horizontalSlider_2.value() / 10)
        img = Enhance.Sharpness(img).enhance(self.ui.horizontalSlider_3.value())
        img = np.array(img)
        img = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
        self.ui.label_6.setPixmap(QPixmap.fromImage(img))

    def picture_choose(self, path):
        self.path = path
        pixmap = QPixmap(path)
        self.ui.label_5.setPixmap(pixmap)
        self.image = Img.open(path)

    # Первые две функции связаны с получением индекса добавленного/удаленного элемента из окна Table для последующей
    # манипуляции с ComboBox(добавить/удалить элемент)
    def addComboBox(self, name):
        self.ui.comboBox.addItem(name)

    def deleteFromComboBox(self, index_combobox):
        self.ui.comboBox.removeItem(index_combobox)

    # Функция вызова окна с Таблицей
    def get_table(self):
        self.table.show()

    # Функция чтения из БД
    def read_sqlite_table(self):
        try:
            conn = sqlite3.connect("dbname2.db")
            cursor = conn.cursor()

            query = """SELECT * from Materials"""
            cursor.execute(query)
            self.records = cursor.fetchall()
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

    # Функция вставки в QTableWidgets
    def tab(self, columns, rows, results):
        self.table.ui.tableWidget.setRowCount(rows)
        self.table.ui.tableWidget.setColumnCount(columns)
        for i in range(rows):
            # Вставка названия материала в ComboBox
            self.ui.comboBox.addItem(results[i][1])
            for j in range(columns):
                item = QTableWidgetItem("{}".format(results[i][j]))
                item.setTextAlignment(Qt.AlignHCenter)
                self.table.ui.tableWidget.setItem(i, j, item)

    # Получение индекса из combobox'а и вывод данных в TextEdit главной формы при нажатии на элемент ComboBox'а
    def findIdx_combobox(self, combobox_entry):
        idx = self.ui.comboBox.findText(combobox_entry)
        data = []
        for i in range(2, self.table.ui.tableWidget.columnCount()):
            data.append(self.table.ui.tableWidget.item(idx, i).text())
        out = "Площадь поры: {}\nОткл: {}\nПористость: {}\nОткл: {}".format(data[0], data[1], data[2], data[3])
        print(out)
        self.ui.textEdit_2.setText(out)


class Table(QWidget):
    # Создал сигнал
    add_combo = QtCore.pyqtSignal(str)
    del_combo = QtCore.pyqtSignal(int)

    def __init__(self):
        super(Table, self).__init__()
        self.ui = uibdbat.Ui_Form()
        self.ui.setupUi(self)
        # Внутри метода активация сигнала через emit(передача id)
        self.ui.pushButton.clicked.connect(self.addButton)
        # Внутри метода активация сигнала через emit(передача id)
        self.ui.pushButton_2.clicked.connect(self.delButton)
        self.ui.pushButton_3.clicked.connect(self.close)

    def addButton(self):
        material_name = self.ui.textEdit.toPlainText()
        material_area = self.ui.textEdit_2.toPlainText()
        material_area_std = self.ui.textEdit_3.toPlainText()
        material_porous = self.ui.textEdit_4.toPlainText()
        material_porous_std = self.ui.textEdit_5.toPlainText()
        data = [material_name, material_area, material_area_std, material_porous, material_porous_std]
        flag = [True if (m is not None and m != '') else False for m in data]
        if flag:
            try:
                material_area = float(material_area)
                material_area_std = float(material_area_std)
                material_porous = float(material_porous)
                material_porous_std = float(material_porous_std)
                conn = sqlite3.connect("dbname2.db")
                crsr = conn.cursor()
                crsr.execute("""INSERT INTO Materials(NAME, PORE_AREA_MEAN, PORE_AREA_STD, POROUS_MEAN, POROUS_STD) 
                        VALUES (?,?,?,?,?)""",
                             (material_name, material_area, material_area_std, material_porous, material_porous_std))
                # Получение row_id из БД для вставки в таблицу значения ID
                id_table = str(crsr.lastrowid)
                conn.commit()
                conn.close()

                # Добавление новой строки в таблицу
                rowPosition = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(rowPosition)

                # Вставка id в data
                data = [id_table] + data
                print(data[0])
                # Вставка в таблицу
                for i in range(6):
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(data[i])
                    item.setTextAlignment(Qt.AlignHCenter)
                    self.ui.tableWidget.setItem(rowPosition, i, item)

                # Активация сигнала(передача material_name)
                self.add_combo.emit(material_name)
            except Exception as e:
                print(e)

    def delButton(self):
        try:
            index = self.ui.textEdit_6.toPlainText()
            index = int(index) - 1
            id = self.ui.tableWidget.item(index, 0).text()
            print(id)
            print(type(id))
            self.ui.tableWidget.removeRow(index)
            # Активация сигнала(передача index)
            self.del_combo.emit(int(index))
            ####РАБОТА С БД
            connect = sqlite3.connect("dbname2.db")
            crsr = connect.cursor()
            crsr.execute('DELETE FROM Materials WHERE ID=?', (id,))
            connect.commit()
            connect.close()
        except Exception as e:
            print(e)
        # rowc = self.ui.tableWidget.rowCount()
        # id = self.ui.tableWidget.takeItem()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec()
