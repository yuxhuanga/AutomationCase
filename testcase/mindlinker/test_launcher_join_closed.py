# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Text
import time


@allure.feature('首页-加入会议-弹窗界面')
@pytest.mark.P0
class TestNumberViewClosed(object):
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
            print("不在mindlinker首页,直接kill进程")
        else:
            self.d(resourceId=id.EXIT).click()

    def test_number_view_closed(self):
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(5)
        self.d.dump_hierarchy
        if not self.d(text=Text.JOIN).exists:
            raise LookupError
        self.d(resourceId=id.JOIN_MEETING).click()
        time.sleep(2)
        self.d.dump_hierarchy
        assert self.d.exists(resourceId=id.NUMBER_VIEW)
        self.d(resourceId=id.CLOSE_BUTTON).click()
        time.sleep(2)
        self.d.dump_hierarchy
        assert self.d.exists(resourceId=id.JOIN_MEETING)


if __name__ == '__main__':
    TestNumberViewClosed()

