手势识别
===================

例程::

    from mpython import *
    import smartcamera_k230 as smartcamera

    smart_camera = smartcamera.SmartCameraK230(tx=Pin.P16, rx=Pin.P15)
    smart_camera.model_init(4)

    while True:
        smart_camera.hand_keypoint_class.recognize()
        print(str('手势id:') + str(smart_camera.hand_keypoint_class.gesture_id))
        print(str('手势字符串:') + str(smart_camera.hand_keypoint_class.gesture_str))
        




mPython图形化示例
----------------
.. figure:: /_static/image/example/track/track_color.png
    :align: center
    :width: 1080