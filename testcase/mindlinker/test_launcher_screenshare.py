# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Text
import time


@allure.feature("首页-屏幕共享")
@pytest.mark.P0
class TestScreenShare(object):
    """
    step1：启动ML
    step2：点击屏幕共享
    step3：判断菜单栏和结束共享的按钮
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
    def test_screenshare(self):
        # 等待启动应用
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(5)

        self.d.dump_hierarchy

        # 判断是否在MindLinker首页,点击屏幕共享
        if self.d.exists(text=Text.SHARE):
            self.d(resourceId=id.SCREEN_SHARE).click()
        else:
            raise LookupError
        time.sleep(6)
        # 等6进入视频会议
        self.d.dump_hierarchy
        txt = self.d(resourceId=id.SCREEN_SHARE_TEXT).get_text()
        if txt == "结束共享":
            time.sleep(5)

        self.d.dump_hierarchy
        assert self.d(resourceId=id.MEETING_ID).exists
        assert self.d(resourceId=id.MEETING_TIME).exists
        assert self.d(resourceId=id.SHARING_STATUS).exists

        self.d.click(3790, 1756)
        time.sleep(2)
        self.d.dump_hierarchy

        assert txt == "结束共享"
        # 点击离开
        self.d(resourceId=id.HANGUP_LAYOUT).click()
        time.sleep(2)
        self.d.dump_hierarchy

        # 点击结束会议
        try:
            assert self.d(resourceId=id.ALERT_CENTER_BUTTON).exists
        except:
            raise LookupError
        else:
            self.d(resourceId=id.ALERT_CENTER_BUTTON).click()
        time.sleep(3)


if __name__ == '__main__':
    TestScreenShare()
