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
from selenium.webdriver.common.action_chains import ActionChains


class TestOrderPage(unittest.TestCase):

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

    def test_invoice_1(self):
        """个人"""
        login_name = self.page.config_reader('test_price.conf', '个人', 'login_name')
        password = self.page.config_reader('test_price.conf', '个人', 'password')
        product = self.page.config_reader('data.conf', 'price_product', 'product')
        price = self.page.config_reader('data.conf', 'price_product', 'price')
        self.home.login(login_name, password)
        self.home.search_sku(product)
        price_assert = self.product_list.element_find(self.product_list.unit_price).text
        print(price_assert)
        assert price in price_assert
        self.page.wait_click(self.product_list.sku_result_click)
        self.page.switch_to_new_window()
        price_assert = self.product_list.element_find(self.product_list.price).text
        print(price_assert)
        assert price in price_assert
        self.product_list.wait_click(self.product_list.skuContent_add_button)
        ActionChains(self.driver).move_to_element(self.product_list.element_find(self.product_list.cart)).perform()
        self.product_list.wait_click(self.product_list.go_cart)
        price_assert = self.cart.element_find(self.cart.unit_price).text
        print(price_assert)
        assert price in price_assert

    def tearDown(self):
        test_method_name = self._testMethodName
        self.driver.save_screenshot("../TestResult/ScreenShot/%s.png" % test_method_name)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(TestCase('test_invoice'))
    # suite.addTest(TestCase('test_address'))
    # file = open('../TestResult/order.html', 'wb')
    # runner = HTMLTestRunner(stream=file, title='WWW下单——测试报告', description='测试情况')
    # runner.run(suite)
    # file.close()
