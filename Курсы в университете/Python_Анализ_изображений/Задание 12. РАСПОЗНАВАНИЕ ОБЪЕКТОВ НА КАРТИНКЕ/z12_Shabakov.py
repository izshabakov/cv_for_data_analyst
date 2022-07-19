from imageai.Detection import ObjectDetection

import os

exec_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.1.0.h5")
detector.loadModel()

list = detector.detectObjectsFromImage(input_image="objects.jpg",
                                    output_image_path ="new_objects.jpg",
                                    minimum_percentage_probability=30,
                                    display_percentage_probability=False,
                                    display_object_name=False)

