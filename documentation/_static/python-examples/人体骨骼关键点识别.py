#mPythonType:0
from mpython import *

import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.model_init(10)
while True:
    smart_camera.person_keypoint_detect.recognize()
    if len(smart_camera.person_keypoint_detect.keypoints) != 0:
        print(str('骨骼关键点数据') + str(smart_camera.person_keypoint_detect.keypoints))
