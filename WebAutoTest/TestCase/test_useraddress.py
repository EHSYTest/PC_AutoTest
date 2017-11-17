import sys
sys.path.append('../Page')
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from Page_Base import Page
from Page_Home import Home
from Page_UserAddress import UserAddress


class TestUserAddress(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = Page(self.driver)
        self.environment = self.page.config_reader('environment.conf', 'Environment', 'environment')
        if self.environment == 'staging':
            self.driver.get('http://ps.ehsy.com')
        else:
            self.driver.get('http://http://www.ehsy.com')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.home = Home(self.driver)
        self.user_address = UserAddress(self.driver)

    def test_receive_address(self):
        loginname = self.page.config_reader('test_order.conf', '个人账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '个人账号', 'password')
        self.home.login(loginname, password)
        self.home.go_user_center()
        self.page.wait_to_stale(self.user_address.layer)
        self.user_address.element_find(self.user_address.my_address).click()
        self.page.wait_to_stale(self.user_address.layer)
        self.user_address.add_receive_address()

    def tearDown(self):
        test_method_name = self._testMethodName
        self.driver.save_screenshot('../TestResult/ScreenShot/%s.png' % test_method_name)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(TestUserAddress('test_receive_address'))
    # file = open('../TestResult/order.html', 'wb')
    # runner = HTMLTestRunner(stream=file, title='WWW下单——测试报告', description='测试情况')
    # runner.run(suite)
    # file.close()

