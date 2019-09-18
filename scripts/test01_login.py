import sys
import os

sys.path.append(os.getcwd())
from tools.until import Until
import pytest
from page.page_in import PageIn
from tools.get_driver import GetDriver


def build_data():
    data = []
    for i in PageIn.read_data().values():
        data.append((i.get("username"),
                     i.get("password"),
                     i.get("success"),
                     i.get("expect")))
    return data


class TestLogin:

    def setup_class(self):
        # 初始化业务对象
        self.login = PageIn.get_page_login()
        # 不更新
        self.login.page_click_x()
        # 点击我
        self.login.page_click_my()
        # 点击已有账号去登陆
        self.login.page_click_exists_user()

    def teardown_class(self):
        # 关闭浏览器驱动对象
        GetDriver.quit_driver()

    @pytest.mark.parametrize("username, password, success, expect", build_data())
    def test_login(self, username, password, success, expect):
        # 登录方法
        self.login.page_login(username, password)
        if success:
            # 断言昵称
            print("昵称", self.login.page_get_nickname())
            Until().assert_nickname(expect)


        else:
            # 断言toast
            print("toast信息", self.login.page_get_toast(expect))
            Until().assert_toast(expect)
