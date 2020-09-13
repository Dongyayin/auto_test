import allure
import os


@allure.feature("截图测试用例")
class TestScreenCap:
    @allure.step("截图写入报告")
    def test_screencap(self):
        # os.open("adb exec-out screencap -p > 1.png")
        os.system('adb exec-out screencap -p > 1.png')
        with open("./1.png", "rb")as f:
            allure.attach(f.read(), "执行截图", attachment_type=allure.attachment_type.PNG)


