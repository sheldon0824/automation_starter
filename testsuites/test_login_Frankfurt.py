import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.cw_login_page import LoginPage


class Login(unittest.TestCase):
    """Cloudweb 登录测试"""
    @classmethod  # 用于同一个类下多个test()时，只执行一次setUp()和tearDown()
    def setUpClass(cls):
        """
        写【测试固件】时，需要的套件之一，setUp()主要为测试固件开始时的前期准备
        :return:
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        写【测试固件】时，需要的套件之一，tearDown()是指测试结束时候的操作，一般是指关闭浏览器啦
        :return:
        """
        cls.driver.quit()

    def test_login_overseas(self):
        """登录法兰克福数据中心"""
        loginpage = LoginPage(self.driver)
        loginpage.type_frankfurt_account('euproqa5', 'admin123')
        loginpage.send_submit_btn()
        time.sleep(5)
        loginpage.take_window_img()

        if loginpage.login_account_name() == 'BeastLaLo':
            print("Login to Frankfurt data center successfully!")
        else:
            print("Failed on login to Frankfurt data center!")

    def test_logout(self):
        """用户登出"""
        loginpage = LoginPage(self.driver)
        loginpage.logout()
        loginpage.take_window_img()


if __name__ == '__main__':
    unittest.main()

