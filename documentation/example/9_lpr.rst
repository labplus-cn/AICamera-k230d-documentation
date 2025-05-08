车牌识别
==============

车牌识别
-----------
例程::

    from mpython import *
    import smartcamera_k230 as smartcamera

    smart_camera = smartcamera.SmartCameraK230(tx=Pin.P16, rx=Pin.P15)
    smart_camera.model_init(8)

    while True:
        smart_camera.lpr.recognize()
        lpr = smart_camera.lpr.lpr_str # 车牌字符串
        if(lpr != None):
            print(str('车牌:') + str(lpr))
            print(len(lpr))
            



mPython图形化示例
-----------

