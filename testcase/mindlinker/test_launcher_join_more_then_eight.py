# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Text
import time


@allure.feature('首页-加入会议-最多输入11位数字')
@pytest.mark.P0
class TestInputMax(object):
    """
    step1：启动ML并点击加入会议
    step2：输入超过11位数字
    step3：判断输入框内容
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

    def test_eleven(self):
        # 把数字0-9排列成一个组合
        key_list = [id.KEY_ONE, id.KEY_TWO, id.KEY_THREE, id.KEY_FOUR,
                    id.KEY_FIVE, id.KEY_SIX, id.KEY_SEVEN, id.KEY_EIGHT,
                    id.KEY_NINE, id.KEY_ZERO, id.KEY_ONE, id.KEY_TWO, id.KEY_THREE]
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

        # 循环列表内的元素并进行输入
        for i in range(0, 13):
            self.d(resourceId=key_list[i]).click()
            time.sleep(1)

        # 判断输入的数字
        self.d.dump_hierarchy
        num = self.d(resourceId=id.EDIT_BOX).get_text()
        assert num == '1234 5678 901'

        time.sleep(2)
        self.d(resourceId=id.CLOSE_BUTTON).click()


if __name__ == '__main__':
    TestInputMax()
