# 动态手势识别
from mpython import *
import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)
smart_camera.model_init(25)

while True:
    smart_camera.dynamic_gesture.recognize()
    if(smart_camera.dynamic_gesture.gesture_id):
        print(str('手势id:') + str(smart_camera.dynamic_gesture.gesture_id))
        print(str('手势字符串:') + str(smart_camera.dynamic_gesture.gesture_str))




