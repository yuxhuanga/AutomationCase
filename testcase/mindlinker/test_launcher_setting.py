# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Text
import time


@allure.feature('首页-设置')
@pytest.mark.P0
class TestSetting(object):
    """
    step1：启动ML
    step2：点击更多-设置
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

    def test_setting(self):
        # 启动ML
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(7)
        self.d.dump_hierarchy
        if not self.d(text=Text.JOIN).exists:
            raise LookupError
        # 点击更多-设置
        self.d(resourceId=id.MORE).click()
        self.d(resourceId=id.SETTING).click(2)
        time.sleep(2)
        self.d.dump_hierarchy
        # 校验界面元素
        assert self.d(resourceId=id.SETTING_CLOSE).exists
        assert self.d(resourceId=id.TAB_AUDIO).exists
        assert self.d(resourceId=id.TAB_VIDEO).exists
        assert self.d(resourceId=id.ONLY_SELF).exists
        assert self.d(resourceId=id.VIDEO_PREVIEW).exists

        self.d(resourceId=id.SETTING_CLOSE).click(2)


if __name__ == '__main__':
    TestSetting()