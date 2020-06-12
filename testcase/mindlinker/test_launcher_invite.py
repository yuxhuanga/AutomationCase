# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Text
import time


@allure.feature('首页-通讯录')
@pytest.mark.P0
class TestInvite(object):
    """
    step1：启动ML
    step2：点击通讯录
    step3：判断按钮可点击态和设备列表
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

    def test_invite(self):
        # 启动ML
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(7)
        self.d.dump_hierarchy

        self.d(resourceId=id.CONTACT).click(2)
        time.sleep(2)
        self.d.dump_hierarchy
        assert self.d(resourceId=id.CONTACT_NAME)
        assert self.d(resourceId=id.CONTACT_CHECK_BOX)

        info = self.d(resourceId=id.CONFIG_BUTTON).info
        status = info['enabled']
        assert status is False


if __name__ == '__main__':
    TestInvite()
