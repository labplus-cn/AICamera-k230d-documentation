人体骨骼姿态识别分类
==============

演示
-----------


代码
-----------
例程::
    
    from mpython import *
    import smartcamera_k230 as smartcamera

    smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)
    smart_camera.model_init(11)


    while True:
        smart_camera.person_keypoint_detect_plus.recognize()
        id = smart_camera.person_keypoint_detect_plus.id #姿态识别id
        if(id != None):
            print(str('姿态识别id:') + str(id))
        



mPython图形化示例
-----------
