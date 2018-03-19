import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from Page_Base import Page
from Page_Home import Home
from Page_UserInvoice import UserInvoice
import pytest, allure


@allure.feature('个人中心-用户发票测试')
@pytest.allure.severity(pytest.allure.severity_level.MINOR)
class TestUserInvoice(unittest.TestCase):
    def setup_method(self, method):
        with allure.step('---Start---'):
            self.driver = webdriver.Chrome()
            self.page = Page(self.driver)
            self.environment = self.page.config_reader('environment.conf', 'Environment', 'environment')
            if self.environment == 'staging':
                self.url = 'http://ps.ehsy.com'
                self.driver.get(self.url)
            else:
                self.url = 'http://www.ehsy.com'
                self.driver.get(self.url)
            self.driver.implicitly_wait(30)
            self.driver.maximize_window()
            self.home = Home(self.driver)
            self.user_invoice = UserInvoice(self.driver)
            allure.attach('初始化参数:', 'environment: ' + self.environment + '\nurl: ' + self.url + '\n')

    @allure.story('个人发票测试')
    def test_invoice_personal(self):
        with allure.step('读取账号配置信息'):
            loginname = self.page.config_reader('test_order.conf', '个人地址发票账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '个人地址发票账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (loginname, password))
        self.home.login(loginname, password)
        self.home.go_user_center()
        self.user_invoice.wait_click(self.user_invoice.my_invoice)
        # 公司类型的发票
        with allure.step('公司发票测试'):
            self.user_invoice.add_company_invoice()
            self.user_invoice.edit_company_invoice()
            self.user_invoice.company_change_personal()
            self.user_invoice.set_default_invoice()
            self.user_invoice.delete_invoice()
        # 个人类型发票
        with allure.step('个人发票测试'):
            self.user_invoice.add_personal_invoice()
            self.user_invoice.edit_personal_invoice()
            self.user_invoice.personal_change_company()
            self.user_invoice.set_default_invoice()
            self.user_invoice.delete_invoice()
        # 增值税发票
        with allure.step('增票测试'):
            self.user_invoice.add_receipt_invoice()
            self.user_invoice.edit_receipt_invoice()
            self.user_invoice.set_default_receipt_invoice()
            self.user_invoice.delete_invoice()

    @allure.story('分销发票测试')
    def test_invoice_company_distribution(self):
        with allure.step('读取账号配置信息'):
            loginname = self.page.config_reader('test_order.conf', '分销地址发票账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '分销地址发票账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (loginname, password))
        self.home.login(loginname, password)
        self.home.go_user_center()
        self.user_invoice.wait_click(self.user_invoice.my_invoice)
        # 公司类型的发票
        with allure.step('公司发票测试'):
            self.user_invoice.add_company_invoice()
            self.user_invoice.edit_company_invoice()
            self.user_invoice.company_change_personal()
            self.user_invoice.set_default_invoice()
            self.user_invoice.delete_invoice()
        # 个人类型发票
        with allure.step('个人发票测试'):
            self.user_invoice.add_personal_invoice()
            self.user_invoice.edit_personal_invoice()
            self.user_invoice.personal_change_company()
            self.user_invoice.set_default_invoice()
            self.user_invoice.delete_invoice()
        # 增值税发票
        with allure.step('增票测试'):
            self.user_invoice.add_receipt_invoice()
            self.user_invoice.edit_receipt_invoice()
            self.user_invoice.set_default_receipt_invoice()
            self.user_invoice.delete_invoice()

    @allure.story('终端发票测试')
    def test_invoice_company_terminal(self):
        with allure.step('读取账号配置信息'):
            loginname = self.page.config_reader('test_order.conf', '终端地址发票账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '终端地址发票账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (loginname, password))
        self.home.login(loginname, password)
        self.home.go_user_center()
        self.user_invoice.wait_click(self.user_invoice.my_invoice)
        # 公司类型的发票
        with allure.step('公司发票测试'):
            self.user_invoice.add_company_invoice()
            self.user_invoice.edit_company_invoice()
            self.user_invoice.company_change_personal()
            self.user_invoice.set_default_invoice()
            self.user_invoice.delete_invoice()
        # 个人类型发票
        with allure.step('个人发票测试'):
            self.user_invoice.add_personal_invoice()
            self.user_invoice.edit_personal_invoice()
            self.user_invoice.personal_change_company()
            self.user_invoice.set_default_invoice()
            self.user_invoice.delete_invoice()
        # 增值税发票
        with allure.step('增票测试'):
            self.user_invoice.add_receipt_invoice()
            self.user_invoice.edit_receipt_invoice()
            self.user_invoice.set_default_receipt_invoice()
            self.user_invoice.delete_invoice()

    def teardown_method(self, method):
        test_method_name = self._testMethodName
        with allure.step('保存截图'):
            self.driver.save_screenshot('../TestResult/ScreenShot/%s.png' % test_method_name)
            f = open('../TestResult/ScreenShot/%s.png' % test_method_name, 'rb').read()
            allure.attach('自动化截图', f, allure.attach_type.PNG)
        with allure.step('---End---'):
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(TestUserInvoice('test_invoice_personal'))
    # file = open('../TestResult/EHSY_AutoTest.html', 'wb')
    # runner = HTMLTestRunner(stream=file, title='用户地址测试报告', description='测试情况')
    # runner.run(suite)
    # file.close()
