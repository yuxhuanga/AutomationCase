# -*- coding:utf-8 -*-

import uiautomator2
import time
"""
step1：连接设备并指定
step2：启动MindLinker
step3：刷新界面
step4：判断是否存在"发起会议"或者其他能够判断是在首页的元素,通过就点击,失败就打印
step5：最后结束会议
"""

# step1
d = uiautomator2.connect("192.168.7.125:5555")

# step2
d.app_start("com.cvte.captain.mindlinker")
time.sleep(5)

# step3
d.dump_hierarchy

# 判断元素是否存在的用法
if d.exists(text="发起会议"):   # 注意key值的大小写,也可以写成d(text="发起会议").exists()-->加上timeout
    print("done")

    try:
        assert d(resourceId="com.cvte.captain.mindlinker:id/createMeetingButton").exists
    except:
        print("resourceId not found")
    else:
        d(resourceId="com.cvte.captain.mindlinker:id/createMeetingButton").click()
else:
    print("fail")
# 如果不需要任何输出,可以直接简化成：d(resourceId="").click_exists()-->timeout

# 长按可以使用：d().long_click

# 拖拽、滑动等等更多api请根据实际需求使用,用法参考_selector.py

time.sleep(5)

d.dump_hierarchy

if not d.exists(resourceId="com.cvte.captain.mindlinker:id/windowMeetingLeave"):
    d.xpath('//android.widget.RelativeLayout[1]').click()
    time.sleep(1)
    d.dump_hierarchy
else:
    pass

d(resourceId="com.cvte.captain.mindlinker:id/windowMeetingLeave").click()
time.sleep(1)
d.dump_hierarchy
try:
    assert d(resourceId="com.cvte.captain.mindlinker:id/alertCenterBtn").exists
except:
    print("离开会议的弹窗异常")
else:
    d(resourceId="com.cvte.captain.mindlinker:id/alertCenterBtn").click()

time.sleep(3)
d(resourceId="com.cvte.captain.mindlinker:id/exitImageButton")



# xpath的使用方法
# d.xpath('//*[@resource-id="com.cvte.captain.mindlinker:id/windowMeetingLeave"]'
#        '/android.widget.ImageView[1]').click()
