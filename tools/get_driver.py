from appium import webdriver


class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 准备启动参数
            caps = {}
            # 必填-且正确
            caps['platformName'] = 'Android'
            # 必填-且正确
            caps['platformVersion'] = '5.1'
            # 必填
            caps['deviceName'] = '192.168.56.101:5555'
            # toast desired_caps[''] = ''
            caps['automationName'] = 'Uiautomator2'
            # 解决中文
            caps['unicodeKeyboard'] = True
            caps['resetKeyboard'] = True
            # APP包名 /
            caps['appPackage'] = 'com.yunmall.lc'
            # 启动名
            caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
            # 获取driver
            cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
