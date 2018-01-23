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
            self.driver.get('http://new.ehsy.com')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.home = Home(self.driver)
        self.page = Page(self.driver)
        self.user_address = UserAddress(self.driver)

    def test_address_personal(self):
        loginname = self.page.config_reader('test_order.conf', '个人地址发票账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '个人地址发票账号', 'password')
        self.home.login(loginname, password)
        self.home.go_user_center()
        self.page.wait_click(self.user_address.my_address)
        ###通用地址###
        self.user_address.add_currency_address()
        self.user_address.edit_currency_address()
        self.user_address.set_default_currency_address()
        self.user_address.delete_currency_address()
        ###收货地址###
        self.user_address.add_receive_address()
        self.user_address.edit_receive_address()
        self.user_address.set_default_receive_address()
        self.user_address.delete_receive_address()
        ###发票地址###
        self.user_address.add_invoice_address()
        self.user_address.edit_invoice_address()
        self.user_address.set_default_invoice_address()
        self.user_address.delete_invoice_address()

    def test_address_company_distribution(self):
        loginname = self.page.config_reader('test_order.conf', '分销地址发票账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '分销地址发票账号', 'password')
        self.home.login(loginname, password)
        self.home.go_user_center()
        self.page.wait_click(self.user_address.my_address)
        ###通用地址###
        self.user_address.add_currency_address()
        self.user_address.edit_currency_address()
        self.user_address.set_default_currency_address()
        self.user_address.delete_currency_address()
        ###收货地址###
        self.user_address.add_receive_address()
        self.user_address.edit_receive_address()
        self.user_address.set_default_receive_address()
        self.user_address.delete_receive_address()
        ###发票地址###
        self.user_address.add_invoice_address()
        self.user_address.edit_invoice_address()
        self.user_address.set_default_invoice_address()
        self.user_address.delete_invoice_address()

    def test_address_company_terminal(self):
        loginname = self.page.config_reader('test_order.conf', '终端地址发票账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '终端地址发票账号', 'password')
        self.home.login(loginname, password)
        self.home.go_user_center()
        self.page.wait_click(self.user_address.my_address)
        ###通用地址###
        self.user_address.add_currency_address()
        self.user_address.edit_currency_address()
        self.user_address.set_default_currency_address()
        self.user_address.delete_currency_address()
        ###收货地址###
        self.user_address.add_receive_address()
        self.user_address.edit_receive_address()
        self.user_address.set_default_receive_address()
        self.user_address.delete_receive_address()
        ###发票地址###
        self.user_address.add_invoice_address()
        self.user_address.edit_invoice_address()
        self.user_address.set_default_invoice_address()
        self.user_address.delete_invoice_address()

    def tearDown(self):
        test_method_name = self._testMethodName
        self.driver.save_screenshot('../TestResult/ScreenShot/%s.png' % test_method_name)
        self.driver.quit()

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestUserAddress('test_address_company_terminal'))
    file = open('../TestResult/EHSY_AutoTest.html', 'wb')
    runner = HTMLTestRunner(stream=file, title='用户地址测试报告', description='测试情况')
    runner.run(suite)
    file.close()

