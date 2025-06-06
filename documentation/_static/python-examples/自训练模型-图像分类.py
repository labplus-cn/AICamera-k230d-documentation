from mpython import *
import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.classify_kmodel_init('/sdcard/xxx.kmodel', 3)

while True:
    smart_camera.classify_model.recognize()
    classify_id = smart_camera.classify_model.id
    if classify_id != None:
        print(str('分类模型id：') + str(classify_id))
        print(str('置信度：') + str(smart_camera.classify_model.score))
