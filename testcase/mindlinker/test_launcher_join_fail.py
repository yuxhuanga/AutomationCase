# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Text
import time


@allure.feature('首页-加入会议失败')
@pytest.mark.P2
class TestJoinFail(object):
    """
    step1：启动ML并点击加入会议
    step2：输入不存在的会议号
    step3：校验失败弹窗
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

    def test_join_fail(self):
        # 启动ML
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(7)
        self.d.dump_hierarchy
        if not self.d(text=Text.JOIN):
            raise LookupError

        # 点击加入会议按钮
        self.d(resourceId=id.JOIN_MEETING).click()
        time.sleep(2)
        self.d.dump_hierarchy
        assert self.d.exists(resourceId=id.NUMBER_VIEW)

        self.d(resourceId=id.EDIT_BOX).set_text("00000000")
        time.sleep(2)
        self.d(resourceId=id.KEY_CONFIRM).click()
        time.sleep(1.5)

        self.d.dump_hierarchy
        assert self.d(resourceId=id.DIALOG_TEXT).exists
        time.sleep(4)
        self.d.dump_hierarchy
        assert self.d(resourceId=id.EXIT).exists


if __name__ == '__main__':
    TestJoinFail()
