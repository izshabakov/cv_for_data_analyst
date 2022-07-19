import sqlite3

from PIL import ImageEnhance as Enhance
import numpy as np
from PIL import Image as Img
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
import cv2
import uispprbat
import uibdbat
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.image = 0
        # Данные нужны 11 лабы
        self.cv_image=0
        self.area_c=0
        self.bad_countours=0
        self.material_area = 0
        self.material_area_std = 0
        self.ui = uispprbat.Ui_MainWindow()
        self.ui.setupUi(self)
        self.table = Table()
        # Передача данных из emit() сигнала в функцию
        self.table.add_combo.connect(self.addComboBox)
        # Передача данных из emit() сигнала в функцию
        self.table.del_combo.connect(self.deleteFromComboBox)

        self.ui.pushButton_3.clicked.connect(self.get_table)
        self.ui.comboBox.activated[str].connect(self.findIdx_combobox)
        # Открыть через label
        self.ui.label_5.clicked.connect(self.picture_choose)
        self.ui.horizontalSlider.valueChanged.connect(self.set_transformed_frame)
        self.ui.horizontalSlider_2.valueChanged.connect(self.set_transformed_frame)
        self.ui.horizontalSlider_3.valueChanged.connect(self.set_transformed_frame)
        # Открыть через Open
        self.ui.actionOpen.triggered.connect(self.picture_choose_for_Open)

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
        img1 = np.array(img)
        img2= np.array(img)
        img = QImage(img1.data, img1.shape[1], img1.shape[0], QImage.Format_RGB888)
        self.ui.label_6.setPixmap(QPixmap.fromImage(img))

        self.cv_image, self.area_c, self.bad_countours = self.explore(img2)
        height, width, channel = self.cv_image.shape
        bytesPerLine = 3 * width
        qImg = QImage(self.cv_image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.ui.label_7.setPixmap(pixmap)
        area_c_check = ''
        if self.area_c < 0.1:
            area_c_check = 'в норме'
        else:
            area_c_check = 'все плохо'

        out = "Отчет:\nПористость: {}\nПористость: {}\nКоличество пор, площадь которых\nпревышает норму: {}".format(
            round(self.area_c, 2), area_c_check, self.bad_countours)
        print(out)
        self.ui.label_10.setText(out)

    def picture_choose_for_Open(self):
        path = QtWidgets.QFileDialog.getOpenFileName()[0]
        if path != '':
            pixmap = QPixmap(path)
            self.ui.label_5.setPixmap(pixmap)
            self.image = Img.open(path)



    def picture_choose(self, path):
        if path!='':
            pixmap = QPixmap(path)
            self.ui.label_5.setPixmap(pixmap)
            self.image = Img.open(path)

    def explore(self, image):
        image = np.copy(image)
        # дополнительная обработка шумов
        blured = cv2.GaussianBlur(image, (5, 5), 0)
        # конвертация BGR формата в формат HSV
        hsv = cv2.cvtColor(blured, cv2.COLOR_BGR2HSV)
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([120, 120, 120])
        # определяем маску для обнаружения контуров пор.
        # будут выделены поры в заданном диапозоне
        mask = cv2.inRange(hsv, lower_black, upper_black)
        # получаем массив конутров
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        good_contours = []
        bad_contours = []
        area_c = 0
        # находим поры, не превышающие нормативную площадь
        for contour in contours:
            # также подсчитываем общую площадь пор
            area_c += cv2.contourArea(contour)
            if self.material_area - self.material_area_std <= cv2.contourArea(contour) <= self.material_area + self.material_area_std:
                good_contours.append(contour)
            else:
                bad_contours.append(contour)
        area_c = area_c / (image.shape[0] * image.shape[1])
        # выделяем 'хорошие' поры зеленым цветом
        cv2.drawContours(image, good_contours, -1, (0, 255, 0), 3)
        # выделяем 'плохие' поры красным цветом
        cv2.drawContours(image, bad_contours, -1, (255, 0, 0), 3)
        return image, area_c, len(bad_contours)

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
        data = []
        idx = self.ui.comboBox.findText(combobox_entry)
        for i in range(2, self.table.ui.tableWidget.columnCount()):
            data.append(self.table.ui.tableWidget.item(idx, i).text())
        out = "Площадь поры: {}\nОткл: {}\nПористость: {}\nОткл: {}".format(data[0], data[1], data[2], data[3])
        print(out)
        self.ui.label_9.setText(out)
        #Данные нужны 11 лабы
        self.material_area = float(data[0])
        self.material_area_std = float(data[1])



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
