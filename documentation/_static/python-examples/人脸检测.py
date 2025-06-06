from mpython import *
import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.model_init(1)

while True:
    smart_camera.face_detect.recognize()
    face_num = smart_camera.face_detect.face_num
    if face_num != None:
        print(str('人脸数量：') + str(face_num))
