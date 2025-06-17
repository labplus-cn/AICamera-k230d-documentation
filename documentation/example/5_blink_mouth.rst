眨眼张嘴检测
==============

Python示例
-----------

.. literalinclude:: /_static/python-examples/眨眼张嘴检测.py
    :caption: 例程：眨眼张嘴检测
    :name: 眨眼张嘴检测

mPython图形化示例
-----------

.. figure:: /_static/image/example/眨眼.png
    :align: center
    :width: 1080


函数方法
-----------

.. function:: smart_camera.model_init(cur_state)
    :noindex:

    实例化模型

    :param cur_state: 初始化模型id
    :type cur_state: int


.. class:: smart_camera.face_living_body

    .. method:: recognize()
        :noindex:

        运行识别


.. class:: smart_camera.face_living_body

    眨眼张嘴检测实例

   :var list mouth_blink_counter: 眨眼张嘴次数列表
   :var int mouth_blink_counter[0]: 眨眼次数
   :var int mouth_blink_counter[1]: 张嘴次数



测试视频
---------- 

.. video:: /_static/image/k230/blink_mouth.mp4
    :align: center
    :width: 640


