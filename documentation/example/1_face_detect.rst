人脸检测
==============

代码
-----------
例程::

    from mpython import *
    import smartcamera_k230 as smartcamera

    smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)
    smart_camera.model_init(1)
    while True:
        smart_camera.face_detect.recognize() 
        print(str('face_num:') + str(smart_camera.face_detect.face_num)) # 人脸数量




mPython图形化示例
-----------
.. figure:: /_static/image/example/face_detect/face_detect.png
    :align: center
    :width: 1080


方法
-----------


.. _face_detect:

.. class:: smart_camera.model_init()
   :synopsis: 人脸检测实例化对象

.. method::  smart_camera.model_init(1)

``cur_state`` -整型 模型选择

例::

    smart_camera.model_init(1)

.. method::  face_detect.recognize() 
运行人脸识别

.. method::  face_detect.face_num
人脸检测数量 整型

.. method::  face_detect.max_score
人脸检测概率 浮点型 范围：[0-1]