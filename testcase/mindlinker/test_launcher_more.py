# -*- coding:utf-8 -*-

import pytest
import uiautomator2
import allure
import time

from element.element import ResourceId as id

@allure.feature("首页-更多")
@pytest.mark.P1
class TestLauncherMore(object):
    d = uiautomator2.connect(id.IP)

    def setup_class(self):
        self.d.dump_hierarchy
        if self.d.exists(resourceId=id.EXIT):
            self.d(resourceId=id.EXIT).click()

        self.d.app_start(id.PACKAGE_NAME)
        time.sleep(5)

        self.d.dump_hierarchy
        assert self.d.exists(resourceId=id.MORE)

    def teardown_class(self):
        self.d.dump_hierarchy

        # 退出MindLinker
        try:
            if self.d.exists(resourceId=id.FEEDBACK):
                self.d.click(600, 1978)
                time.sleep(1)
                self.d.dump_hierarchy
            else:
                assert self.d(resourceId=id.EXIT).exists
        except:
            self.d.app_stop(id.PACKAGE_NAME)
            print("不在mindlinker首页,直接kill进程")
        else:
            self.d(resourceId=id.EXIT).click()

    def test_more(self):
        self.d(resourceId=id.MORE).click()
        time.sleep(1)
        self.d.dump_hierarchy

        assert self.d(resourceId=id.SETTING).exists
        assert self.d.exists(resourceId=id.FEEDBACK)
        assert self.d.exists(resourceId=id.ABOUT)


if __name__ == '__main__':
    TestLauncherMore()
