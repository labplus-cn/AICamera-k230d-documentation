#mPythonType:0
from mpython import *

import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.color_obj_count_init(0)

while True:
    smart_camera.color_obj_count.recognize()
    count = smart_camera.color_obj_count.color_count
    if count != None:
        print(str('色块数量：') + str(count))
