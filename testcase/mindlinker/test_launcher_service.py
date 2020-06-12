# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Text
import time


@allure.feature('首页-服务')
@pytest.mark.P0
class TestService(object):
    """
    step1：启动ML
    step2：判断当前设备是否已加入企业
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

    def test_service(self):
        # 启动ML
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(7)
        self.d.dump_hierarchy
        if not self.d(text=Text.JOIN).exists:
            raise LookupError

        # 判断当前的设备状态
        if self.d(resourceId=id.DOT).exists:
            self.d(resourceId=id.SERVICE).click(2)
            self.d.dump_hierarchy
            status = self.d(resourceId=id.DEVICES_STATUS).get_text()
            assert status == "加入企业"
        else:
            self.d(resourceId=id.SERVICE).click(2)
            self.d.dump_hierarchy
            status = self.d(resourceId=id.DEVICES_STATUS).get_text()
            assert status == "已加入"


if __name__ == '__main__':
    TestService()
