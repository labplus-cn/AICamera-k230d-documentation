80类识别
==============

80类物体列表["人","自行车","汽车","摩托车","飞机","公共汽车","火车","卡车","船","交通灯","消防栓","停车标志","泊车计时器","长椅","鸟","猫","狗","马","绵羊","奶牛","大象","熊","斑马","长颈鹿","背包","雨伞","手提包","领带","手提箱","飞盘","滑雪板","运动球","风筝","棒球","蝙蝠","棒球手套","滑板","冲浪板","网球拍","瓶子","酒杯","杯子","叉子","刀","勺子","碗","香蕉","苹果","三明治","橙子","西兰花","胡萝卜","热狗","披萨","甜甜圈","蛋糕","椅子","沙发","盆栽","床","餐桌","厕所","电视","笔记本电脑","鼠标","遥控器","键盘","手机","微波炉","烤箱","烤面包机", "水槽","冰箱","书籍","时钟","花瓶","剪刀","泰迪熊","吹风机","牙刷"] 


代码
-----------
例程::

    from mpython import *
    import smartcamera_k230 as smartcamera

    smart_camera = smartcamera.SmartCameraK230(tx=Pin.P1, rx=Pin.P0)
    smart_camera.model_init(2)
    while True:
    smart_camera.yolo_detect.recognize() 
    if smart_camera.yolo_detect.id != None:
        print(str('类别：') + str(smart_camera.yolo_detect.category_list[smart_camera.yolo_detect.id]))
        print(str('置信度：') + str(smart_camera.yolo_detect.max_score))


mPython图形化示例
-----------
.. figure:: /_static/image/example/yolo_detect/yolo_detect.png
    :align: center
    :width: 1080