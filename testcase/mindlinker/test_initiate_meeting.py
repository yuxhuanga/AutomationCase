# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Xpath
from element.element import Text
import time


@allure.feature("首页-发起会议")
@pytest.mark.P0
class TestInitiateMeeting(object):
    """
    step1：启动ML,判断是否在首页
    step2：点击首页的发起会议
    step3：通过菜单栏判断是否创建会议成功
    """
    d = uiautomator2.connect(id.IP)

    # @allure.step("前置条件")
    def setup_class(self):
        self.d.dump_hierarchy
        if self.d.exists(resourceId=id.EXIT):
            self.d(resourceId=id.EXIT).click()

    # @allure.step("恢复测试环境")
    def teardown_class(self):
        self.d.dump_hierarchy

        # 退出MindLinker
        try:
            assert self.d(resourceId=id.EXIT).exists
        except:
            self.d.app_stop(id.PACKAGE_NAME)
        else:
            self.d(resourceId=id.EXIT).click()

    @allure.story("执行用例")
    def test_start(self):
        # 等待启动应用
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(5)

        self.d.dump_hierarchy

        # 判断是否在MindLinker首页,点击发起会议
        if self.d.exists(text=Text.CREATE):
            self.d(resourceId=id.CREATE_MEETING).click()

        time.sleep(5)
        # 等5s进入视频会议
        self.d.dump_hierarchy

        # 判断是否在菜单栏是否存在,若不存在,继续判断是否在会中
        if not self.d.exists(resourceId=id.HANGUP_LAYOUT):
            try:
                assert self.d.exists(resourceId=id.MEETING_ID)
            except:
                raise ValueError
            else:
                self.d.click(3790, 1756)
                time.sleep(1)
                self.d.dump_hierarchy
        # 点击离开
        self.d(resourceId=id.HANGUP_LAYOUT).click()

        time.sleep(2)
        self.d.dump_hierarchy

        # 点击结束会议
        try:
            assert self.d(resourceId=id.ALERT_CENTER_BUTTON).exists
        except:
            raise ValueError
        else:
            self.d(resourceId=id.ALERT_CENTER_BUTTON).click()
        time.sleep(3)


if __name__ == '__main__':
    TestInitiateMeeting()
