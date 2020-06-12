# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Xpath
import time

"""
类名必须Test开头
函数名必须test_开头
@pytest.mark是用来标记一个函数的
跳过用例标记为：@pytest.mark.skip(reason='')
"""


@allure.feature("启动mindlinker")
@pytest.mark.P1
class TestStartMindLinker(object):
    d = uiautomator2.connect(id.IP)

    # @allure.step("前置条件")
    def setup(self):
        """
        用例执行的前置条件可以放到这里
        :return:
        """
        pass

    # @allure.step("恢复测试环境")
    def teardown(self):
        """
        用例执行完成后的环境恢复请放到这里来。(这个函数不管用例执行成功或者失败,总会执行到)
        :return:None
        """
        self.d.dump_hierarchy

        # 退出MindLinker
        try:
            assert self.d(resourceId=id.EXIT).exists
        except:
            self.d.app_stop(id.PACKAGE_NAME)
            print("不在mindlinker首页,直接kill进程")
        else:
            self.d(resourceId=id.EXIT).click()

    @allure.story("执行用例")
    def test_start(self):
        """
        测试步骤写在这里
        :return:
        """
        # 等待启动应用
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(5)

        self.d.dump_hierarchy

        # 判断是否在MindLinker首页
        if self.d.exists(text="发起会议"):
            self.d(resourceId=id.CREATE_MEETING).click()
        else:
            print("start mindlinker failed")

        time.sleep(5)
        # 等5s进入视频会议
        self.d.dump_hierarchy

        # 判断是否在菜单栏是否存在,若不存在,继续判断是否在会中
        if not self.d.exists(resourceId=id.HANGUP_LAYOUT):
            try:
                assert self.d.exists(resourceId=id.MEETING_ID)
            except:
                print("会中侧边栏不存在")
            else:
                self.d.click(3790, 1756)
                time.sleep(1)
                self.d.dump_hierarchy
        # 点击离开
        self.d(resourceId=id.HANGUP_LAYOUT).click()

        time.sleep(2)
        self.d.dump_hierarchy

        # 点击结束会议
        try:
            assert self.d(resourceId=id.ALERT_CENTER_BUTTON).exists
        except:
            print("离开会议的弹窗异常")
        else:
            self.d(resourceId=id.ALERT_CENTER_BUTTON).click()
        time.sleep(3)


if __name__ == '__main__':
    TestStartMindLinker()
