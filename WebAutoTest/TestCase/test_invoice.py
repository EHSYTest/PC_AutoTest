import sys
sys.path.append('../Page')
import time
import unittest
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
from Page_MiniCart import MiniCart
from Page_NormalCart import NormalCart
from selenium.webdriver.common.action_chains import ActionChains


class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = Page(self.driver)
        self.environment = self.page.config_reader('environment.conf', 'Environment', 'environment')
        if self.environment == 'staging':
            self.driver.get('http://ps.ehsy.com')
        elif self.environment == 'production':
            self.driver.get('http://www.ehsy.com')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.cart = Cart(self.driver)
        self.home = Home(self.driver)
        self.order = Order(self.driver)
        self.order_result = OrderResult(self.driver)
        self.product_list = ProductList(self.driver)
        self.quick_order = QuickOrder(self.driver)
        self.report_order = ReportOrder(self.driver)
        self.mini_cart = MiniCart(self.driver)
        self.normal_cart = NormalCart(self.driver)

    def test_invoice(self):
        """发票信息增删改"""
        login_name = self.page.config_reader('test_order.conf', '发票地址账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '发票地址账号', 'password')
        self.home.login(login_name, password)
        ActionChains(self.driver).move_to_element(self.cart.element_find(self.product_list.cart)).perform()
        self.product_list.element_find(self.product_list.go_cart).click()
        self.cart.element_find(self.cart.go_to_order).click()
        self.order.invoice_normal_personal_add()
        self.order.element_find(self.order.close).click()
        self.order.invoice_normal_personal_edit()
        self.order.element_find(self.order.close).click()
        self.order.invoice_normal_delete()
        self.order.element_find(self.order.close).click()
        self.order.invoice_normal_company_add()
        self.order.element_find(self.order.close).click()
        self.order.invoice_normal_company_edit()
        self.order.element_find(self.order.close).click()
        self.order.invoice_normal_delete()
        self.order.element_find(self.order.close).click()
        self.order.invoice_vat_add()
        self.order.element_find(self.order.close).click()
        self.order.invoice_vat_delete()
        self.order.element_find(self.order.close).click()

    def test_address(self):
        """收货地址增删改"""
        login_name = self.page.config_reader('test_order.conf', '发票地址账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '发票地址账号', 'password')
        self.home.login(login_name, password)
        ActionChains(self.driver).move_to_element(self.cart.element_find(self.product_list.cart)).perform()
        self.product_list.element_find(self.product_list.go_cart).click()
        self.cart.element_find(self.cart.go_to_order).click()
        self.order.add_receiving_address()
        self.order.receiving_address_edit()
        self.order.receiving_address_delete()

    # def test_invoice_check(self):
    #     """发票信息填写校验-普票"""
    #     login_name = self.page.config_reader('test_order.conf', '发票地址账号', 'login_name')
    #     password = self.page.config_reader('test_order.conf', '发票地址账号', 'password')
    #     self.home.login(login_name, password)
    #     ActionChains(self.driver).move_to_element(self.cart.element_find(self.product_list.cart)).perform()
    #     self.product_list.element_find(self.product_list.go_cart).click()
    #     self.cart.element_find(self.cart.go_to_order).click()
    #     self.order.normal_invoice_check()

    def tearDown(self):
        test_method_name = self._testMethodName
        self.driver.save_screenshot("../TestResult/ScreenShot/%s.png" % test_method_name)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
