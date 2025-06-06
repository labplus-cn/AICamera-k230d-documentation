#mPythonType:0
from mpython import *

import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.model_init(27)

while True:
    smart_camera.face_living_body.recognize()
    print(str('眨眼次数：') + str(smart_camera.face_living_body.mouth_blink_counter[0]))
    print(str('张嘴次数：') + str(smart_camera.face_living_body.mouth_blink_counter[1]))
