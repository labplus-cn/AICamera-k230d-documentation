眨眼张嘴检测
==============

代码
-----------
例程::
    
    from mpython import *
    import smartcamera_k230 as smartcamera

    smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)
    smart_camera.model_init(27)

    while True:
        smart_camera.face_living_body.recognize()
        mouth_blink_counter = smart_camera.face_living_body.mouth_blink_counter #[眨眼次数,张嘴次数]
        if(mouth_blink_counter[0] != None):
            print(str('眨眼次数:') + str(mouth_blink_counter[0]))
            print(str('张嘴次数:') + str(mouth_blink_counter[1]))
            if(mouth_blink_counter[0]==3 and mouth_blink_counter[1]==3):
                print('执行开门')
            else:
                pass
        

测试视频
-----------   
.. video:: /_static/image/k230/blink_mouth.mp4
    :align: center
    :width: 640


mPython图形化示例
-----------
