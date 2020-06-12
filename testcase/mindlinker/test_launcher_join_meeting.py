# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
from element.element import ResourceId as id
from element.element import Text
import time


@allure.feature('首页-输入会议邀请码加入会议')
@pytest.mark.P0
class TestJoinFail(object):
    """
    step1：启动ML并点击加入会议
    step2：先创建会议,获取会议号之后离开
    step3：通过会议号再次加入会议
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

    def test_join_meeting(self):
        # 启动ML
        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(7)
        self.d.dump_hierarchy
        if not self.d(text=Text.JOIN).exists:
            raise LookupError

        # 直接创建会议,并且获取会议号
        self.d(resourceId=id.CREATE_MEETING).click()
        time.sleep(15)
        self.d.dump_hierarchy
        meeting_id = self.d(resourceId=id.MEETING_ID).get_text()

        # 离开会议
        self.d.click(3790, 1756)
        self.d(resourceId=id.HANGUP_LAYOUT).click(2)
        self.d(resourceId=id.ALERT_CONFIRM_BUTTON).click(2)

        # 把前一个会议中获得的会议号输入并加入
        self.d.dump_hierarchy
        self.d(resourceId=id.JOIN_MEETING).click(5)
        self.d(resourceId=id.EDIT_BOX).set_text(meeting_id)
        self.d(resourceId=id.KEY_CONFIRM).click()
        time.sleep(12)
        self.d.dump_hierarchy

        # 校验左上角会议号和会议时间
        assert self.d(resourceId=id.MEETING_ID).exists
        assert self.d(resourceId=id.MEETING_TIME).exists

        # 离开会议
        self.d.click(3790, 1756)
        self.d(resourceId=id.HANGUP_LAYOUT).click(2)
        self.d(resourceId=id.ALERT_CENTER_BUTTON).click(2)
        time.sleep(5)


if __name__ == '__main__':
    TestJoinFail()
