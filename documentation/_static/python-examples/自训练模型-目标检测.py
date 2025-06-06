from mpython import *
import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.detect_kmodel_init('/data/detect.kmodel', 3)

import time
while True:
    smart_camera.detect_kmodel.recognize()
    _id = smart_camera.detect_kmodel.id
    if _id != None:
        _score = smart_camera.detect_kmodel.score
        if _score >= 0.6:
            print(str('分类id：') + str(_id))
            print(str('置信度：') + str(_score))
        else:
            print('未知分类')
    time.sleep(0.01)
