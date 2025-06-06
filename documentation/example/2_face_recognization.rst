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

