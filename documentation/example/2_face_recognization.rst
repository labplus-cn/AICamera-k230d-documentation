人脸识别
==============

Python示例
-----------

.. literalinclude:: /_static/python-examples/人脸识别.py
    :caption: 例程：人脸识别
    :name: 人脸识别


mPython图形化示例
-----------
.. figure:: /_static/image/example/face_recognization/face_recognization.png
    :align: center
    :width: 1080


函数方法
-----------

.. function:: smart_camera.model_init(cur_state)
    :noindex:

    实例化模型

    :param cur_state: 初始化模型id
    :type cur_state: int


.. class:: smart_camera.fcr

    .. method:: recognize()
        :noindex:

        运行识别


.. class:: smart_camera.fcr

    人脸识别实例

   :var int face_id: 人脸id 
   :var float score: 人脸置信度



人脸注册
-----------

打开摄像头拍照模式,拍照选取合适的人脸图片
^^^^^^^^^^^^^^^^^^^^

一张图片中只有一个人脸，正面人脸，照片分辨率支持低于1000*1000 jpg、png格式图像

.. figure:: /_static/image/example/face_recognization/1.jpg
    :align: center
    :width: 1080


打开相册
^^^^^^^^^^^^^^^^^^^^

图片路径/CanMV/data/Camera/Photos

.. figure:: /_static/image/example/face_recognization/2.png
    :align: center
    :width: 1080

复制人脸图片到人脸数据目录
^^^^^^^^^^^^^^^^^^^^^^^^

复制人脸图片到人脸数据目录，按数字命名，从0开始

人脸数据路径 /CanMV/sdcard/data/face_img

.. figure:: /_static/image/example/face_recognization/5.jpg
    :align: center
    :width: 1080


注册人脸，等待出现成功提示
^^^^^^^^^^^^^^^^^^^^

.. figure:: /_static/image/example/face_recognization/3.jpg
    :align: center
    :width: 1080


.. figure:: /_static/image/example/face_recognization/4.jpg
    :align: center
    :width: 1080


.. Attention:: 注册成功的人脸永久有效，添加新的人脸后要重新执行人脸注册

.. Attention:: /CanMV/sdcard/data/face_db 查看人脸数据库路径