## MindLinker自动化

-------------------------------
#### 感谢DSS项目的小伙伴鼎力支持,根据 **robothub** 这个框架的描述：

* 通过UIautomator2 + weditor + pytest + allure + airtest + ADB 来实现Android、Windows和Linux的自动化测试。

* 需要搭建的环境有：Python 3、Python的编辑器、adb环境变量和git。如果需要用到web端,还需要下载对应的webdrive。

* 需要的Python库：uiautomator2、weditor、pytest、opencv-python、airtest、selenium、allure-python

-------------------------------
##### 以下出自个人理解的不成熟的建议

#### 维护
* **测试用例：**

    1.放到testcase文件夹统一管理,可以在这个文件夹内创建对应模块的文件夹管理相关用例
    
    2.具体可参考test_pytest.py文件
    
    3.ui2的api参考test_ui2.py
    
        注意：
    
        * 测试文件以test_开头(以_test结尾也可以,注意大小写)
        * 测试类以Test开头,并且不能带有init方法
        * 测试函数以test_开头
        * 断言使用基本的assert即可
    
    
* **界面元素：**

    放到element文件夹管理,有需要的可以新建多个文件,建议每个人单独维护自己那部分的内容,可以是文件,也可以创建新的类,但是一定要有标识
    
* **其他：**

    如果需要封装函数或者方法,可以新建文件或者文件夹管理,之后再继续补充

* **关于用例：**
    
    1、多使用断言来保证用例的准确性
    
    2、在可能出现异常的地方捕获异常,保障用例的健壮性
    
    3、单条用例可以独立运行,不要出现耦合
    
    4、灵活使用setup()和teardown()
    
    5、代码出现if else不可怕,但是不要嵌套太多层if else
    
    6、....
    
* **执行用例的命令：**
    
    pytest testcase/ --alluredir ./result/
    
    (start.py文件支持直接在pycharm运行脚本了,单个测试函数运行可以在文件名后面增加::test_xxx)
    
* **生成可视化报告的命令：**

    allure generate ./result/ -o ./report/ --clean

* **查阅报告的命令：**

    allure open -h 127.0.0.1 -p 8083 ./report/
    
* **参考资料**

https://learning-pytest.readthedocs.io/zh/latest/doc/fixture/autouse.html

https://github.com/openatx/uiautomator2#install-an-app

https://blog.csdn.net/liudinglong1989/article/details/83023886
    

* **...**