from mpython import *
import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.model_init(8)

while True:
    smart_camera.lpr.recognize()
    lpr_str = smart_camera.lpr.lpr_str
    if lpr_str != None:
        print(str('车牌：') + str(lpr_str))
