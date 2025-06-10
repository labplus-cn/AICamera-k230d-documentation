人脸检测
==============

Python示例
-----------

.. literalinclude:: /_static/python-examples/人脸检测.py
    :caption: 例程：人脸检测
    :name: 人脸检测



mPython图形化示例
-----------
.. figure:: /_static/image/example/face_detect/face_detect.png
    :align: center
    :width: 1080


函数方法
-----------

.. function:: smart_camera.model_init(cur_state)
    :noindex:

    实例化模型

    :param cur_state: 初始化模型id
    :type cur_state: int

例::

    smart_camera.model_init(1)


.. class:: smart_camera.face_detect

    .. method:: recognize()
        :noindex:

        运行识别


.. class:: smart_camera.face_detect

    人脸检测实例

   :var int face_num: 人脸数量 
