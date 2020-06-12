# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Text
import time


@allure.feature('首页-加入会议-弹窗界面')
@pytest.mark.P0
class TestNumberView(object):
    """
    step1：启动ML
    step2：点击'加入会议'后判断弹窗,包括按钮是否可点击、关闭按钮等
    """
    d = uiautomator2.connect(id.IP)

    def setup_class(self):
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
        else:
            self.d(resourceId=id.EXIT).click()

    def test_number_view(self):
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(7)
        self.d.dump_hierarchy
        if not self.d(text=Text.JOIN).exists:
            raise LookupError
        # 点击加入会议
        self.d(resourceId=id.JOIN_MEETING).click()
        time.sleep(2)
        self.d.dump_hierarchy
        assert self.d.exists(resourceId=id.NUMBER_VIEW)
        # 获取确认按钮的属性以及输入框的默认文案
        en = self.d(resourceId=id.KEY_CONFIRM).info
        dt = en['enabled']
        txt = self.d(resourceId=id.BLANK_BOX).get_text()

        # 做界面元素的校验
        assert self.d.exists(resourceId=id.CLOSE_BUTTON)
        assert self.d.exists(resourceId=id.KEY_ONE)
        assert self.d.exists(resourceId=id.KEY_CLEAR)
        assert self.d.exists(resourceId=id.KEY_DELETE)
        assert dt is False
        assert txt == '会议邀请码'

        # 关闭弹窗
        self.d(resourceId=id.CLOSE_BUTTON).click()
        time.sleep(2)


if __name__ == '__main__':
    TestNumberView()


