from mpython import *
import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.model_init(2)

while True:
    smart_camera.yolo_detect.recognize()
    class_id = smart_camera.yolo_detect.id
    if class_id != None:
        print(str('类别id：') + str(smart_camera.yolo_detect.id))
        print(str('类别名称：') + str(smart_camera.yolo_detect.category_list[smart_camera.yolo_detect.id]))
        print(str('置信度：') + str(smart_camera.yolo_detect.max_score))
