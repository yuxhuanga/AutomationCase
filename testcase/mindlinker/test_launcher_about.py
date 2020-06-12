# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Text
import time


@allure.feature('首页-关于')
@pytest.mark.P2
class TestAbout(object):
    """
    step1：启动ML
    step2：点击更多-关于
    step3：校验界面元素
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

    def test_about(self):
        # 启动ML
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(7)
        self.d.dump_hierarchy
        if not self.d(text=Text.JOIN).exists:
            raise LookupError
        # 点击更多-反馈
        self.d(resourceId=id.MORE).click()
        self.d(resourceId=id.ABOUT).click(2)
        time.sleep(2)
        self.d.dump_hierarchy
        # 校验界面元素
        assert self.d(text=Text.ABOUT)
        assert self.d(resourceId=id.VERSION)
        assert self.d(resourceId=id.SDK)
        assert self.d(resourceId=id.ABOUT_CLOSE)
        assert self.d(resourceId=id.CHECK_UPDATE)
        assert self.d(resourceId=id.DOWNLOAD)

        self.d(resourceId=id.ABOUT_CLOSE).click(2)
        time.sleep(2)
        self.d.dump_hierarchy
        assert self.d(resourceId=id.EXIT).exists


if __name__ == '__main__':
    TestAbout()
