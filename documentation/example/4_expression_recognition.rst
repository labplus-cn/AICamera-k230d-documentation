表情识别
==============

Python示例
-----------

.. literalinclude:: /_static/python-examples/表情识别.py
    :caption: 例程：表情识别
    :name: 表情识别


mPython图形化示例
-----------
.. figure:: /_static/image/example/face_expression.png
    :align: center
    :width: 800



函数方法
-----------

.. function:: smart_camera.model_init(cur_state)
    :noindex:

    实例化模型

    :param cur_state: 初始化模型id
    :type cur_state: int


.. class:: smart_camera.face_expression

    .. method:: recognize()
        :noindex:

        运行识别


.. class:: smart_camera.face_expression

    表情识别实例

   :var int expression: 表情id ：0-4  
   :var str expression_str: 表情字符串 ：['normal','smile happy','sadness','surprise','anger']


演示
-----------

.. video:: /_static/video/AI摄像头4.0-表情识别.mp4
    :align: center
    :width: 640


表情示例
-----------

.. figure:: /_static/image/k230/表情/开心.jpeg
    :align: center
    :width: 640

    开心


.. figure:: /_static/image/k230/表情/悲伤.jpg
    :align: center
    :width: 640

    悲伤


.. figure:: /_static/image/k230/表情/惊讶.jpg
    :align: center
    :width: 640

    惊讶
