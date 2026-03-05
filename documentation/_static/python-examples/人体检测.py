#mPythonType:0
from mpython import *

import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.model_init(6)
while True:
    smart_camera.person_detect.recognize()
    flag = smart_camera.person_detect.flag
    if flag:
        print(smart_camera.person_detect.person_num)
        print('已识别到人体')
