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
from Page_PersonalCenter import PersonalCenter

class TestOrder(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)
        self.page = Page(self.driver)
        self.environment = self.page.config_reader('environment.conf', 'Environment', 'environment')
        if self.environment == 'staging':
            self.driver.get('http://ps.ehsy.com')
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
        self.personal_center = PersonalCenter(self.driver)

    def test_order_01(self):
        """产线大图页入口-个人用户下单-不开票"""
        login_name = self.page.config_reader('test_order.conf', '个人账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '个人账号', 'password')
        self.home.login(login_name, password)
        self.home.category_tree_click()
        self.product_list.bigImg_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_none_invoice()
        self.order.wait_click(self.order.submit_order_button)
        self.order.wait_click(self.order.notice_layer)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_02(self):
        """产线列表页入口-分销用户下单-普票"""
        login_name = self.page.config_reader('test_order.conf', '分销账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '分销账号', 'password')
        self.home.login(login_name, password)
        self.home.category_tree_click()
        self.product_list.list_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_normal_invoice()
        self.order.wait_click(self.order.submit_order_button)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_03(self):
        """品牌页入口-分销用户下单-增票"""
        login_name = self.page.config_reader('test_order.conf', '分销账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '分销账号', 'password')
        self.home.login(login_name, password)
        self.home.brand_click()
        self.product_list.brand_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_vat_invoice()
        self.order.wait_click(self.order.submit_order_button)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_04(self):
        """搜索页入口-终端用户下单-普票"""
        login_name = self.page.config_reader('test_order.conf', '终端账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '终端账号', 'password')
        self.home.login(login_name, password)
        self.home.search_sku()
        self.product_list.wait_click(self.product_list.bigImg_add_button)
        self.product_list.wait_click(self.product_list.jump_to_cart)
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_normal_invoice()
        self.order.wait_click(self.order.submit_order_button)
        self.order.wait_click(self.order.notice_layer)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_05(self):
        """产品详情页入口-终端用户下单-增票"""
        login_name = self.page.config_reader('test_order.conf', '终端账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '终端账号', 'password')
        self.home.login(login_name, password)
        self.home.search_sku()
        self.page.wait_click(self.product_list.sku_result_click)
        self.page.switch_to_new_window()
        self.product_list.wait_click(self.product_list.skuContent_add_button)
        self.product_list.wait_click(self.product_list.jump_to_cart)
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_vat_invoice()
        self.order.wait_click(self.order.submit_order_button)
        self.order.wait_click(self.order.notice_layer)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_06(self):
        """快速下单页入口-终端用户下单-增票"""
        login_name = self.page.config_reader('test_order.conf', '终端账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '终端账号', 'password')
        self.home.login(login_name, password)
        self.home.quick_order_click()
        self.quick_order.quick_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_vat_invoice()
        self.order.wait_click(self.order.submit_order_button)
        self.order.wait_click(self.order.notice_layer)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_07(self):
        """产线列表页入口-EAS用户下单-超过审批额-审批通过"""
        login_name = self.page.config_reader('test_order.conf', 'EAS账号', 'login_name')
        password = self.page.config_reader('test_order.conf', 'EAS账号', 'password')
        self.home.login(login_name, password)
        self.home.category_tree_click()
        self.product_list.list_add_to_cart()
        self.cart.element_find(self.cart.quantity_input).send_keys(0)  # 修改数量为10，使其超出审批额1000
        self.cart.wait_click(self.cart.unit_price)
        self.cart.wait_click(self.cart.go_to_order)
        self.cart.wait_click(self.cart.choose_company_eas)
        self.cart.wait_click(self.cart.choose_purchaseteam_eas)
        self.cart.wait_click(self.cart.eas_confirm)
        self.order.choose_vat_invoice()
        self.order.wait_click(self.order.submit_order_button)
        self.order.wait_click(self.order.notice_layer)
        self.order.wait_click(self.order.choose_eas_flow)
        self.order.wait_click(self.order.confirm)
        pr_number = self.order_result.get_pr_by_url()
        self.home.wait_click(self.home.logout_button)
        login_name = self.page.config_reader('test_order.conf', 'EAS审批人账号', 'login_name')
        password = self.page.config_reader('test_order.conf', 'EAS审批人账号', 'password')
        self.home.login(login_name, password)
        self.home.wait_click(self.home.my_ehsy)
        self.personal_center.wait_click(self.personal_center.menu_approve)
        pr_number_assert = self.personal_center.element_find(self.personal_center.first_pr_number).text
        assert pr_number == pr_number_assert
        self.personal_center.wait_click(self.personal_center.first_approve_menu)
        self.personal_center.approve_pr(status='pass')
        # 取消订单
        sql = "select a.ORDER_ID from oc.order_info a where a.EXTERNAL_ORDER_NO='"+pr_number+"'"
        sql_result = self.page.db_con('oc-staging', sql)
        SO = sql_result[0]['ORDER_ID']
        print(SO)
        self.page.cancel_order(SO)

    def test_order_08(self):
        """产线大图页入口-EAS用户下单-超过审批额-审批驳回"""
        login_name = self.page.config_reader('test_order.conf', 'EAS账号', 'login_name')
        password = self.page.config_reader('test_order.conf', 'EAS账号', 'password')
        self.home.login(login_name, password)
        self.home.category_tree_click()
        self.product_list.bigImg_add_to_cart()
        self.cart.element_find(self.cart.quantity_input).send_keys(0)  # 修改数量为10，使其超出审批额1000
        self.cart.wait_click(self.cart.unit_price)
        self.cart.wait_click(self.cart.go_to_order)
        self.cart.wait_click(self.cart.choose_company_eas)
        self.cart.wait_click(self.cart.choose_purchaseteam_eas)
        self.cart.wait_click(self.cart.eas_confirm)
        self.order.choose_vat_invoice()
        self.order.wait_click(self.order.submit_order_button)
        self.order.wait_click(self.order.notice_layer)
        self.order.wait_click(self.order.choose_eas_flow)
        self.order.wait_click(self.order.confirm)
        pr_number = self.order_result.get_pr_by_url()
        self.home.wait_click(self.home.logout_button)
        login_name = self.page.config_reader('test_order.conf', 'EAS审批人账号', 'login_name')
        password = self.page.config_reader('test_order.conf', 'EAS审批人账号', 'password')
        self.home.login(login_name, password)
        self.home.wait_click(self.home.my_ehsy)
        self.personal_center.wait_click(self.personal_center.menu_approve)
        pr_number_assert = self.personal_center.element_find(self.personal_center.first_pr_number).text
        assert pr_number == pr_number_assert
        self.personal_center.wait_click(self.personal_center.first_approve_menu)
        self.personal_center.approve_pr(status='reject')

    def test_order_09(self):
        """搜索页入口-EAS用户下单-不超过审批额-自动审批"""
        login_name = self.page.config_reader('test_order.conf', 'EAS账号', 'login_name')
        password = self.page.config_reader('test_order.conf', 'EAS账号', 'password')
        self.home.login(login_name, password)
        self.home.search_sku()
        self.product_list.wait_click(self.product_list.bigImg_add_button)
        self.product_list.wait_click(self.product_list.jump_to_cart)
        self.cart.wait_click(self.cart.go_to_order)
        self.cart.wait_click(self.cart.choose_company_eas)
        self.cart.wait_click(self.cart.choose_purchaseteam_eas)
        self.cart.wait_click(self.cart.eas_confirm)
        self.order.choose_vat_invoice()
        self.order.wait_click(self.order.submit_order_button)
        self.order.wait_click(self.order.notice_layer)
        self.order.wait_click(self.order.choose_eas_flow)
        self.order.wait_click(self.order.confirm)
        pr_number = self.order_result.get_pr_by_url()
        message = self.order_result.element_find(self.order_result.eas_message).text
        assert message == '您提交的请购单已审批通过，请做好收货准备！'
        # 取消订单
        sql = "select a.ORDER_ID from oc.order_info a where a.EXTERNAL_ORDER_NO='" + pr_number + "'"
        sql_result = self.page.db_con('oc-staging', sql)
        SO = sql_result[0]['ORDER_ID']
        print(SO)
        self.page.cancel_order(SO)

    def test_order_10(self):
        """产品详情页入口-EIS用户下单-表单"""
        url = self.page.config_reader('test_order.conf', 'EIS_URL', 'URL_FORM')
        self.driver.get(url)
        self.home.search_sku()
        self.page.wait_click(self.product_list.sku_result_click)
        self.page.switch_to_new_window()
        self.product_list.wait_click(self.product_list.skuContent_add_button)
        self.product_list.wait_click(self.product_list.jump_to_cart)
        self.cart.wait_click(self.cart.go_to_order)
        self.cart.wait_click(self.cart.eis_confirm)
        message = self.order_result.element_find(self.order_result.eis_message).text
        assert message == '推送成功'

    def test_order_11(self):
        """产品列表页入口-EIS用户下单-CXML"""
        url = self.page.config_reader('test_order.conf', 'EIS_URL', 'URL_CXML')
        self.driver.get(url)
        self.home.category_tree_click()
        self.product_list.list_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.cart.wait_click(self.cart.eis_confirm)
        message = self.order_result.element_find(self.order_result.eis_message).text
        assert message == '推送成功'

    def test_order_12(self):
        """报价单入口-终端用户下单-增票(报价地址与收货地址一致)"""
        login_name = self.page.config_reader('test_order.conf', '终端账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '终端账号', 'password')
        self.home.login(login_name, password)
        self.home.search_sku()
        self.page.wait_click(self.product_list.sku_result_click)
        self.page.switch_to_new_window()
        self.product_list.wait_click(self.product_list.skuContent_add_button)
        self.product_list.wait_click(self.product_list.jump_to_cart)
        self.cart.wait_click(self.cart.report_order)
        self.report_order.create_order_by_report_order('北京市', '北京市')
        self.report_order.switch_to_new_window(handle_quantity=2)
        self.order.choose_vat_invoice()
        self.order.wait_click(self.order.submit_order_button)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_13(self):
        """报价单入口-终端用户下单-普票(报价地址与收货地址不一致)"""
        login_name = self.page.config_reader('test_order.conf', '终端账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '终端账号', 'password')
        self.home.login(login_name, password)
        self.home.search_sku()
        self.page.wait_click(self.product_list.sku_result_click)
        self.page.switch_to_new_window()
        self.product_list.wait_click(self.product_list.skuContent_add_button)
        self.product_list.wait_click(self.product_list.jump_to_cart)
        self.cart.wait_click(self.cart.report_order)
        self.report_order.create_order_by_report_order('江苏省', '南京市')
        self.report_order.switch_to_new_window(handle_quantity=2)
        self.order.choose_normal_invoice()
        self.order.wait_click(self.order.submit_order_button)
        alert_text = self.order.element_find(self.order.div_alert).text
        assert alert_text == '收货地址和报价城市不一致'
        self.order.wait_click(self.order.alert_confirm)
        self.order.elements_find(self.order.receiving_address)[1].click()
        self.order.wait_click(self.order.submit_order_button)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_14(self):
        """产线列表页入口-分销定制产线用户下单-普票"""
        login_name = self.page.config_reader('test_order.conf', '产线定制-分销', 'login_name')
        password = self.page.config_reader('test_order.conf', '产线定制-分销', 'password')
        self.home.login(login_name, password)
        attr_class = self.home.element_find(self.home.category_knife).get_attribute('class')
        assert 'disabled' in attr_class
        self.home.category_tree_click()
        self.product_list.list_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_normal_invoice()
        self.order.wait_click(self.order.submit_order_button)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def test_order_15(self):
        """产线列表页入口-终端定制产线用户下单-增票"""
        login_name = self.page.config_reader('test_order.conf', '产线定制-终端', 'login_name')
        password = self.page.config_reader('test_order.conf', '产线定制-终端', 'password')
        self.home.login(login_name, password)
        attr_class = self.home.element_find(self.home.category_knife).get_attribute('class')
        assert 'disabled' in attr_class
        self.home.category_tree_click()
        self.product_list.list_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_vat_invoice()
        self.order.wait_click(self.order.submit_order_button)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def tearDown(self):
        test_method_name = self._testMethodName
        self.driver.save_screenshot("../TestResult/ScreenShot/%s.png" % test_method_name)
        self.driver.quit()

if __name__ == '__main__':
    suit = unittest.TestSuite()
    case_list = [
                  TestOrder('test_order_01'),
                  TestOrder('test_order_02'),
                  TestOrder('test_order_03'),
                  TestOrder('test_order_04'),
                  TestOrder('test_order_05'),
                  TestOrder('test_order_06'),
                  TestOrder('test_order_07'),
                  TestOrder('test_order_08'),
                  TestOrder('test_order_09'),
                  TestOrder('test_order_10'),
                  TestOrder('test_order_11'),
                  TestOrder('test_order_12'),
                  TestOrder('test_order_13'),
                  TestOrder('test_order_14'),
                  TestOrder('test_order_15'),
    ]
    suit.addTests(case_list)
    # now = time.strftime("%Y_%m_%d %H_%M_%S")
    file = open('../TestResult/order.html', 'wb')
    runner = HTMLTestRunner(stream=file, title='WWW下单——测试报告', description='测试情况')
    result = runner.run(suit)
    file.close()


