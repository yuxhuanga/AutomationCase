# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Text
import time


@allure.feature('首页-反馈')
@pytest.mark.P2
class TestFeedback(object):
    """
    step1：启动ML
    step2：点击更多-反馈
    step3：校验二维码
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

    def test_feedback(self):
        # 启动ML
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(7)
        self.d.dump_hierarchy
        if not self.d(text=Text.JOIN).exists:
            raise LookupError
        # 点击更多-反馈
        self.d(resourceId=id.MORE).click()
        self.d(resourceId=id.SETTING).click(2)
        time.sleep(2)
        self.d.dump_hierarchy
        # 校验界面元素
        assert self.d(resourceId=id.QR_CLOSE)
        assert self.d(resourceId=id.FEEDBACK_QR)
        assert self.d(text=Text.FEEDBACK_TXT)
        assert self.d(text=Text.PLEASE_USE)

        self.d(resourceId=id.ABOUT_CLOSE).click(2)


if __name__ == '__main__':
    TestFeedback()