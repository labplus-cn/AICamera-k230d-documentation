# LAB颜色识别 
from mpython import *
import smartcamera_k230 as smartcamera

smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)
smart_camera.lab_color_count_init([0, 40, 0, 90, -128, -20]) # [Lmin,Lmax,A,B]

while True:
    smart_camera.lab_color_count.recognize()
    color_flag = smart_camera.lab_color_count.flag  # 是否识别到 True/False
    color_count = smart_camera.lab_color_count.color_count
    if(color_flag != None):
        print(str('色块计数:') + str(color_count)) 




