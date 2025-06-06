from mpython import *
import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)

smart_camera.model_init(28)

while True:
    smart_camera.face_expression.recognize()
    if smart_camera.face_expression.expression != None:
        print(str('手势id：') + str(smart_camera.face_expression.expression))
        print(str('表情：') + str(smart_camera.face_expression.expression_str))
