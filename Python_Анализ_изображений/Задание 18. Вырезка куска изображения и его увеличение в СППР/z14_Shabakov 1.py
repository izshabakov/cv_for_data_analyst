import imghdr
import os
import subprocess
import sys

import openpyxl
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import *
from PIL import Image
from pylab import *

import DetectObjects
import lab19_ui
import test


class Settings(QWidget):
    def __init__(self):
        super(Settings, self).__init__()
        self.ui = lab19_ui.Ui_Form()
        self.ui.setupUi(self)
        self.original_image=form.file_path
        self.buf_image='settings.jpg'

        self.ui.gray_checkbox.stateChanged.connect(self.gray)
        # form.file_path_signal.connect(self.gray)

    def gray(self):
        im = Image.open(form.file_path)
        if self.ui.gray_checkbox.isChecked():
            im1 = im.convert('L')
        else:
            im1 = im.convert('P')

        if im1.mode != 'RGB':
            im1 = im1.convert('RGB')

        im1.save(self.buf_image, quality=100)
        form.set_pixmap_label(self.buf_image)
        #img = QImage(im1.data, im1.shape[1], im1.shape[0], QImage.Format_RGB888)
        #form.ui.crapResult_label.setPixmap(QPixmap.fromImage(img))

class MainWindow(QMainWindow):
    # file_path_signal= QtCore.pyqtSignal(str)

    def __init__(self, t):
        super(MainWindow, self).__init__()
        self.ui = DetectObjects.Ui_MainWindow()
        self.ui.setupUi(self)
        # Обработка кнопок
        self.ui.openButton.clicked.connect(self.open_file)
        self.ui.sourceButton.clicked.connect(self.open_source)
        self.ui.startButton.clicked.connect(self.start_detection)
        self.ui.resButton.clicked.connect(self.open_result)
        self.ui.actionWebcam.triggered.connect(self.webcam)
        self.ui.actionwebcam_test.triggered.connect(self.webcam_test)
        self.ui.action_objectSet.triggered.connect(self.checkboxObj)
        self.ui.editPhotoButton.clicked.connect(self.crap)
        self.ui.original_photo.clicked.connect(self.back_original)
        self.ui.settings_button.clicked.connect(self.show_settings)
        # Путь к файлу
        self.file_path = 0
        # Массив обнаруженных объектов
        self.list = 0
        # Передаваемые параметры
        self.name = False
        self.prob = False
        self.minProb = 50
        self.fps = 20
        # Данная директория
        self.execution_path = os.getcwd()
        # Проверка файл на расширение(изображение/видео)
        self.file_check = 0
        self.save_dir = 'Results'

        self.pixmap = QtGui.QPixmap()
        self.original_photo = 0

    def show_settings(self):
        self.settings = Settings()
        self.settings.show()

    def set_pixmap_label(self, path):
        self.pixmap.load(path)
        scaled_pixmap = self.pixmap.scaled(self.ui.crapResult_label.width(), self.ui.crapResult_label.height())
        self.ui.crapResult_label.setPixmap(scaled_pixmap)

    def set_pixmap_from_img(self, img):
        self.pixmap.fromImage(img)
        scaled_pixmap = self.pixmap.scaled(self.ui.crapResult_label.width(), self.ui.crapResult_label.height())
        self.ui.crapResult_label.setPixmap(scaled_pixmap)

    def back_original(self):
        self.file_path = self.original_photo
        self.set_pixmap_label(self.file_path)

    def crap(self):
        im = Image.open(self.file_path)
        im_arr = array(im)
        fig = figure()
        imshow(im_arr)
        fig.show()

        x = ginput(2)
        im_crop = im.crop((x[0][0], x[0][1], x[1][0], x[1][1])).save('pillow_crop.jpg', quality=95)
        self.file_path = os.path.join(self.execution_path, 'pillow_crop.jpg')

        self.set_pixmap_label(self.file_path)

    def checkboxObj(self):
        t.show()

    # Функция вызова диалогового окна
    def open_file(self):
        path = \
            QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', None, "Image or Video (*.jpeg *.jpg *.avi *.mp4)")[
                0]
        if path != '':
            # Обнуление таблицы при загрузке нового файла
            self.ui.table.setRowCount(0)
            self.ui.resButton.setEnabled(False)
            self.file_path = path
            # Включение кнопок Исходный файл и Запуск
            self.ui.sourceButton.setEnabled(True)
            self.ui.startButton.setEnabled(True)
            self.check_image_or_video()
            # Если пользователь загрузил видео- включение редактора текста Количество кадров
            if self.file_check == 'Video':
                self.ui.fps_text.setEnabled(True)

                self.ui.editPhotoButton.setEnabled(False)
                self.ui.original_photo.setEnabled(False)
                self.ui.settings_button.setEnabled(False)
            else:
                self.ui.fps_text.setEnabled(False)
                self.ui.editPhotoButton.setEnabled(True)

                self.original_photo = self.file_path
                self.ui.original_photo.setEnabled(True)
                self.ui.settings_button.setEnabled(True)

                self.set_pixmap_label(self.file_path)
                # self.file_path_signal.emit(self.file_path)

    # Функция проверки типа файла
    def check_image_or_video(self):
        image_type = imghdr.what(self.file_path)
        if not image_type:
            self.file_check = 'Video'
        else:
            self.file_check = 'Image'

    # Функция запуска исходного файла
    def open_source(self):
        opener = "xdg-open"
        subprocess.call([opener, self.file_path])

    # Функция запуска полученного результата
    def open_result(self):
        opener = "xdg-open"
        if self.file_check == 'Image':
            subprocess.call([opener, os.path.join(self.execution_path, self.save_dir,
                                                  'result' + '[' + os.path.basename(self.file_path) + ']' + '.jpg')])

        if self.file_check == 'Video':
            subprocess.call([opener, os.path.join(self.execution_path, self.save_dir,
                                                  'result' + '[' + os.path.basename(self.file_path) + ']' + '.avi')])

    # Функция проверки флажков и редакторов текста
    def check_checkbox(self):
        if self.ui.name_checkBox.isChecked():
            self.name = True
        if self.ui.prob_checkBox.isChecked():
            self.prob = True
        if len(self.ui.minProb_text.toPlainText()) != 0:
            self.minProb = float(self.ui.minProb_text.toPlainText())
        if len(self.ui.fps_text.toPlainText()) != 0:
            self.fps = int(self.ui.fps_text.toPlainText())

    # Функция обработки обнаруженных объектов и их запись в таблицу(для фото)
    def from_list_to_table(self, frame_number=1):
        dct = {}
        for x in self.list:
            elem = x.get('name')
            if elem in dct:
                dct[elem] += 1
            else:
                dct[elem] = 1

        for item in dct.items():
            rowPosition = self.ui.table.rowCount()
            self.ui.table.insertRow(rowPosition)
            self.ui.table.setItem(rowPosition, 0, QTableWidgetItem(item[0]))
            self.ui.table.setItem(rowPosition, 1, QTableWidgetItem(str(item[1])))
            self.ui.table.setItem(rowPosition, 2, QTableWidgetItem(str(frame_number)))

        for item in dct.items():
            for i in range(len(t.all_list)):
                if item[0] == t.all_list[i]:
                    if t.table.cellWidget(i, 4).findChild(type(QCheckBox())).isChecked() \
                            and item[1] > int(t.table.cellWidget(i, 3).findChild(type(QTextEdit())).toPlainText()):
                        QSound.play('bzzz.wav')

    # Функция обработки обнаруженных объектов и их запись в таблицу(для видео)
    def forFrame(self, frame_number, output_array, output_count):
        print("FOR FRAME ", frame_number)
        print("Output for each object : ", output_array)
        print("Output count for unique objects : ", output_count)
        print("------------END OF A FRAME --------------")
        for item in output_count.items():
            rowPosition = self.ui.table.rowCount()
            self.ui.table.insertRow(rowPosition)
            self.ui.table.setItem(rowPosition, 0, QTableWidgetItem(item[0]))
            self.ui.table.setItem(rowPosition, 1, QTableWidgetItem(str(item[1])))
            self.ui.table.setItem(rowPosition, 2, QTableWidgetItem(str(frame_number)))

        for item in output_count.items():
            for i in range(len(t.all_list)):
                if item[0] == t.all_list[i]:
                    if t.table.cellWidget(i, 4).findChild(type(QCheckBox())).isChecked() \
                            and item[1] > int(t.table.cellWidget(i, 3).findChild(type(QTextEdit())).toPlainText()):
                        QSound.play('bzzz.wav')

    # Функция обработки файла
    def start_detection(self):
        self.ui.table.setRowCount(0)
        if not os.path.exists(os.path.join(self.execution_path, self.save_dir)):
            os.mkdir(os.path.join(self.execution_path, self.save_dir))
        self.check_checkbox()
        from imageai.Detection import VideoObjectDetection, ObjectDetection
        if self.file_check == 'Video':
            detector = VideoObjectDetection()
            detector.setModelTypeAsYOLOv3()
            detector.setModelPath("yolo.h5")
            detector.loadModel(detection_speed='flash')
            custom = detector.CustomObjects()
            if t.checked_list:
                for i in t.checked_list:
                    custom[i] = 'valid'
            else:
                for key in custom:
                    custom[key] = 'valid'
            self.list = detector.detectObjectsFromVideo(custom_objects=custom, input_file_path=self.file_path,
                                                        output_file_path=os.path.join(self.execution_path,
                                                                                      self.save_dir,
                                                                                      'result' + '[' + os.path.basename(
                                                                                          self.file_path) + ']'),
                                                        display_object_name=self.name,
                                                        display_percentage_probability=self.prob,
                                                        minimum_percentage_probability=self.minProb,
                                                        frames_per_second=self.fps,
                                                        log_progress=True, per_frame_function=self.forFrame,
                                                        detection_timeout=1)
            # Включение кнопки Результат
            self.ui.resButton.setEnabled(True)

        if self.file_check == 'Image':
            detector = ObjectDetection()
            detector.setModelTypeAsYOLOv3()
            detector.setModelPath("yolo.h5")
            detector.loadModel(detection_speed='flash')
            custom = detector.CustomObjects()
            print(t.checked_list)
            if t.checked_list:
                for i in t.checked_list:
                    custom[i] = 'valid'
            else:
                for key in custom:
                    custom[key] = 'valid'
                print(custom)
            self.list = detector.detectObjectsFromImage(custom_objects=custom, input_image=self.file_path,
                                                        output_image_path=os.path.join(self.execution_path,
                                                                                       self.save_dir,
                                                                                       'result' + '[' + os.path.basename(
                                                                                           self.file_path) + ']' + '.jpg'),
                                                        minimum_percentage_probability=self.minProb,
                                                        display_percentage_probability=self.prob,
                                                        display_object_name=self.name)
            # Включение кнопки Результат
            self.ui.resButton.setEnabled(True)
            self.from_list_to_table()

    def webcam(self):
        from imageai.Detection import ObjectDetection
        import cv2

        detector = ObjectDetection()
        detector.setModelTypeAsYOLOv3()
        detector.setModelPath('yolo.h5')
        detector.loadModel(detection_speed='flash')

        camera = cv2.VideoCapture(0)
        camera.set(cv2.CAP_PROP_FPS, 30)
        frame_counter = 1
        self.ui.table.setRowCount(0)
        while camera.isOpened():
            ret, frame = camera.read()
            if ret:
                returned_image, self.list = detector.detectObjectsFromImage(input_image=frame, input_type='array',
                                                                            output_type='array')
                self.from_list_to_table(frame_counter)
                frame_counter += 1
                cv2.imshow('Frame', returned_image)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        camera.release()
        cv2.destroyAllWindows()

    def webcam_test(self):
        from imageai.Detection import VideoObjectDetection
        import cv2

        camera = cv2.VideoCapture(0)
        camera.set(cv2.CAP_PROP_FPS, 30)

        self.ui.resButton.setEnabled(False)
        self.ui.sourceButton.setEnabled(False)

        detector = VideoObjectDetection()
        detector.setModelTypeAsYOLOv3()
        detector.setModelPath("yolo.h5")
        detector.loadModel(detection_speed='flash')
        detector.detectObjectsFromVideo(camera_input=camera,
                                        output_file_path='camera_detected_video', frames_per_second=20.0,
                                        log_progress=True,
                                        return_detected_frame=True)


if __name__ == '__main__':
    book = openpyxl.open('test.xlsx', read_only=True)
    sheet = book.active
    excel_list = [sheet[i][0].value for i in range(1, sheet.max_row + 1)]
    excel_list2 = [sheet[i][1].value for i in range(1, sheet.max_row + 1)]
    d = dict(zip(excel_list, excel_list2))

    app = QApplication(sys.argv)
    t = test.Window(d)
    t.resize(700, 300)
    form = MainWindow(t)
    form.show()
    app.exec()
