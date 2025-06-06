#mPythonType:0
from mpython import *
import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.model_init(23)

while True:
    smart_camera.bar_code.recognize()
    if smart_camera.bar_code.type != None:
        print(str('条形码类型：') + str(smart_camera.bar_code.type))
        print(str('条形码数据：') + str(smart_camera.bar_code.info))
