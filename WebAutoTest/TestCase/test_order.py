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
import pytest, allure


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.feature('下单流程测试')
class TestOrder(unittest.TestCase):

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
            self.personal_center = PersonalCenter(self.driver)
            allure.attach('初始化参数:', 'environment: '+self.environment+'\nurl: '+self.url+'\n')

    @allure.story('个人用户下单-产线大图页入口')
    def test_order_01(self):
        """产线大图页入口-个人用户下单-不开票"""
        allure.environment(Report='AutoTest Report', Browser='Chrome 63', URL=self.url)
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '个人账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '个人账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.home.category_tree_click()
        self.product_list.bigImg_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_none_invoice()
        with allure.step('提交订单'):
            self.order.wait_click(self.order.submit_order_button)
            self.order.wait_click(self.order.notice_layer)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    @allure.story('分销用户下单-产线列表页入口')
    def test_order_02(self):
        """产线列表页入口-分销用户下单-普票"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '分销账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '分销账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.home.category_tree_click()
        self.product_list.list_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_normal_invoice()
        with allure.step('提交订单'):
            self.order.wait_click(self.order.submit_order_button)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    @allure.story('分销用户下单-品牌页入口')
    def test_order_03(self):
        """品牌页入口-分销用户下单-增票"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '分销账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '分销账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.home.brand_click()
        self.product_list.brand_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_vat_invoice()
        with allure.step('提交订单'):
            self.order.wait_click(self.order.submit_order_button)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    @allure.story('终端用户下单-搜索页入口')
    def test_order_04(self):
        """搜索页入口-终端用户下单-普票"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '终端账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '终端账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        sku = self.page.config_reader('data.conf', '普通商品', 'product')
        self.home.search_sku(sku)
        self.product_list.searchResult_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_normal_invoice()
        with allure.step('提交订单'):
            self.order.wait_click(self.order.submit_order_button)
            self.order.wait_click(self.order.notice_layer)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    @allure.story('终端用户下单-产品详情页入口')
    def test_order_05(self):
        """产品详情页入口-终端用户下单-增票"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '终端账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '终端账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        sku = self.page.config_reader('data.conf', '普通商品', 'product')
        self.home.search_sku(sku)
        self.product_list.detail_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_vat_invoice()
        with allure.step('提交订单'):
            self.order.wait_click(self.order.submit_order_button)
            self.order.wait_click(self.order.notice_layer)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    @allure.story('终端用户下单-快速下单页入口')
    def test_order_06(self):
        """快速下单页入口-终端用户下单-增票"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '终端账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '终端账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.home.quick_order_click()
        self.quick_order.quick_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_vat_invoice()
        with allure.step('提交订单'):
            self.order.wait_click(self.order.submit_order_button)
            self.order.wait_click(self.order.notice_layer)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    @allure.story('EAS用户下单-超过审批额-审批通过')
    def test_order_07(self):
        """产线列表页入口-EAS用户下单-超过审批额-审批通过"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', 'EAS账号', 'login_name')
            password = self.page.config_reader('test_order.conf', 'EAS账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.home.category_tree_click()
        self.product_list.list_add_to_cart()
        with allure.step('修改购物车数量为10'):
            self.cart.element_find(self.cart.quantity_input).send_keys(0)  # 修改数量为10，使其超出审批额1000
        self.cart.wait_click(self.cart.unit_price)
        self.cart.wait_click(self.cart.go_to_order)
        with allure.step('选择采购组织'):
            self.cart.wait_click(self.cart.choose_company_eas)
            self.cart.wait_click(self.cart.choose_purchaseteam_eas)
            self.cart.wait_click(self.cart.eas_confirm)
        self.order.choose_vat_invoice()
        with allure.step('提交订单'):
            self.order.wait_click(self.order.submit_order_button)
            with allure.step('选择审批流'):
                self.order.wait_click(self.order.choose_eas_flow)
                self.order.wait_click(self.order.confirm)
        pr_number = self.order_result.get_pr_by_url()
        with allure.step('退出登录'):
            self.home.wait_click(self.home.logout_button)
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', 'EAS审批人账号', 'login_name')
            password = self.page.config_reader('test_order.conf', 'EAS审批人账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        with allure.step('审批采购申请单'):
            self.home.wait_click(self.home.my_ehsy)
            self.personal_center.wait_click(self.personal_center.menu_approve)
            pr_number_assert = self.personal_center.element_find(self.personal_center.first_pr_number).text
            assert pr_number == pr_number_assert
            self.personal_center.wait_click(self.personal_center.first_approve_menu)
            with allure.step('审批通过'):
                self.personal_center.approve_pr(status='pass')
        # 取消订单
        with allure.step('数据库查询SO单号'):
            sql = "select a.ORDER_ID from oc.order_info a where a.EXTERNAL_ORDER_NO='"+pr_number+"'"
            sql_result = self.page.db_con(self.environment, sql)
            SO = sql_result[0]['ORDER_ID']
            allure.attach('SO单号: ', SO)
        self.page.cancel_order(SO, environment=self.environment)

    @allure.story('EAS用户下单-超过审批额-审批驳回')
    def test_order_08(self):
        """产线大图页入口-EAS用户下单-超过审批额-审批驳回"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', 'EAS账号', 'login_name')
            password = self.page.config_reader('test_order.conf', 'EAS账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.home.category_tree_click()
        self.product_list.bigImg_add_to_cart()
        with allure.step('修改购物车数量为10'):
            self.cart.element_find(self.cart.quantity_input).send_keys(0)  # 修改数量为10，使其超出审批额1000
        self.cart.wait_click(self.cart.unit_price)
        self.cart.wait_click(self.cart.go_to_order)
        with allure.step('选择采购组织'):
            self.cart.wait_click(self.cart.choose_company_eas)
            self.cart.wait_click(self.cart.choose_purchaseteam_eas)
            self.cart.wait_click(self.cart.eas_confirm)
        self.order.choose_vat_invoice()
        with allure.step('提交订单'):
            self.order.wait_click(self.order.submit_order_button)
            with allure.step('选择审批流'):
                self.order.wait_click(self.order.choose_eas_flow)
                self.order.wait_click(self.order.confirm)
        pr_number = self.order_result.get_pr_by_url()
        with allure.step('退出登录'):
            self.home.wait_click(self.home.logout_button)
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', 'EAS审批人账号', 'login_name')
            password = self.page.config_reader('test_order.conf', 'EAS审批人账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        with allure.step('审批采购申请单'):
            self.home.wait_click(self.home.my_ehsy)
            self.personal_center.wait_click(self.personal_center.menu_approve)
            pr_number_assert = self.personal_center.element_find(self.personal_center.first_pr_number).text
            assert pr_number == pr_number_assert
            self.personal_center.wait_click(self.personal_center.first_approve_menu)
            with allure.step('审批驳回'):
                self.personal_center.approve_pr(status='reject')

    @allure.story('EAS用户下单-不超过审批额-自动审批')
    def test_order_09(self):
        """搜索页入口-EAS用户下单-不超过审批额-自动审批"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', 'EAS账号', 'login_name')
            password = self.page.config_reader('test_order.conf', 'EAS账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        with allure.step('读取普通商品配置'):
            sku = self.page.config_reader('data.conf', '普通商品', 'product')
            allure.attach('SKU: ', sku)
        self.home.search_sku(sku)
        self.product_list.searchResult_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        with allure.step('选择采购组织'):
            self.cart.wait_click(self.cart.choose_company_eas)
            self.cart.wait_click(self.cart.choose_purchaseteam_eas)
            self.cart.wait_click(self.cart.eas_confirm)
        self.order.choose_vat_invoice()
        with allure.step('提交订单'):
            self.order.wait_click(self.order.submit_order_button)
            with allure.step('选择审批流'):
                self.order.wait_click(self.order.choose_eas_flow)
                self.order.wait_click(self.order.confirm)
        so = self.order_result.get_so_by_url()
        print(so)
        with allure.step('断言页面提示为：订单已提交，请尽快完成支付！'):
            message = self.order_result.element_find(self.order_result.eas_message).text
            assert message == '订单已提交，请尽快完成支付！'
        # 取消订单
        self.page.cancel_order(so, environment=self.environment)

    @allure.story('EIS用户下单-表单')
    def test_order_10(self):
        """产品详情页入口-EIS用户下单-表单"""
        with allure.step('读取EIS-URL配置信息'):
            url = self.page.config_reader('test_order.conf', 'EIS_URL', 'URL_FORM')
            allure.attach('URL: ', url)
        self.driver.get(url)
        with allure.step('读取普通商品配置信息'):
            sku = self.page.config_reader('data.conf', '普通商品', 'product')
            allure.attach('SKU: ', sku)
        self.home.search_sku(sku)
        self.product_list.detail_add_to_cart(switch=False)
        self.cart.wait_click(self.cart.go_to_order)
        self.cart.wait_click(self.cart.eis_confirm)
        with allure.step('断言页面提示为: 推送成功'):
            message = self.order_result.element_find(self.order_result.eis_message).text
            assert message == '推送成功'

    @allure.story('EIS用户下单-CXML')
    def test_order_11(self):
        """产品列表页入口-EIS用户下单-CXML"""
        with allure.step('读取EIS-URL配置信息'):
            url = self.page.config_reader('test_order.conf', 'EIS_URL', 'URL_CXML')
            allure.attach('URL: ', url)
        self.driver.get(url)
        with allure.step('读取页面显示的URL信息'):
            url = self.home.element_find(self.home.cxml_url).text
            allure.attach('URL: ', url)
        self.driver.get(url)
        self.home.category_tree_click()
        self.product_list.list_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.cart.wait_click(self.cart.eis_confirm)
        with allure.step('断言页面提示为: 推送成功'):
            message = self.order_result.element_find(self.order_result.eis_message).text
            assert message == '推送成功'

    @allure.story('报价单转订单-报价地址与收货地址一致')
    def test_order_12(self):
        """报价单入口-终端用户下单-增票(报价地址与收货地址一致)"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '终端账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '终端账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        with allure.step('读取普通商品配置信息'):
            sku = self.page.config_reader('data.conf', '普通商品', 'product')
            allure.attach('SKU: ', sku)
        self.home.search_sku(sku)
        self.product_list.detail_add_to_cart()
        with allure.step('创建报价单'):
            self.cart.wait_click(self.cart.report_order)
            self.report_order.create_order_by_report_order('北京市', '北京市')
        self.report_order.switch_to_new_window(handle_quantity=2)
        self.order.choose_vat_invoice()
        with allure.step('提交订单'):
            self.order.wait_click(self.order.submit_order_button)
            self.order.wait_click(self.order.notice_layer)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    @allure.story('报价单转订单-报价地址与收货地址不一致')
    def test_order_13(self):
        """报价单入口-终端用户下单-普票(报价地址与收货地址不一致)"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '终端账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '终端账号', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        with allure.step('读取普通商品配置信息'):
            sku = self.page.config_reader('data.conf', '普通商品', 'product')
            allure.attach('SKU: ', sku)
        self.home.search_sku(sku)
        self.product_list.detail_add_to_cart()
        self.cart.wait_click(self.cart.report_order)
        self.report_order.create_order_by_report_order('江苏省', '南京市')
        self.report_order.switch_to_new_window(handle_quantity=2)
        self.order.choose_normal_invoice()
        with allure.step('提交订单'):
            self.order.wait_click(self.order.submit_order_button)
            self.order.wait_click(self.order.notice_layer)
        time.sleep(2)
        with allure.step('断言页面提示为: 收货地址和报价城市不一致'):
            alert_text = self.order.element_find(self.order.div_alert).text
            assert alert_text == '收货地址和报价城市不一致'
        self.order.wait_click(self.order.alert_confirm)
        with allure.step('修改收货地址'):
            self.order.elements_find(self.order.receiving_address)[1].click()
        with allure.step('再次提交订单'):
            self.order.wait_click(self.order.submit_order_button)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    @allure.story('分销定制产线用户下单-产线列表页入口')
    def test_order_14(self):
        """产线列表页入口-分销定制产线用户下单-普票"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '产线定制-分销', 'login_name')
            password = self.page.config_reader('test_order.conf', '产线定制-分销', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        with allure.step('断言刀具产线class属性为disabled'):
            attr_class = self.home.element_find(self.home.category_knife).get_attribute('class')
            assert 'disabled' in attr_class
        self.home.category_tree_click()
        self.product_list.list_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_normal_invoice()
        with allure.step('提交订单'):
            self.order.wait_click(self.order.submit_order_button)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    @allure.story('终端定制产线用户下单-产线列表页入口')
    def test_order_15(self):
        """产线列表页入口-终端定制产线用户下单-增票"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_order.conf', '产线定制-终端', 'login_name')
            password = self.page.config_reader('test_order.conf', '产线定制-终端', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        with allure.step('断言刀具产线class属性为disabled'):
            attr_class = self.home.element_find(self.home.category_knife).get_attribute('class')
            assert 'disabled' in attr_class
        self.home.category_tree_click()
        self.product_list.list_add_to_cart()
        self.cart.wait_click(self.cart.go_to_order)
        self.order.choose_vat_invoice()
        with allure.step('提交订单'):
            self.order.wait_click(self.order.submit_order_button)
        orderId = self.order_result.get_so_by_url()
        self.page.cancel_order(orderId, environment=self.environment)  # 接口取消订单

    def teardown_method(self, method):
        test_method_name = self._testMethodName
        with allure.step('保存截图'):
            self.driver.save_screenshot('../TestResult/ScreenShot/%s.png' % test_method_name)
            f = open('../TestResult/ScreenShot/%s.png' % test_method_name, 'rb').read()
            allure.attach('自动化截图', f, allure.attach_type.PNG)
        with allure.step('---End---'):
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
                  TestOrder('test_order_15')
    ]
    suit.addTests(case_list)
    # now = time.strftime("%Y_%m_%d %H_%M_%S")
    file = open('../TestResult/EHSY_AutoTest.html', 'wb')
    runner = HTMLTestRunner(stream=file, title='WWW下单——测试报告', description='测试情况')
    result = runner.run(suit)
    file.close()


