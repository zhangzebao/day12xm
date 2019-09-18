from page.page_address import PageAddress
from page.page_login import PageLogin
from tools.read_data import read_data


class PageIn:
    # 获取登录page页面对象
    @classmethod
    def get_page_login(cls):
        return PageLogin()

    @classmethod
    def read_data(cls):
        return read_data("data.yaml")

    @classmethod
    def get_page_address(cls):
        return PageAddress()
