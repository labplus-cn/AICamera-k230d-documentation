from mpython import *
import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.model_init(31)

while True:
    smart_camera.fcr.recognize()
    face_id = smart_camera.fcr.id
    if face_id != None:
        print(str('人脸id：') + str(face_id))
        print(str('置信度：') + str(smart_camera.fcr.score))
