初始化AI摄像头4.0
==============

.. _SmartCamera:

.. class:: SmartCameraK230(tx=Pin.P16, rx=Pin.P15)
   :synopsis: AI摄像头4.0类 

.. method::  SmartCameraK230(tx=Pin.P16, rx=Pin.P15)

``tx`` 
串口发送引脚

``rx``
串口接收引脚

例如::
    
    from mpython import *
    import smartcamera_k230 as smartcamera
    smartcamera.SmartCamera(tx=Pin.P16, rx=Pin.P15)


mPython图形化示例
-----------
.. figure:: /_static/image/example/face_detect/face_detect.png
    :align: center
    :width: 1080
