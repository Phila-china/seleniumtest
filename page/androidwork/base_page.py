
from appium import webdriver

class BasePage:

    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps['appPackage'] = 'com.android.deskclock'
        caps['appActivity'] = 'com.android.deskclock.DeskClock'
        # 当界面不停变化的时候，不要等界面处于空闲状态
        caps['settings[waitForIdleTimeout]'] = 0
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def close(self):
        self.driver.quit()