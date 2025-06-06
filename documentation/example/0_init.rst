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


.. function:: fetch_data(url, method='GET', timeout=30)
   :noindex:

   从指定URL获取数据。

   :param url: 请求的目标URL。
   :type url: str
   :param method: HTTP方法，可选 ``'GET'`` 或 ``'POST'``。
   :type method: str
   :param timeout: 超时时间（秒），默认为30。
   :type timeout: int
   :return: 包含响应状态和数据的字典。
   :rtype: dict
   :raises requests.Timeout: 请求超时时抛出。