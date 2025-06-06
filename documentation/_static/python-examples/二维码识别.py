from mpython import *
import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.model_init(5)

while True:
    smart_camera.qrcode.recognize()
    info = smart_camera.qrcode.info
    if info != None:
        print(str('二维码内容：') + str(info))
