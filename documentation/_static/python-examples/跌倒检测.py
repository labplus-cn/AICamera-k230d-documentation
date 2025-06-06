from mpython import *
import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.model_init(7)

while True:
    smart_camera.fall.recognize()
    fall_id = smart_camera.fall.id
    if fall_id != None:
        print(str('跌倒id：') + str(fall_id))
