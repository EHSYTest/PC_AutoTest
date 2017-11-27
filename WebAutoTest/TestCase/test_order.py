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


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = Page(self.driver)
        self.environment = self.page.config_reader('environment.conf', 'Environment', 'environment')
        if self.environment == 'staging':
            self.driver.get('http://ps.ehsy.com/')
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

    def test_order_1(self):
        """产线大图页入口-个人用户下单-不开票"""
        login_name = self.page.config_reader('test_order.conf', '个人账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '个人账号', 'password')
        self.home.login(login_name, password)
        self.home.category_tree_click()
        self.home.wait_to_stale(self.home.layer)
        self.product_list.bigImg_add_to_cart()
        self.home.wait_to_stale(self.home.layer)
        self.cart.element_find(self.cart.go_to_order).click()
        self.home.wait_to_stale(self.home.layer)
        self.order.choose_none_invoice()
        self.order.element_find(self.order.submit_order_button).click()
        self.order.element_find(self.order.notice_layer).click()
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_2(self):
        """产线列表页入口-分销用户下单-普票"""
        login_name = self.page.config_reader('test_order.conf', '分销账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '分销账号', 'password')
        self.home.login(login_name, password)
        self.home.category_tree_click()
        self.home.wait_to_stale(self.home.layer)
        self.product_list.list_add_to_cart()
        self.home.wait_to_stale(self.home.layer)
        self.cart.element_find(self.cart.go_to_order).click()
        self.home.wait_to_stale(self.home.layer)
        self.order.choose_normal_invoice()
        self.order.element_find(self.order.submit_order_button).click()
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_3(self):
        """品牌页入口-分销用户下单-增票"""
        login_name = self.page.config_reader('test_order.conf', '分销账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '分销账号', 'password')
        self.home.login(login_name, password)
        self.home.brand_click()
        self.home.wait_to_stale(self.home.layer)
        self.product_list.brand_add_to_cart()
        self.page.wait_to_stale(self.product_list.layer)
        self.cart.element_find(self.cart.go_to_order).click()
        self.page.wait_to_stale(self.product_list.layer)
        self.order.choose_vat_invoice()
        self.order.element_find(self.order.submit_order_button).click()
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_4(self):
        """详情页入口-终端用户下单-普票"""
        login_name = self.page.config_reader('test_order.conf', '终端账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '终端账号', 'password')
        self.home.login(login_name, password)
        self.home.search_sku()
        self.product_list.wait_to_stale(self.product_list.layer)
        self.product_list.element_find(self.product_list.bigImg_add_button).click()
        self.product_list.wait_to_unvisible(self.product_list.layer_sku)
        ActionChains(self.driver).move_to_element(self.cart.element_find(self.product_list.cart)).perform()
        self.product_list.element_find(self.product_list.go_cart).click()
        self.home.wait_to_stale(self.home.layer)
        self.cart.element_find(self.cart.go_to_order).click()
        self.page.wait_to_stale(self.product_list.layer)
        self.order.choose_normal_invoice()
        self.order.element_find(self.order.submit_order_button).click()
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_5(self):
        """产品详情页入口-终端用户下单-增票"""
        login_name = self.page.config_reader('test_order.conf', '终端账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '终端账号', 'password')
        self.home.login(login_name, password)
        self.home.search_sku()
        self.page.wait_to_stale(self.product_list.layer)
        element = self.page.element_find(self.product_list.sku_result_click)
        element.click()
        self.page.switch_to_new_window()
        self.home.wait_to_stale(self.home.layer)
        self.product_list.element_find(self.product_list.skuContent_add_button).click()
        self.page.wait_to_unvisible(self.product_list.layer_sku)
        ActionChains(self.driver).move_to_element(self.product_list.element_find(self.product_list.cart)).perform()
        self.product_list.element_find(self.product_list.go_cart).click()
        self.page.wait_to_stale(self.product_list.layer)
        self.cart.element_find(self.cart.go_to_order).click()
        self.page.wait_to_stale(self.product_list.layer)
        self.order.choose_vat_invoice()
        self.order.element_find(self.order.submit_order_button).click()
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    # def test_order_6(self):
    #     """产线列表页入口-国电用户下单-普票"""
    #     login_name = self.page.config_reader('test_order.conf', '国电账号', 'login_name')
    #     password = self.page.config_reader('test_order.conf', '国电账号', 'password')
    #     self.home.login(login_name, password)
    #     self.home.category_tree_click()
    #     self.home.wait_to_stale(self.home.layer)
    #     self.product_list.list_add_to_cart()
    #     self.home.wait_to_stale(self.home.layer)
    #     self.cart.element_find(self.cart.go_to_order).click()
    #     self.home.wait_to_stale(self.home.layer)
    #     self.order.choose_normal_invoice()
    #     self.order.element_find(self.order.submit_order_button).click()
    #     orderId = self.order_result.get_so_by_url()
    #     self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单
    #
    # def test_order_7(self):
    #     """快速下单页入口-国电用户下单-增票"""
    #     login_name = self.page.config_reader('test_order.conf', '国电账号', 'login_name')
    #     password = self.page.config_reader('test_order.conf', '国电账号', 'password')
    #     self.home.login(login_name, password)
    #     self.home.quick_order_click()
    #     self.quick_order.quick_add_to_cart()
    #     self.cart.element_find(self.cart.go_to_order).click()
    #     self.order.choose_vat_invoice()
    #     self.order.element_find(self.order.submit_order_button).click()
    #     orderId = self.order_result.get_so_by_url()
    #     self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单
    #
    # def test_order_8(self):
    #     """产线列表页入口-EAS用户下单-不开票-超过审批额"""
    #     login_name = self.page.config_reader('test_order.conf', 'EAS账号', 'login_name')
    #     password = self.page.config_reader('test_order.conf', 'EAS账号', 'password')
    #     self.home.login(login_name, password)
    #     self.home.category_tree_click()
    #     self.product_list.list_add_to_cart()
    #     for i in range(10):
    #         try:
    #             self.cart.element_find(self.cart.quantity_input).send_keys(0)  # 修改数量为10，使其超出审批额1000
    #             time.sleep(2)
    #             break
    #         except StaleElementReferenceException:
    #             continue
    #     self.cart.element_find(self.cart.go_to_order).click()
    #     self.order.choose_none_invoice()
    #     self.order.submit_order_eas(none_invoice=True)
    #     for i in range(30):
    #         try:
    #             message = self.order_result.element_find(self.order_result.eas_message).text
    #             assert message == '您已成功提交请购单，等待审批结果！'
    #             break
    #         except AssertionError:
    #             continue
    #
    # def test_order_9(self):
    #     """产品详情页入口-EAS用户下单-增票-不超过审批额"""
    #     login_name = self.page.config_reader('test_order.conf', 'EAS账号', 'login_name')
    #     password = self.page.config_reader('test_order.conf', 'EAS账号', 'password')
    #     self.home.login(login_name, password)
    #     self.home.search_sku()
    #     self.product_list.element_find(self.product_list.sku_result_click).click()
    #     self.page.switch_to_new_window()
    #     self.product_list.element_find(self.product_list.skuContent_add_button).click()
    #     self.product_list.element_find(self.product_list.skuContent_jump_to_cart).click()
    #     self.cart.element_find(self.cart.go_to_order).click()
    #     self.order.choose_vat_invoice()
    #     self.order.submit_order_eas()
    #     for i in range(10):
    #         try:
    #             orderId = self.order_result.get_order_id()
    #             break
    #         except NoSuchElementException:
    #             continue
    #     self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_10(self):
        """产品详情页入口-EIS用户下单-表单"""
        url = self.page.config_reader('test_order.conf', 'EIS_URL', 'URL_FORM')
        self.driver.get(url)
        self.home.search_sku()
        self.page.wait_to_stale(self.product_list.layer)
        element = self.page.element_find(self.product_list.sku_result_click)
        element.click()
        self.page.switch_to_new_window()
        self.home.wait_to_stale(self.home.layer)
        self.product_list.element_find(self.product_list.skuContent_add_button).click()
        self.page.wait_to_unvisible(self.product_list.layer_sku)
        ActionChains(self.driver).move_to_element(self.product_list.element_find(self.product_list.cart)).perform()
        self.product_list.element_find(self.product_list.go_cart).click()
        self.page.wait_to_stale(self.product_list.layer)
        self.cart.element_find(self.cart.go_to_order).click()
        self.cart.element_find(self.cart.eis_confirm).click()
        message = self.order_result.element_find(self.order_result.eis_message).text
        assert message == '推送成功'

    def test_order_11(self):
        """产品列表页入口-EIS用户下单-CXML"""
        url = self.page.config_reader('test_order.conf', 'EIS_URL', 'URL_CXML')
        self.driver.get(url)
        self.home.category_tree_click()
        self.home.wait_to_stale(self.home.layer)
        self.product_list.list_add_to_cart()
        self.home.wait_to_stale(self.home.layer)
        self.cart.element_find(self.cart.go_to_order).click()
        self.cart.element_find(self.cart.eis_confirm).click()
        message = self.order_result.element_find(self.order_result.eis_message).text
        assert message == '推送成功'

    def test_order_12(self):
        """报价单入口-终端用户下单-增票"""
        login_name = self.page.config_reader('test_order.conf', '终端账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '终端账号', 'password')
        self.home.login(login_name, password)
        self.home.search_sku()
        self.page.wait_to_stale(self.product_list.layer)
        element = self.page.element_find(self.product_list.sku_result_click)
        element.click()
        self.page.switch_to_new_window()
        self.home.wait_to_stale(self.home.layer)
        self.product_list.element_find(self.product_list.skuContent_add_button).click()
        self.page.wait_to_unvisible(self.product_list.layer_sku)
        ActionChains(self.driver).move_to_element(self.product_list.element_find(self.product_list.cart)).perform()
        self.product_list.element_find(self.product_list.go_cart).click()
        self.page.wait_to_stale(self.product_list.layer)
        self.cart.element_find(self.cart.report_order).click()
        self.report_order.create_order_by_report_order()
        self.report_order.switch_to_new_window(handle_quantity=3)
        self.order.choose_vat_invoice()
        self.order.element_find(self.order.submit_order_button).click()
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_13(self):
        """产线列表页入口-分销定制产线用户下单-普票"""
        login_name = self.page.config_reader('test_order.conf', '产线定制-分销', 'login_name')
        password = self.page.config_reader('test_order.conf', '产线定制-分销', 'password')
        self.home.wait_to_stale(self.home.layer)
        self.home.login(login_name, password)
        attr_class = self.home.element_find(self.home.category_knife).get_attribute('class')
        assert 'disabled' in attr_class
        self.home.category_tree_click()
        # self.home.wait_to_stale(self.home.layer)
        self.product_list.list_add_to_cart()
        self.home.wait_to_stale(self.home.layer)
        self.cart.element_find(self.cart.go_to_order).click()
        self.home.wait_to_stale(self.home.layer)
        self.order.choose_normal_invoice()
        self.order.element_find(self.order.submit_order_button).click()
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_14(self):
        """产线列表页入口-终端定制产线用户下单-增票"""
        login_name = self.page.config_reader('test_order.conf', '产线定制-终端', 'login_name')
        password = self.page.config_reader('test_order.conf', '产线定制-终端', 'password')
        self.home.wait_to_stale(self.home.layer)
        self.home.login(login_name, password)
        attr_class = self.home.element_find(self.home.category_knife).get_attribute('class')
        assert 'disabled' in attr_class
        self.home.category_tree_click()
        self.home.wait_to_stale(self.home.layer)
        self.product_list.list_add_to_cart()
        self.home.wait_to_stale(self.home.layer)
        self.cart.element_find(self.cart.go_to_order).click()
        self.home.wait_to_stale(self.home.layer)
        self.order.choose_vat_invoice()
        self.order.element_find(self.order.submit_order_button).click()
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def tearDown(self):
        test_method_name = self._testMethodName
        self.driver.save_screenshot("../TestResult/ScreenShot/%s.png" % test_method_name)
        self.driver.quit()

if __name__ == '__main__':
    suit = unittest.TestSuite()
    case_list = [
                  TestOrder('test_order_1'),
                  TestOrder('test_order_2'),
                  TestOrder('test_order_3'),
                  TestOrder('test_order_4'),
                  TestOrder('test_order_5'),
                  # TestOrder('test_order_6'),
                  # TestOrder('test_order_7'),
                  # TestOrder('test_order_8'),
                  # TestOrder('test_order_9'),
                  TestOrder('test_order_10'),
                  TestOrder('test_order_11'),
                  TestOrder('test_order_12'),
                  TestOrder('test_order_13'),
                  TestOrder('test_order_14'),
    ]
    suit.addTests(case_list)
    # now = time.strftime("%Y_%m_%d %H_%M_%S")
    file = open('../TestResult/order.html', 'wb')
    runner = HTMLTestRunner(stream=file, title='WWW下单——测试报告', description='测试情况')
    runner.run(suit)
    file.close()
