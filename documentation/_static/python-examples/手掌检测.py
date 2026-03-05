#mPythonType:0
from mpython import *

import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.model_init(3)
while True:
    smart_camera.hand_detect.recognize()
    if smart_camera.hand_detect.flag:
        print('已识别到')
        print(str('手掌数量：') + str(smart_camera.hand_detect.hand_num))
