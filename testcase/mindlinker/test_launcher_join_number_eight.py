# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Text
import time


@allure.feature('首页-加入会议-输入八位数字')
@pytest.mark.P0
class TestNumberEight(object):
    """
    step1：启动ML并点击加入会议
    step2：输入八位数字
    step3：判断按钮是否可点击
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

    def test_eight_number(self):
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(7)
        self.d.dump_hierarchy
        if not self.d(text=Text.JOIN).exists:
            raise LookupError
        self.d(resourceId=id.JOIN_MEETING).click()
        time.sleep(2)
        # 先判断按钮为不可点击
        self.d.dump_hierarchy
        assert self.d.exists(resourceId=id.NUMBER_VIEW)

        en = self.d(resourceId=id.KEY_CONFIRM).info
        dt = en['enabled']
        assert dt is False
        # 输入12345678,再次判断按钮的可点击态
        self.d(resourceId=id.EDIT_BOX).set_text("12345678")
        time.sleep(2)
        self.d.dump_hierarchy
        assert self.d.exists(resourceId=id.NUMBER_VIEW)

        en1 = self.d(resourceId=id.KEY_CONFIRM).info
        dt1 = en1['enabled']
        assert dt1 is True
        # 关闭弹窗
        self.d(resourceId=id.CLOSE_BUTTON).click()
        time.sleep(2)


if __name__ == '__main__':
    TestNumberEight()
