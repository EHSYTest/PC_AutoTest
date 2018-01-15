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


class TestPrice(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = Page(self.driver)
        self.environment = self.page.config_reader('environment.conf', 'Environment', 'environment')
        if self.environment == 'staging':
            self.driver.get('http://ps.ehsy.com/mall')
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

    def price_assert(self, dis, csp=False, promotion=False):
        # csp: csp产品标志； promotion: 促销产品标志
        if csp:     # 若csp,取csp产品和价格
            product = self.page.config_reader('data.conf', 'csp_price_product', 'csp_product')
            price = self.page.config_reader('data.conf', 'csp_price_product', 'csp_price')
            price = float(price)
        elif promotion:     # 若促销，取促销产品和价格
            product = self.page.config_reader('data.conf', 'promotion_price_product', 'promotion_product')
            origin_price = self.page.config_reader('data.conf', 'promotion_price_product', 'origin_price')
            promotion_price = self.page.config_reader('data.conf', 'promotion_price_product', 'promotion_price')
            discount_price = float('%.2f' % (float(origin_price) * dis))
            price = min(float(promotion_price), discount_price)
        else:   # 若普通，取普通产品和价格
            product = self.page.config_reader('data.conf', 'price_product', 'product')
            price = self.page.config_reader('data.conf', 'price_product', 'price')
            price = float('%.2f' % (float(price) * dis))
            print(price)
        # 搜索结果页价格验证
        self.home.search_sku(product)
        search_price = self.product_list.element_find(self.product_list.unit_price).text[2:]
        print(float(search_price))
        assert price == float(search_price)
        # 产品详情页价格验证
        self.page.wait_click(self.product_list.sku_result_click)
        self.page.switch_to_new_window()
        detail_price = self.product_list.element_find(self.product_list.discount_price).text[2:]
        assert price == float(detail_price)
        # 购物车页价格验证-单价
        self.product_list.wait_click(self.product_list.skuContent_add_button)
        ActionChains(self.driver).move_to_element(self.product_list.element_find(self.product_list.cart)).perform()
        self.product_list.wait_click(self.product_list.go_cart)
        cart_unit_price = self.cart.element_find(self.cart.unit_price).text[2:]
        assert price == float(cart_unit_price)
        # 购物车页价格验证-总价、折扣优惠
        qty = self.cart.element_find(self.cart.quantity_input).get_attribute('value')
        if csp:
            discount = 0.00
            total = price * int(qty)
        else:
            discount = float('%.2f' % (price * int(qty) * 0.02))
            total = price * int(qty) - discount
        total_assert = self.cart.element_find(self.cart.total_price).text[2:]
        discount_assert = self.cart.element_find(self.cart.discount).text[9:]
        assert (total == float(total_assert)) and (discount == float(discount_assert))   # float == float
        self.cart.wait_click(self.cart.delete_line)

    def test_price_01(self):
        """价格测试-个人"""
        login_name = self.page.config_reader('test_price.conf', '个人', 'login_name')
        password = self.page.config_reader('test_price.conf', '个人', 'password')
        self.home.login(login_name, password)
        self.price_assert(dis=1)
    
    def test_price_02(self):
        """价格测试-分销-待审核"""
        login_name = self.page.config_reader('test_price.conf', '分销-待审核', 'login_name')
        password = self.page.config_reader('test_price.conf', '分销-待审核', 'password')
        self.home.login(login_name, password)
        self.price_assert(dis=0.98)

    def test_price_03(self):
        """价格测试-分销-被驳回"""
        login_name = self.page.config_reader('test_price.conf', '分销-被驳回', 'login_name')
        password = self.page.config_reader('test_price.conf', '分销-被驳回', 'password')
        self.home.login(login_name, password)
        self.price_assert(dis=1)

    def test_price_04(self):
        """价格测试-分销-认证通过"""
        login_name = self.page.config_reader('test_price.conf', '分销-已认证', 'login_name')
        password = self.page.config_reader('test_price.conf', '分销-已认证', 'password')
        self.home.login(login_name, password)
        self.price_assert(dis=0.88)

    def test_price_05(self):
        """价格测试-终端-待审核"""
        login_name = self.page.config_reader('test_price.conf', '终端-待审核', 'login_name')
        password = self.page.config_reader('test_price.conf', '终端-待审核', 'password')
        self.home.login(login_name, password)
        self.price_assert(dis=0.98)

    def test_price_06(self):
        """价格测试-终端-被驳回"""
        login_name = self.page.config_reader('test_price.conf', '终端-被驳回', 'login_name')
        password = self.page.config_reader('test_price.conf', '终端-被驳回', 'password')
        self.home.login(login_name, password)
        self.price_assert(dis=1)

    def test_price_07(self):
        """价格测试-终端-认证通过"""
        login_name = self.page.config_reader('test_price.conf', '终端-已认证', 'login_name')
        password = self.page.config_reader('test_price.conf', '终端-已认证', 'password')
        self.home.login(login_name, password)
        self.price_assert(dis=0.98)

    def test_price_08(self):
        """CSP价格测试-分销-认证通过"""
        login_name = self.page.config_reader('test_price.conf', '分销-已认证', 'login_name')
        password = self.page.config_reader('test_price.conf', '分销-已认证', 'password')
        self.home.login(login_name, password)
        self.price_assert(dis=1, csp=True)

    def test_price_09(self):
        """CSP价格测试-终端-认证通过"""
        login_name = self.page.config_reader('test_price.conf', '终端-已认证', 'login_name')
        password = self.page.config_reader('test_price.conf', '终端-已认证', 'password')
        self.home.login(login_name, password)
        self.price_assert(dis=1, csp=True)

    def test_price_10(self):
        """促销价格测试-个人"""
        login_name = self.page.config_reader('test_price.conf', '个人', 'login_name')
        password = self.page.config_reader('test_price.conf', '个人', 'password')
        self.home.login(login_name, password)
        self.price_assert(dis=1, promotion=True)

    def test_price_11(self):
        """促销价格测试-分销-已认证"""
        login_name = self.page.config_reader('test_price.conf', '分销-已认证', 'login_name')
        password = self.page.config_reader('test_price.conf', '分销-已认证', 'password')
        self.home.login(login_name, password)
        self.price_assert(dis=0.88, promotion=True)

    def test_price_12(self):
        """促销价格测试-终端-已认证"""
        login_name = self.page.config_reader('test_price.conf', '终端-已认证', 'login_name')
        password = self.page.config_reader('test_price.conf', '终端-已认证', 'password')
        self.home.login(login_name, password)
        self.price_assert(dis=0.98, promotion=True)

    def tearDown(self):
        test_method_name = self._testMethodName
        self.driver.save_screenshot("../TestResult/ScreenShot/%s.png" % test_method_name)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(TestPrice('test_price_12'))
    # file = open('../TestResult/order.html', 'wb')
    # runner = HTMLTestRunner(stream=file, title='WWW下单——测试报告', description='测试情况')
    # runner.run(suite)
    # file.close()
