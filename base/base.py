from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tools.get_driver import GetDriver
from tools.get_log import GetLog
import allure

log = GetLog.get_log()


class Base:
    # 初始化driver
    @allure.step(title="初始化驱动对象")
    def __init__(self):
        allure.attach("获取driver对象:", "{}".format(GetDriver.get_driver()))
        log.info("获取driver对象{}".format(GetDriver.get_driver()))
        self.driver = GetDriver.get_driver()

    # 定位元素
    @allure.step(title="定位元素操作")
    def base_find_element(self, loc, timeout=10, poll=0.5):
        allure.attach("查找的元素:", "{}".format(loc))
        log.info("正在查找元素:{} 超时时间:{} 访问评率:{}".format(loc, timeout, poll))
        return (WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
                .until(lambda x: x.find_element(*loc)))

    # 定位一组元素
    @allure.step(title="定位一组元素操作")
    def base_find_elements(self, loc, timeout=10, poll=0.5):
        allure.attach("查找的一组元素:", "{}".format(loc))
        log.info("正在查找一组元素:{} 超时时间:{} 访问评率:{}".format(loc, timeout, poll))
        return (WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
                .until(lambda x: x.find_elements(*loc)))

    # 点击定位一组元素
    @allure.step(title="定位一组元素点击元素操作")
    def base_click(self, loc, num):
        allure.attach("点击的元素:", "{}".format(loc))
        log.info("点击元素:{}".format(loc))
        elements = self.base_find_elements(loc)
        elements[num].click()

    # 点击
    @allure.step(title="点击元素操作")
    def base_click_func(self, loc):
        allure.attach("点击的元素:", "{}".format(loc))
        log.info("点击元素:{}".format(loc))
        element = self.base_find_element(loc)
        element.click()

    # 输入
    @allure.step(title="输入的操作")
    def base_input_func(self, loc, value):
        allure.attach("向{}元素输入".format(loc), "输入的内容".format(value))
        log.info("向{}元素输入".format(loc), "输入的内容".format(value))
        element = self.base_find_element(loc)
        element.clear()
        element.send_keys(value)

    # 获取元素文本
    @allure.step(title="获取元素文本操作")
    def base_get_text(self, loc):
        allure.attach("获取元素文本", "{}".format(loc))
        log.info("获取元素文本{}".format(loc))
        return self.base_find_element(loc).text

    # 获取toast消息
    @allure.step(title="获取toast消息操作")
    def base_get_toast(self, msg):
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(msg)
        allure.attach(
            "获取{}元素toast消息".format(self.base_find_element(loc), "值为{}".format(self.base_find_element(loc).text)))
        log.info("获取{}元素toast消息".format(loc))
        return self.base_find_element(loc, timeout=5, poll=0.2).text

    # 拖拽
    @allure.step(title="拖拽操作")
    def base_drag_and_drop(self, loc1, loc2):
        start_el = self.base_find_element(loc1)
        end_el = self.base_find_element(loc2)
        self.driver.drag_and_drop(start_el, end_el)

    # 轻敲
    @allure.step(title="轻敲元素操作")
    def base_tap(self, loc):
        action = TouchAction(self.driver)
        action.tap(self.base_find_element(loc))
        action.perform()

    @allure.step(title="以坐标轻敲元素操作")
    def base_tap_xy(self, x, y):
        allure.attach("x={}".format(x), "y={}".format(y))
        log.info("应用坐标点击元素, x={}, y={}".format(x, y))
        action = TouchAction(self.driver)
        action.tap(element=None, x=x, y=y)
        action.perform()

    @allure.step(title="以文本点击元素操作")
    def base_click_text(self, text):
        loc = By.XPATH, "//*[contains(@text, '{}')]".format(text)
        self.base_click_func(loc)

    @allure.step(title="获取一组以文本点击元素操作")
    def base_texts_click(self, text, num=0):
        loc = By.XPATH, "//*[contains(@text, '{}')]".format(text)
        self.base_click_func(self.base_find_elements(loc)[num])

    # 获取一组元素的文本
    def base_get_list_text(self, loc):
        return [element.text for element in self.base_find_elements(loc)]
