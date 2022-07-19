import os
import imghdr
from PyQt5 import QtCore, QtWidgets
import DetectObjects
import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
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
            else:
                self.ui.fps_text.setEnabled(False)

    # Функция проверки типа файла
    def check_image_or_video(self):
        image_type = imghdr.what(self.file_path)
        if not image_type:
            self.file_check = 'Video'
        else:
            self.file_check = 'Image'

    # Функция запуска исходного файла
    def open_source(self):
        os.startfile(self.file_path)

    # Функция запуска полученного результата
    def open_result(self):
        if self.file_check == 'Image':
            os.startfile(os.path.join(self.execution_path, self.save_dir,
                                      'result' + '[' + os.path.basename(self.file_path) + ']' + '.jpg'))
        if self.file_check == 'Video':
            os.startfile(os.path.join(self.execution_path, self.save_dir,
                                      'result' + '[' + os.path.basename(self.file_path) + ']' + '.avi'))

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

    # Функция обработки файла
    def start_detection(self):
        if not os.path.exists(os.path.join(self.execution_path, self.save_dir)):
            os.mkdir(os.path.join(self.execution_path, self.save_dir))
        self.check_checkbox()
        from imageai.Detection import VideoObjectDetection, ObjectDetection
        if self.file_check == 'Video':
            detector = VideoObjectDetection()
            detector.setModelTypeAsYOLOv3()
            detector.setModelPath("yolo.h5")
            detector.loadModel(detection_speed='flash')
            self.list = detector.detectObjectsFromVideo(input_file_path=self.file_path,
                                                        output_file_path=os.path.join(self.execution_path,
                                                                                      self.save_dir,
                                                                                      'result' + '[' + os.path.basename(
                                                                                          self.file_path) + ']'),
                                                        display_object_name=self.name,
                                                        display_percentage_probability=self.prob,
                                                        minimum_percentage_probability=self.minProb,
                                                        frames_per_second=self.fps,
                                                        log_progress=True, per_frame_function=self.forFrame)
            # Включение кнопки Результат
            self.ui.resButton.setEnabled(True)

        if self.file_check == 'Image':
            detector = ObjectDetection()
            detector.setModelTypeAsRetinaNet()
            detector.setModelPath("resnet50_coco_best_v2.1.0.h5")
            detector.loadModel(detection_speed='flash')
            self.list = detector.detectObjectsFromImage(input_image=self.file_path,
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

        detector = VideoObjectDetection()
        detector.setModelTypeAsYOLOv3()
        detector.setModelPath("yolo.h5")
        detector.loadModel(detection_speed='flash')
        detector.detectObjectsFromVideo(camera_input=camera,
                                       output_file_path='camera_detected_video', frames_per_second=20.0, log_progress=True,
                                       return_detected_frame=True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec()
