# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Text
import time


@allure.feature('首页-加入会议-点击空白区域')
@pytest.mark.P0
class TestClickBlank(object):
    """
    step1：启动ML
    step2：打开会议号输入框
    step3：点击空白地方,不关闭输入框则用例通过
    """
    d = uiautomator2.connect(id.IP)

    def setup_class(self):
        # 判断当前界面如果在ML则关闭重新启动
        self.d.dump_hierarchy
        if self.d.exists(resourceId=id.EXIT):
            self.d(resourceId=id.EXIT).click()

    def teardown_class(self):
        self.d.dump_hierarchy

        # 退出MindLinker
        try:
            assert self.d(resourceId=id.EXIT).exists
        except:
            self.d.app_stop(id.PACKAGE_NAME)
            print("不在mindlinker首页,直接kill进程")
        else:
            self.d(resourceId=id.EXIT).click()

    def test_click_blank(self):
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(7)
        self.d.dump_hierarchy
        if not self.d(text=Text.JOIN).exists:
            raise LookupError

        # 点击加入会议
        self.d(resourceId=id.JOIN_MEETING).click()
        time.sleep(2)
        self.d.dump_hierarchy
        # 判断输入框
        assert self.d.exists(resourceId=id.NUMBER_VIEW)
        time.sleep(2)

        # 点击空白处
        self.d.click(3000, 456)
        time.sleep(2)
        self.d.dump_hierarchy
        assert not self.d.exists(resourceId=id.NUMBER_VIEW)
        self.d(resourceId=id.CLOSE_BUTTON).click()
        time.sleep(2)


if __name__ == '__main__':
    TestClickBlank()
