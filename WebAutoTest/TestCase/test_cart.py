import sys
sys.path.append('../Page')
import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from Page_Base import Page
from Page_NormalCart import NormalCart
from Page_Home import Home
from Page_ProductList import ProductList
import pytest, allure


@allure.feature('购物车页面测试')
@pytest.allure.severity(pytest.allure.severity_level.MINOR)
class TestCart(unittest.TestCase):

    def setup_method(self, method):
        with allure.step('---Start---'):
            self.driver = webdriver.Chrome('/desktop/chromedriver')
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
            self.home = Home(self.driver)
            self.productList = ProductList(self.driver)
            self.normal_cart = NormalCart(self.driver)
            allure.attach('初始化参数:', 'environment: '+self.environment+'\nurl: '+self.url+'\n')

    @allure.story('数量、复选框、商品详情跳转')
    def test_cart_check(self):
        # allure.environment(Report='Cart Report', Browser='Chrome 63', URL=self.url)
        with allure.step('读取配置的普通产品SKU'):
            sku = self.page.config_reader('data.conf', '普通商品', 'product')
            allure.attach('SKU', sku)
        self.home.search_sku(sku)
        self.productList.searchResult_add_to_cart()
        self.normal_cart.quantity_add_or_sub()
        self.normal_cart.wait_to_stale(self.normal_cart.layer)
        self.normal_cart.quantity_edit_check()
        self.normal_cart.wait_to_stale(self.normal_cart.layer)
        self.normal_cart.cart_checkboxs_select()
        self.normal_cart.product_click()

    # def test_cart_areaLimit(self):
    #     ###购物车区域限制商品###
    #     sku = self.page.config_reader('data.conf', '区域限制产品', 'product')
    #     self.home.search_sku(sku)
    #     self.productList.searchResult_add_to_cart()
    #     self.normal_cart.area_limit_sku()

    @allure.story('跳转报价单')
    def test_cart_bj(self):
        with allure.step('读取普通商品配置信息'):
            sku = self.page.config_reader('data.conf', '普通商品', 'product')
            allure.attach('SKU: ', sku)
        self.home.search_sku(sku)
        self.productList.searchResult_add_to_cart()
        self.normal_cart.bj_page()

    @allure.story('未登录—>登录购物车SKU合并')
    def test_cart_combine(self):
        with allure.step('读取普通商品配置信息'):
            sku = self.page.config_reader('data.conf', '普通商品', 'product')
            allure.attach('SKU: ', sku)
        self.home.search_sku(sku)
        self.productList.searchResult_add_to_cart()
        self.normal_cart.cart_combine()

    @allure.story('商品删除')
    def test_cart_delete(self):
        with allure.step('读取普通商品配置信息'):
            sku = self.page.config_reader('data.conf', '区域限制产品', 'product')
            allure.attach('SKU: ', sku)
        self.home.search_sku(sku)
        self.productList.searchResult_add_to_cart()
        with allure.step('读取账号配置信息'):
            loginname = self.page.config_reader('test_order.conf', '个人账号', 'login_name')
            password = self.page.config_reader('test_order.conf', '个人账号', 'password')
            allure.attach('账号: ', 'loginname: '+loginname+'\npassword: '+password)
        with allure.step('登录'):
            self.home.login(loginname, password)
        self.normal_cart.cart_delete()

    def teardown_method(self, method):
        test_method_name = self._testMethodName
        with allure.step('保存截图'):
            self.driver.save_screenshot('../TestResult/ScreenShot/%s.png' % test_method_name)
            f = open('../TestResult/ScreenShot/%s.png' % test_method_name, 'rb').read()
            allure.attach('自动化截图', f, allure.attach_type.PNG)
        with allure.step('End'):
            self.driver.quit()



