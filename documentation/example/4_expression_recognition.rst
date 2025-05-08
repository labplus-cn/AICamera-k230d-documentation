表情识别
==============

代码
-----------
例程::

    from mpython import *
    import smartcamera_k230 as smartcamera

    smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)
    smart_camera.model_init(28)

    while True:
        smart_camera.face_expression.recognize()
        expression = smart_camera.face_expression.expression #表情id
        expression_str = smart_camera.face_expression.expression_str #表情字符串
        if(expression != None):
            print(str('表情id:') + str(expression))
            print(str('表情:') + str(expression_str))
        
    



mPython图形化示例
-----------
