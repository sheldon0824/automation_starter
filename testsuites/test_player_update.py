import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.cw_login_page import HomePage


class PlayerUpdate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_new_player(self):
        """页面标题验证测试"""
        homepage = HomePage(self.driver)
        print(homepage.get_title())
        homepage.take_window_img()
