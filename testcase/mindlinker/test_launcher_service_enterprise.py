# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Text
import time


@allure.feature('首页-服务-已加入企业')
@pytest.mark.P0
class TestEnterprise(object):
    """
    step1：启动ML
    step2：已加入企业的弹窗
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

    def test_enterprise(self):
        # 启动ML
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(7)
        self.d.dump_hierarchy

        if self.d(resourceId=id.DOT).exists:
            raise ValueError

        self.d(resourceId=id.SERVICE).click(2)
        self.d(resourceId=id.SERVICE_MENU).click(2)
        time.sleep(2)
        self.d.dump_hierarchy

        assert self.d(resourceId=id.DEVICES_STATUS).exists
        assert self.d(resourceId=id.ENTERPRISE_NAME).exists
        assert self.d(text=Text.DOES_NOT_BELONG).exists
        assert self.d(text=Text.CLICK_FEEDBACK).exists

        self.d(resourceId=id.SERVICE_CLOSE).click(2)
        time.sleep(2)
        self.d.dump_hierarchy
        assert self.d(resourceId=id.EXIT).exists


if __name__ == '__main__':
    TestEnterprise()
