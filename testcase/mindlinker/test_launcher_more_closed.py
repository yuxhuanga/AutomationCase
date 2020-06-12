# -*- coding:utf-8 -*-

import pytest
import allure
import uiautomator2
import time

from element.element import ResourceId as id


@allure.feature("首页-更多-关闭")
@pytest.mark.P1
class TestLauncherMoreClosed(object):
    """
    step1：启动ML
    step2：打开首页的设置
    step3：点击空白地方关闭设置,校验反馈等按钮是否存在
    """
    d = uiautomator2.connect(id.IP)

    def setup_class(self):
        self.d.dump_hierarchy
        # 判断当前界面是否在ML,在则退出再重新启动
        if self.d.exists(resourceId=id.EXIT):
            self.d(resourceId=id.EXIT).click()

    def teardown_class(self):
        self.d.dump_hierarchy

        # 退出MindLinker
        try:
            assert self.d(resourceId=id.EXIT).exists
        except:
            self.d.app_stop(id.PACKAGE_NAME)
        else:
            self.d(resourceId=id.EXIT).click()

    def test_closed(self):

        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(7)
        # 校验启动是否成功
        self.d.dump_hierarchy
        assert self.d.exists(resourceId=id.MORE)
        # 点击更多
        self.d(resourceId=id.MORE).click()
        time.sleep(2)
        self.d.dump_hierarchy

        # 校验设置、反馈和关于按钮
        assert self.d(resourceId=id.SETTING).exists
        assert self.d(resourceId=id.FEEDBACK).exists
        assert self.d(resourceId=id.ABOUT).exists
        time.sleep(2)
        # 点击空白处
        self.d.click(600, 1978)
        time.sleep(2)
        self.d.dump_hierarchy

        # 判断反馈按钮,不存在则用例通过
        assert not self.d.exists(resourceId=id.FEEDBACK)


if __name__ == '__main__':
    TestLauncherMoreClosed()
