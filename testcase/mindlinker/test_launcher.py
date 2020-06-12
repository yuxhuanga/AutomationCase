# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
import time

from element.element import ResourceId as id

@allure.feature("首页-界面显示")
@pytest.mark.P0
class TestLauncher(object):
    """
    step1：启动ML
    step2：判断首页的元素（按钮、文案）是否存在
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

    def test_launcher(self):
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(5)
        self.d.dump_hierarchy

        # 判断首页的元素是否存在
        assert self.d(resourceId=id.MINDLINKER).exists
        assert self.d(resourceId=id.DEVICES_NAME).exists
        assert self.d(resourceId=id.CREATE_MEETING).exists
        assert self.d(resourceId=id.JOIN_MEETING).exists
        assert self.d(resourceId=id.SCREEN_SHARE).exists
        assert self.d(resourceId=id.EXIT).exists
        assert self.d(resourceId=id.MORE).exists
        assert self.d(resourceId=id.SERVICE).exists
        time.sleep(1)


if __name__ == '__main__':
    TestLauncher()
