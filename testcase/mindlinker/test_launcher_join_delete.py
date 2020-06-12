# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Text
import time


@allure.feature('首页-加入会议-清空输入框')
@pytest.mark.P1
class TestClear(object):
    """
    step1：启动ML并点击加入会议
    step2：输入预设的数字,判断数字是否输入成功
    step3：清除数字后判断默认文案
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

    def test_clear(self):
        # 启动ML
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(7)
        self.d.dump_hierarchy
        if not self.d(text=Text.JOIN).exists:
            raise LookupError

        # 点击加入会议按钮
        self.d(resourceId=id.JOIN_MEETING).click()
        time.sleep(2)
        self.d.dump_hierarchy
        assert self.d.exists(resourceId=id.NUMBER_VIEW)

        # 输入1234
        self.d(resourceId=id.EDIT_BOX).set_text("1234")
        time.sleep(2)

        # 判断输入的数字
        self.d.dump_hierarchy
        num = self.d(resourceId=id.EDIT_BOX).get_text()
        assert num == '1234'
        time.sleep(1)

        # 每删除一位数字后再做校验
        for i in range(0, 3):
            self.d(resourceId=id.KEY_DELETE).click()
            time.sleep(2)
            self.d.dump_hierarchy
            num1 = self.d(resourceId=id.EDIT_BOX).get_text()
            if i == 0:
                assert num1 == '123'
            elif i == 1:
                assert num1 == '12'
            else:
                assert num1 == '1'

        self.d(resourceId=id.CLOSE_BUTTON).click()


if __name__ == '__main__':
    TestClear()
