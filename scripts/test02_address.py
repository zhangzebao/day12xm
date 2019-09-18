import sys
import os

from tools.until import Until

sys.path.append(os.getcwd())
from tools.read_data import read_data
from page.page_in import PageIn
from tools.get_driver import GetDriver
import pytest


def build_data(key):
    data1 = []
    data1.append(tuple(read_data("address.yaml").get(key).values()))
    return data1


class TestAddress:
    def setup_class(self):
        self.page_login = PageIn.get_page_login()
        self.page_address = PageIn.get_page_address()
        # 点击不更新
        self.page_login.page_click_x()
        # 登录方法
        self.page_login.page_login_address()

    def teardown_class(self):
        GetDriver.quit_driver()

    @pytest.mark.parametrize("receipt, phone, address, code, province, city, area", build_data("add_address"))
    def test01_address(self, receipt, phone, address, code, province, city, area):
        # 新增地址
        self.page_address.page_add_address(receipt, phone, address, code, province, city, area)

        print("新增收件人 电话{}, 所有收件人 电话列表{}".format(receipt + "  " + phone, self.page_address.page_name_phone_list()))
        try:
            assert receipt + "  " + phone in self.page_address.page_name_phone_list()
        except AssertionError as e:
            Until().screen_shot()
            raise e

    @pytest.mark.parametrize("receipt, phone, address, code, province, city, area", build_data("add_address"))
    def test02_update_address(self, receipt, phone, address, code, province, city, area):
        # 修改地址
        self.page_address.page_update_address(receipt, phone, address, code, province, city, area)
        print("修改的收件人 电话{}, 所有收件人 电话列表{}".format(receipt + "  " + phone, self.page_address.page_name_phone_list()))
        try:
            assert receipt + "  " + phone in self.page_address.page_name_phone_list()
        except AssertionError as e:
            Until().screen_shot()
            raise e

    def test03_delete_address(self):
        # 删除地址
        self.page_address.page_delete_all_address()
        try:
            assert self.page_address.page_address_is_exists()
        except AssertionError as e:
            Until().screen_shot()
            raise e
