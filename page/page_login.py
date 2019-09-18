from time import sleep

import allure

from base.base import Base
import page
from tools.get_log import GetLog

log = GetLog.get_log()


class PageLogin(Base):
    # 不更新
    @allure.step(title="不更新方法")
    def page_click_x(self):
        self.base_click_func(page.no_update)

    # 点击我
    @allure.step(title="点击我方法")
    def page_click_my(self):
        self.base_click_func(page.login_me)

    # 点击已有账号去登陆
    @allure.step(title="点击已有账号去登陆方法")
    def page_click_exists_user(self):
        self.base_click_func(page.exists_user)

    # 输入用户名
    @allure.step(title="输入用户名方法")
    def page_input_username(self, username):
        self.base_input_func(page.login_username, value=username)

    # 输入密码
    @allure.step(title="输入密码方法")
    def page_input_password(self, password):
        self.base_input_func(page.login_password, value=password)

    # 点击登陆
    @allure.step(title="点击登陆方法")
    def page_click_login_btn(self):
        self.base_click_func(page.login_btn)

    # 获取昵称-》登陆成功使用
    @allure.step(title="获取昵称-》登陆成功使用方法")
    def page_get_nickname(self):
        return self.base_get_text(page.nickname)

    # 点击设置
    @allure.step(title="点击设置方法")
    def page_click_setting(self):
        self.base_click_func(page.setting_btn)

    # 拖拽
    @allure.step(title="拖拽方法")
    def page_drag_and_drop(self):
        self.base_drag_and_drop(page.message_push, page.modify_pwd)

    # 点击退出
    @allure.step(title="点击退出方法")
    def page_click_quit(self):
        self.base_click_func(page.quit_btn)

    # 点击确认
    @allure.step(title="点击确认方法")
    def page_click_sure(self):
        self.base_click_func(page.sure_quit)

    # 获取toast消息-》登陆失败使用
    @allure.step(title="获取toast消息-》登陆失败使用方法")
    def page_get_toast(self, msg):
        return self.base_get_toast(msg)

    # 组合业务方法
    @allure.step(title="登录组合业务方法")
    def page_login(self, username, password):
        log.info("[组合业务方法] 用户名:{} 密码:{}".format(username, password))
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()

    # 正向用例退出方法组合
    @allure.step(title="正向用例退出方法组合方法")
    def page_login_quit(self):
        log.info("正向用例退出业务方法")
        self.page_click_setting()
        self.page_drag_and_drop()
        self.page_click_quit()
        self.page_click_sure()

    # 组合业务方法
    @allure.step(title="登录组合业务方法")
    def page_login_address(self, username="15190488353", password="123456"):
        log.info("[组合业务方法] 用户名:{} 密码:{}".format(username, password))
        # 点击我
        self.page_click_my()
        # 点击已有账号登录
        self.page_click_exists_user()
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
        sleep(3)
        # 点击设置
        self.page_click_setting()

