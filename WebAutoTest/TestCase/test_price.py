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
from selenium.webdriver.common.by import By
import allure, pytest


@allure.feature('价格测试')
@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
class TestPrice(unittest.TestCase):

    def setup_method(self, method):
        with allure.step('---Start---'):
            self.driver = webdriver.Chrome()
            self.page = Page(self.driver)
            self.environment = self.page.config_reader('environment.conf', 'Environment', 'environment')
            if self.environment == 'staging':
                self.url = 'http://ps.ehsy.com'
                self.driver.get(self.url)
            else:
                self.url = 'http://new.ehsy.com'
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

    def price_assert(self, dis, csp=False, promotion=False):
        # csp: csp产品标志； promotion: 促销产品标志
        with allure.step('测试价格'):
            with allure.step('判断是否CSP'):
                if csp:     # 若csp,取csp产品和价格
                    product = self.page.config_reader('data.conf', 'csp_price_product', 'csp_product')
                    price = self.page.config_reader('data.conf', 'csp_price_product', 'csp_price')
                    price = float(price)
                    allure.attach('参数值: ', 'Product： '+product+'\nPrice: '+str(price))
            with allure.step('判断是否促销'):
                if promotion:     # 若促销，取促销产品和价格
                    product = self.page.config_reader('data.conf', 'promotion_price_product', 'promotion_product')
                    origin_price = self.page.config_reader('data.conf', 'promotion_price_product', 'origin_price')
                    promotion_price = self.page.config_reader('data.conf', 'promotion_price_product', 'promotion_price')
                    discount_price = float('%.2f' % (float(origin_price) * dis))
                    price = min(float(promotion_price), discount_price)
                    allure.attach('参数值: ', 'Product： '+product+'\nPrice: '+str(price))
            with allure.step('判断是否普通商品'):
                if not (promotion or csp):   # 若普通，取普通产品和价格
                    product = self.page.config_reader('data.conf', 'price_product', 'product')
                    price = self.page.config_reader('data.conf', 'price_product', 'price')
                    price = float('%.2f' % (float(price) * dis))
                    allure.attach('参数值: ', 'Product： '+product+'\nPrice: '+str(price))
            print('price: %.2f' % price)
            with allure.step('搜索结果页价格验证'):
                self.home.search_sku(product)
                search_price = self.product_list.element_find(self.product_list.unit_price).text[2:]
                print('search_price: %s' % float(search_price))
                allure.attach('参数值: ', 'Price： ' + str(price) + '\nSearch_Price: ' + search_price)
                assert price == float(search_price)
            with allure.step('产品详情页价格验证'):
                self.page.wait_click(self.product_list.sku_result_click)
                self.page.switch_to_new_window()
                detail_price = self.product_list.element_find(self.product_list.discount_price).text[2:]
                print('detail_price: %s' % detail_price)
                allure.attach('参数值: ', 'Price： ' + str(price) + '\nDetail_Price: ' + detail_price)
                assert price == float(detail_price)
            with allure.step('购物车页价格验证-单价'):
                self.product_list.wait_click(self.product_list.skuContent_add_button)
                self.product_list.wait_click(self.product_list.jump_to_cart)
                cart_unit_price = self.cart.element_find(self.cart.unit_price).text[2:]
                print('cart_unit_price: %s' % cart_unit_price)
                allure.attach('参数值: ', 'Price： ' + str(price) + '\nCart_Unit_Price: ' + cart_unit_price)
                assert price == float(cart_unit_price)
            with allure.step('购物车页价格验证-总价、折扣优惠'):
                qty = self.cart.element_find(self.cart.quantity_input).get_attribute('value')
                if csp:
                    discount = 0.00
                    total = price * int(qty)
                    total = float('%.2f' % total)
                else:
                    discount = float('%.2f' % (price * int(qty) * 0.02))
                    total = price * int(qty) - discount
                    total = float('%.2f' % total)
                total_assert = self.cart.element_find(self.cart.total_price).text[2:]
                discount_assert = self.cart.element_find(self.cart.discount).text[9:]
                print('total: %.2f, total_assert: %s, discount: %.2f, discount_assert: %s' % (total, total_assert, discount, discount_assert))
                allure.attach('参数值: ', 'Discount： ' + str(discount) + '\nDiscount_Assert: ' + discount_assert + '\nTotal: ' + str(total) + '\nTotal_Assert: ' + total_assert)
                assert (total == float(total_assert)) and (discount == float(discount_assert))   # float == float
            with allure.step('删除商品'):
                self.cart.wait_click(self.cart.delete_line)

    @allure.story('价格测试-个人')
    def test_price_01(self):
        """价格测试-个人"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_price.conf', '个人', 'login_name')
            password = self.page.config_reader('test_price.conf', '个人', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.price_assert(dis=1)

    @allure.story('价格测试-分销-待审核')
    def test_price_02(self):
        """价格测试-分销-待审核"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_price.conf', '分销-待审核', 'login_name')
            password = self.page.config_reader('test_price.conf', '分销-待审核', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.price_assert(dis=0.98)

    @allure.story('价格测试-分销-被驳回')
    def test_price_03(self):
        """价格测试-分销-被驳回"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_price.conf', '分销-被驳回', 'login_name')
            password = self.page.config_reader('test_price.conf', '分销-被驳回', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.price_assert(dis=1)

    @allure.story('价格测试-分销-认证通过')
    def test_price_04(self):
        """价格测试-分销-认证通过"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_price.conf', '分销-已认证', 'login_name')
            password = self.page.config_reader('test_price.conf', '分销-已认证', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.price_assert(dis=0.90)

    @allure.story('价格测试-终端-待审核')
    def test_price_05(self):
        """价格测试-终端-待审核"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_price.conf', '终端-待审核', 'login_name')
            password = self.page.config_reader('test_price.conf', '终端-待审核', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.price_assert(dis=0.98)

    @allure.story('价格测试-终端-被驳回')
    def test_price_06(self):
        """价格测试-终端-被驳回"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_price.conf', '终端-被驳回', 'login_name')
            password = self.page.config_reader('test_price.conf', '终端-被驳回', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.price_assert(dis=1)

    @allure.story('价格测试-终端-认证通过')
    def test_price_07(self):
        """价格测试-终端-认证通过"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_price.conf', '终端-已认证', 'login_name')
            password = self.page.config_reader('test_price.conf', '终端-已认证', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.price_assert(dis=0.98)

    @allure.story('CSP价格测试-分销-认证通过')
    def test_price_08(self):
        """CSP价格测试-分销-认证通过"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_price.conf', '分销-已认证', 'login_name')
            password = self.page.config_reader('test_price.conf', '分销-已认证', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.price_assert(dis=1, csp=True)

    @allure.story('CSP价格测试-终端-认证通过')
    def test_price_09(self):
        """CSP价格测试-终端-认证通过"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_price.conf', '终端-已认证', 'login_name')
            password = self.page.config_reader('test_price.conf', '终端-已认证', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.price_assert(dis=1, csp=True)

    @allure.story('促销价格测试-个人')
    def test_price_10(self):
        """促销价格测试-个人"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_price.conf', '个人', 'login_name')
            password = self.page.config_reader('test_price.conf', '个人', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.price_assert(dis=1, promotion=True)

    @allure.story('促销价格测试-分销-已认证')
    def test_price_11(self):
        """促销价格测试-分销-已认证"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_price.conf', '分销-已认证', 'login_name')
            password = self.page.config_reader('test_price.conf', '分销-已认证', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.price_assert(dis=0.90, promotion=True)

    @allure.story('促销价格测试-终端-已认证')
    def test_price_12(self):
        """促销价格测试-终端-已认证"""
        with allure.step('读取账号配置信息'):
            login_name = self.page.config_reader('test_price.conf', '终端-已认证', 'login_name')
            password = self.page.config_reader('test_price.conf', '终端-已认证', 'password')
            allure.attach('账号信息: ', 'login_name: %s\npassword: %s' % (login_name, password))
        self.home.login(login_name, password)
        self.price_assert(dis=0.98, promotion=True)

    def teardown_method(self, method):
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
    suite.addTests([TestPrice('test_price_08')])
    file = open('../TestResult/EHSY_AutoTest.html', 'wb')
    runner = HTMLTestRunner(stream=file, title='WWW下单——测试报告', description='测试情况')
    runner.run(suite)
    file.close()
