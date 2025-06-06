#mPythonType:0
from mpython import *
import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.model_init(11)

while True:
    smart_camera.person_keypoint_detect_plus.recognize()
    person_keypoint = smart_camera.person_keypoint_detect_plus.id
    if person_keypoint != None:
        print(str('姿态识别id：') + str(person_keypoint))
