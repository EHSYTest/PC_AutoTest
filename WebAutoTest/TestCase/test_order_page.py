import sys
sys.path.append('../Page')
import time
import unittest, sys
sys.path.append('../Page')
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from Page_Base import Page
from Page_Cart import Cart
from Page_Home import Home
from Page_Order import Order
from Page_OrderResult import OrderResult
from Page_ProductList import ProductList
from Page_QuickOrder import QuickOrder
from Page_ReportOrder import ReportOrder
from selenium.webdriver.common.action_chains import ActionChains
import allure, pytest


@allure.feature('下单页-发票地址测试')
@pytest.allure.severity(pytest.allure.severity_level.MINOR)
class TestOrderPage(unittest.TestCase):

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
            self.cart = Cart(self.driver)
            self.home = Home(self.driver)
            self.order = Order(self.driver)
            self.order_result = OrderResult(self.driver)
            self.product_list = ProductList(self.driver)
            self.quick_order = QuickOrder(self.driver)
            self.report_order = ReportOrder(self.driver)
            allure.attach('初始化参数:', 'environment: ' + self.environment + '\nurl: ' + self.url + '\n')

    @allure.story('个人-发票信息增删改')
    def test_invoice_1(self):
        """发票信息增删改-个人"""
        # allure.environment(Report='TestOrderPage Report', Browser='Chrome 63', URL=self.url)
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '个人地址发票账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '个人地址发票账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        with allure.step('进入购物车页面'):
            self.home.search_sku()
            self.product_list.searchResult_add_to_cart()
        with allure.step('进入订单提交页'):
            self.cart.wait_click(self.cart.go_to_order)
        self.order.invoice_normal_personal_add()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_normal_personal_edit()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_normal_delete()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_normal_company_add()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_normal_company_edit()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_normal_delete()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_vat_add()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_vat_edit()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_vat_delete()
        self.order.wait_click(self.order.confirm)

    @allure.story('分销-发票信息增删改')
    def test_invoice_2(self):
        """发票信息增删改-分销"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '分销地址发票账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '分销地址发票账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        with allure.step('进入购物车页面'):
            self.home.search_sku()
            self.product_list.searchResult_add_to_cart()
        with allure.step('进入订单提交页'):
            self.cart.wait_click(self.cart.go_to_order)
        self.order.invoice_normal_personal_add()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_normal_personal_edit()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_normal_delete()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_normal_company_add()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_normal_company_edit()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_normal_delete()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_vat_add()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_vat_edit()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_vat_delete()
        self.order.wait_click(self.order.confirm)

    @allure.story('终端-发票信息增删改')
    def test_invoice_3(self):
        """发票信息增删改-终端"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '终端地址发票账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '终端地址发票账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        with allure.step('进入购物车页面'):
            self.home.search_sku()
            self.product_list.searchResult_add_to_cart()
        with allure.step('进入订单提交页'):
            self.cart.wait_click(self.cart.go_to_order)
        self.order.invoice_normal_personal_add()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_normal_personal_edit()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_normal_delete()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_normal_company_add()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_normal_company_edit()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_normal_delete()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_vat_add()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_vat_edit()
        self.order.wait_click(self.order.confirm)
        self.order.invoice_vat_delete()
        self.order.wait_click(self.order.confirm)

    @allure.story('个人-收货地址增删改')
    def test_address_1(self):
        """收货地址增删改-个人"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '个人地址发票账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '个人地址发票账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        with allure.step('进入购物车页面'):
            self.home.search_sku()
            self.product_list.searchResult_add_to_cart()
        with allure.step('进入订单提交页'):
            self.cart.wait_click(self.cart.go_to_order)
        self.order.add_receiving_address()
        self.order.receiving_address_edit()
        self.order.receiving_address_delete()

    @allure.story('分销-收货地址增删改')
    def test_address_2(self):
        """收货地址增删改-分销"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '分销地址发票账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '分销地址发票账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        with allure.step('进入购物车页面'):
            self.home.search_sku()
            self.product_list.searchResult_add_to_cart()
        with allure.step('进入订单提交页'):
            self.cart.wait_click(self.cart.go_to_order)
        self.order.add_receiving_address()
        self.order.receiving_address_edit()
        self.order.receiving_address_delete()

    @allure.story('终端-收货地址增删改')
    def test_address_3(self):
        """收货地址增删改-终端"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '终端地址发票账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '终端地址发票账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        with allure.step('进入购物车页面'):
            self.home.search_sku()
            self.product_list.searchResult_add_to_cart()
        with allure.step('进入订单提交页'):
            self.cart.wait_click(self.cart.go_to_order)
        self.order.add_receiving_address()
        self.order.receiving_address_edit()
        self.order.receiving_address_delete()

    @allure.story('发票信息填写校验')
    def test_invoice_check(self):
        """发票信息填写校验"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '个人地址发票账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '个人地址发票账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        with allure.step('进入购物车页面'):
            self.home.search_sku()
            self.product_list.searchResult_add_to_cart()
        with allure.step('进入订单提交页'):
            self.cart.wait_click(self.cart.go_to_order)
        self.order.normal_invoice_check()
        self.order.wait_click(self.order.confirm)
        self.order.vat_invoice_check()

    @allure.story('收货地址信息填写校验')
    def test_address_check(self):
        """收货地址信息填写校验"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '个人地址发票账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '个人地址发票账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        with allure.step('进入购物车页面'):
            self.home.search_sku()
            self.product_list.searchResult_add_to_cart()
        with allure.step('进入订单提交页'):
            self.cart.wait_click(self.cart.go_to_order)
        self.order.receiving_address_check()

    def teardown_method(self, method):
        self.order.check_no_address()
        test_method_name = self._testMethodName
        with allure.step('保存截图'):
            self.driver.save_screenshot('../TestResult/ScreenShot/%s.png' % test_method_name)
            f = open('../TestResult/ScreenShot/%s.png' % test_method_name, 'rb').read()
            allure.attach('自动化截图', f, allure.attach_type.PNG)
        with allure.step('---End---'):
            self.driver.quit()


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTests([TestOrderPage('test_address_1')])
    file = open('../TestResult/EHSY_AutoTest.html', 'wb')
    runner = HTMLTestRunner(stream=file, title='WWW下单——测试报告', description='测试情况')
    runner.run(suite)
    file.close()
