# -*- coding:utf-8 -*-

import pytest
import allure


def setup_module(self):
    print("setup_class")


def teardown_module(self):
    print("teardown_class")

@allure.feature("首页-界面显示")
@pytest.mark.P0
class TestLauncher(object):


    @allure.step("步骤1")
    def test_launcher0(self):
        print("test1")

    @allure.step("步骤2")
    def test_launcher1(self):
        print("test2")


if __name__ == '__main__':
    TestLauncher()
