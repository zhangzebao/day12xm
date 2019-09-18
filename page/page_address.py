from time import sleep

import allure

import page
from base.base import Base


class PageAddress(Base):
    # 点击设置
    @allure.step(title="点击设置方法")
    def page_click_setting_func(self):
        self.base_click_func(page.setting_btn)

    # 点击地址管理
    @allure.step(title="点击地址管理方法")
    def page_click_address_menage(self):
        self.base_tap(page.address_menage)  # 轻敲

    # 点击新增地址
    @allure.step(title="点击新增地址方法")
    def page_click_address_add(self):
        self.base_click_func(page.add_address)

    # 输入收件人
    @allure.step(title="输入收件人方法")
    def page_input_receipt_name(self, receipt):
        self.base_input_func(page.receipt_name, receipt)

    # 输入手机号
    @allure.step(title="输入手机号方法")
    def page_input_address_phone(self, phone):
        self.base_input_func(page.address_phone, phone)

    # 点击所在地区
    @allure.step(title="新增地址点击所在地区")
    def page_click_address_province(self):
        self.base_click_func(page.address_province)

    @allure.step(title="修改地址点击新增地址方法")
    def page_tap_province(self):
        self.base_tap(page.address_province)

    # 点击北京市(两次)
    @allure.step(title="第一次点击北京市方法")
    def page_click_address_beijing(self):
        self.base_click_func(page.address_beijing)

    @allure.step(title="第二次点击北京市方法")
    def page_click_double_beijing(self):
        # self.base_tap(page.address_beijing)
        self.base_click(page.address_beijing, 1)
        # self.base_click_func(page.double_beijing)

    # 点击昌平区
    @allure.step(title="点击昌平区方法")
    def page_click_address_chang_ping(self):
        self.base_click_func(page.address_chang_ping)

    # 输入详细地址
    @allure.step(title="输入详细地址方法")
    def page_input_address_detail(self, address):
        self.base_input_func(page.address_detail, address)

    # 输入邮编
    @allure.step(title="输入邮编方法")
    def page_input_address_post(self, code):
        self.base_input_func(page.address_post, code)

    # 点击设为默认地址
    @allure.step(title="点击设为默认地址方法")
    def page_click_address_default(self):
        self.base_click_func(page.address_default)

    # 点击保存
    @allure.step(title="点击保存方法")
    def page_click_address_send(self):
        self.base_click_func(page.address_send)

    # 点击编辑
    @allure.step(title="点击编辑方法")
    def page_click_address_edit(self):
        self.base_click_func(page.address_edit)

    # 点击修改
    @allure.step(title="点击修改方法")
    def page_click_address_modify(self):
        self.base_tap_xy(x=1085, y=428)
        # self.base_texts_click(text="修改")

    # 点击上海
    @allure.step(title="第一次用元素点击上海方法")
    def page_click_address_shanghai(self):
        self.base_click_func(page.address_shanghai)

    @allure.step(title="第二次用坐标点击上海方法")
    def page_click_double_shanghai(self):
        # self.base_tap_xy(x=500, y=300)
        self.base_click(page.address_shanghai, 1)

    # 点击长宁区
    @allure.step(title="点击长宁区方法")
    def page_click_address_chang_ing(self):
        self.base_click_func(page.address_chang_ing)

    # 点击删除
    @allure.step(title="点击删除方法")
    def page_click_delete(self):
        self.base_tap_xy(x=1359, y=383)
        # self.base_texts_click(text="删除")

    # 点击确认删除
    @allure.step(title="点击确认删除方法")
    def page_click_sure_delete(self):
        self.base_click_func(page.sure_delete_address)

    # 点击所在地区组合业务方法(不适合直辖市 适合 省 市 区)
    def page_address(self, province, city, area):
        # 点击所在地区
        self.base_click_func(page.address_province)
        # 点击省
        self.base_click_text(province)
        # 点击市
        self.base_click_text(city)
        # 点击区
        self.base_click_text(area)

    # 获取所有地址列表收件人 电话方法
    def page_name_phone_list(self):
        return self.base_get_list_text(page.add_name_phone)

    # 新增地址组合业务方法
    @allure.step(title="新增地址组合业务方法")
    def page_add_address(self, receipt, phone, address, code,  province, city, area):
        self.page_click_address_menage()
        self.page_click_address_add()
        self.page_input_receipt_name(receipt)
        self.page_input_address_phone(phone)
        self.page_address(province, city, area)  # 所在地区组合业务方法
        # self.page_click_address_province()
        # self.page_click_address_beijing()
        # sleep(3)
        # self.page_click_double_beijing()
        self.page_click_address_chang_ping()
        self.page_input_address_detail(address)
        self.page_input_address_post(code)
        self.page_click_address_default()
        self.page_click_address_send()

    # 修改地址组合业务方法
    @allure.step(title="修改地址组合业务方法")
    def page_update_address(self, receipt, phone, address, code, province, city, area):
        self.page_click_address_edit()
        self.page_click_address_modify()
        self.page_input_receipt_name(receipt)
        self.page_input_address_phone(phone)
        self.page_address(province, city, area)
        # self.page_tap_province()
        # self.page_click_address_shanghai()
        # sleep(3)  # 必须加等待不加定位不到
        # self.page_click_double_shanghai()
        # self.page_click_address_chang_ing()
        self.page_input_address_detail(address)
        self.page_input_address_post(code)
        self.page_click_address_send()

    # 删除一个地址组合业务方法
    @allure.step(title="删除地址组合业务方法")
    def page_delete_address(self):
        self.page_click_address_edit()
        sleep(3)  # 必须加等待不加会点错
        self.page_click_delete()
        self.page_click_sure_delete()

    # 删除所有地址组合业务方法
    @allure.step(title="删除所有地址组合业务方法")
    def page_delete_all_address(self):
        list_text = self.base_get_list_text(page.add_name_phone)
        for i in range(len(list_text)):
            self.page_delete_address()

    # 判断地址是否被删除所有
    @allure.step(title="判断地址是否被删除所有方法")
    def page_address_is_exists(self):
        try:
            self.base_find_elements(page.address_delete)
            return False
        except:
            return True
