from imageai.Detection import VideoObjectDetection

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")
detector.loadModel()

list = detector.detectObjectsFromVideo(input_file_path="traffic.mp4",
                                       output_file_path="traffic_result.mp4",
                                       frames_per_second=20,
                                       log_progress=True)
print(list)

