import sys
sys.path.append('../Page')
from HTMLTestRunner import HTMLTestRunner
import unittest, time
from selenium import webdriver
from Page_Base import Page
from Page_Cart import Cart
from Page_Home import Home
from Page_Order import Order
from Page_OrderResult import OrderResult
from Page_ProductList import ProductList
from Page_QuickOrder import QuickOrder
from Page_ReportOrder import ReportOrder
from selenium.webdriver.common.action_chains import ActionChains
from Page_Base import AssistFunction


class PowerChinaOrder(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)
        self.page = Page(self.driver)
        self.environment = self.page.config_reader('environment.conf', 'Environment', 'environment')
        if self.environment == 'staging':
            self.driver.get('http://powerchina.ehsy.com')
        elif self.environment == 'production':
            self.driver.get('http://www.ehsy.com')
        self.driver.maximize_window()
        self.cart = Cart(self.driver)
        self.home = Home(self.driver)
        self.order = Order(self.driver)
        self.order_result = OrderResult(self.driver)
        self.product_list = ProductList(self.driver)
        self.quick_order = QuickOrder(self.driver)
        self.report_order = ReportOrder(self.driver)

    def test_powerchina_01(self):
        """产线大图页入口-不开票"""
        login_name = self.page.config_reader('test_order.conf', 'PowerChina_User', 'login_name')
        password = self.page.config_reader('test_order.conf', 'PowerChina_User', 'password')
        self.home.login(login_name, password)
        self.home.category_tree_click(self.home.powerchina_l1_category,self.home.powerchina_l2_category)
        self.product_list.bigImg_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_none_invoice()
        self.order.wait_click(self.order.submit_order_button)
        self.order.wait_click(self.order.notice_layer)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_powerchina_02(self):
        """产线列表页入口-普票"""
        login_name = self.page.config_reader('test_order.conf', 'PowerChina_User', 'login_name')
        password = self.page.config_reader('test_order.conf', 'PowerChina_User', 'password')
        self.home.login(login_name, password)
        self.home.category_tree_click(self.home.powerchina_l1_category,self.home.powerchina_l2_category)
        self.product_list.list_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_normal_invoice()
        self.order.wait_click(self.order.submit_order_button)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_powerchina_03(self):
        """品牌页入口-增票"""
        login_name = self.page.config_reader('test_order.conf', 'PowerChina_User', 'login_name')
        password = self.page.config_reader('test_order.conf', 'PowerChina_User', 'password')
        self.home.login(login_name, password)
        self.home.brand_click()
        self.product_list.brand_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_vat_invoice()
        self.order.wait_click(self.order.submit_order_button)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_powerchina_04(self):
        """搜索页入口-普票"""
        login_name = self.page.config_reader('test_order.conf', 'PowerChina_User', 'login_name')
        password = self.page.config_reader('test_order.conf', 'PowerChina_User', 'password')
        self.home.login(login_name, password)
        self.home.search_sku('AJV671')
        self.product_list.wait_click(self.product_list.bigImg_add_button)
        self.product_list.wait_click(self.product_list.jump_to_cart)
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_normal_invoice()
        self.order.wait_click(self.order.submit_order_button)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_powerchina_05(self):
        """详情页入口-增票"""
        login_name = self.page.config_reader('test_order.conf', 'PowerChina_User', 'login_name')
        password = self.page.config_reader('test_order.conf', 'PowerChina_User', 'password')
        self.home.login(login_name, password)
        self.home.search_sku('AJV671')
        self.page.wait_click(self.product_list.sku_result_click)
        self.page.switch_to_new_window()
        self.product_list.wait_click(self.product_list.skuContent_add_button)
        self.product_list.wait_click(self.product_list.jump_to_cart)
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_vat_invoice()
        self.order.wait_click(self.order.submit_order_button)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def tearDown(self):
        test_method_name = self._testMethodName
        self.driver.save_screenshot("../TestResult/ScreenShot/%s.png" % test_method_name)
        self.driver.quit()


class PowerChinaOrderPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = Page(self.driver)
        self.environment = self.page.config_reader('environment.conf', 'Environment', 'environment')
        if self.environment == 'staging':
            self.driver.get('http://powerchina.ehsy.com')
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

    def test_invoice(self):
        """发票信息增删改"""
        login_name = self.page.config_reader('test_order.conf', 'PowerChina_Address_Invoice', 'login_name')
        password = self.page.config_reader('test_order.conf', 'PowerChina_Address_Invoice', 'password')
        self.home.login(login_name, password)
        ActionChains(self.driver).move_to_element(self.cart.element_find(self.product_list.cart)).perform()
        self.product_list.wait_click(self.product_list.go_cart)
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

    def test_address(self):
        """收货地址增删改"""
        login_name = self.page.config_reader('test_order.conf', 'PowerChina_Address_Invoice', 'login_name')
        password = self.page.config_reader('test_order.conf', 'PowerChina_Address_Invoice', 'password')
        self.home.login(login_name, password)
        ActionChains(self.driver).move_to_element(self.cart.element_find(self.product_list.cart)).perform()
        self.product_list.wait_click(self.product_list.go_cart)
        self.cart.wait_click(self.cart.go_to_order)
        self.order.add_receiving_address()
        self.order.receiving_address_edit()
        self.order.receiving_address_delete()

    def test_invoice_check(self):
        """发票信息填写校验"""
        login_name = self.page.config_reader('test_order.conf', 'PowerChina_Address_Invoice', 'login_name')
        password = self.page.config_reader('test_order.conf', 'PowerChina_Address_Invoice', 'password')
        self.home.login(login_name, password)
        ActionChains(self.driver).move_to_element(self.cart.element_find(self.product_list.cart)).perform()
        self.product_list.wait_click(self.product_list.go_cart)
        self.cart.wait_click(self.cart.go_to_order)
        self.order.normal_invoice_check()
        self.order.wait_click(self.order.confirm)
        self.order.vat_invoice_check()

    def tearDown(self):
        test_method_name = self._testMethodName
        self.driver.save_screenshot("../TestResult/ScreenShot/%s.png" % test_method_name)
        self.driver.quit()

if __name__ == '__main__':
    suit = unittest.TestSuite()
    case_list = [
                  PowerChinaOrder('test_powerchina_01'),
                  PowerChinaOrder('test_powerchina_02'),
                  PowerChinaOrder('test_powerchina_03'),
                  PowerChinaOrder('test_powerchina_04'),
                  PowerChinaOrder('test_powerchina_05'),
                  PowerChinaOrderPage('test_invoice'),
                  PowerChinaOrderPage('test_address'),
                  PowerChinaOrderPage('test_invoice_check'),
    ]
    suit.addTests(case_list)
    # now = time.strftime("%Y_%m_%d %H_%M_%S")
    file = open('../TestResult/PowerChina.html', 'wb')
    runner = HTMLTestRunner(stream=file, title='PowerChina——自动化测试报告', description='测试情况')
    result = runner.run(suit)
    file.close()

    if result.errors:
        msg = 'Error!'
    elif result.failures:
        msg = 'Failed!'
    else:
        msg = 'Success!'

    dir = '../TestResult/PowerChina.html'
    AssistFunction().send_email(dir, msg)


