"""
公共方法类:
    封装正向逆向断言方法
"""
import allure
from config import BASE_PATH
from page.page_in import PageIn
from page.page_login import PageLogin
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_log()


class Until:
    def __init__(self):
        self.login = PageIn.get_page_login()
        self.driver = GetDriver.get_driver()
        self.page_login = PageLogin()

    def assert_nickname(self, expect):
        """断言昵称"""
        try:
            assert self.login.page_get_nickname() == expect
        except AssertionError as f:
            self.driver.get_screenshot_as_file(BASE_PATH + "/img/bug_.png")
            with open(BASE_PATH + "/img/bug_.png", "rb") as f:
                allure.attach("失败原因", f.read(), allure.attach_type.PNG)
                log.error(f)
            raise
        finally:
            self.page_login.page_login_quit()
            self.page_login.page_click_my()
            self.page_login.page_click_exists_user()

    def assert_toast(self, expect):
        """断言toast消息"""
        try:
            assert self.login.page_get_toast(expect) == expect
        except AssertionError as f:
            self.driver.get_screenshot_as_file(BASE_PATH + "/img/bug_.png")
            with open(BASE_PATH + "/img/bug_.png", "rb") as e:
                allure.attach("失败原因", e.read(), allure.attach_type.PNG)
                log.error(e)
            raise

    def screen_shot(self):
        """截图并把图片写入报告"""
        self.driver.get_screenshot_as_file(BASE_PATH + "/img/bug_.png")
        with open(BASE_PATH + "/img/bug_.png", "rb") as f:
            allure.attach("失败原因", f.read(), allure.attach_type.PNG)
            log.error(f)

