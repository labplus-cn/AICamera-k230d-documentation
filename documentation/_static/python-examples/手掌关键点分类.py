#mPythonType:0
from mpython import *
import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.model_init(4)

while True:
    smart_camera.hand_keypoint_class.recognize()
    if smart_camera.hand_keypoint_class.gesture_id != None:
        print(str('手势id：') + str(smart_camera.hand_keypoint_class.gesture_id))
        print(str('手势字符串：') + str(smart_camera.hand_keypoint_class.gesture_str))
