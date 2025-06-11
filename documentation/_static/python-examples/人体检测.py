# 人体检测
from mpython import *
import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)
smart_camera.model_init(6)

while True:
    smart_camera.person_detect.recognize()
    color_flag = smart_camera.person_detect.flag  # 是否识别到 True/False
    if(color_flag == True):
        print(str('已识别到人体')) 







