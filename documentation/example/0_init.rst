初始化AI摄像头4.0
==============

.. class:: SmartCameraK230(tx=Pin.P16, rx=Pin.P15)

    实例化AI摄像头4.0类 

    :param tx: 串口发送引脚
    :type tx: int
    :param rx: 串口接收引脚
    :type rx: int


例如::
    
    from mpython import *
    import smartcamera_k230 as smartcamera
    smartcamera.SmartCamera(tx=Pin.P16, rx=Pin.P15)


mPython图形化示例
-----------
.. figure:: /_static/image/example/init.png
    :align: center
    :width: 1080
