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
        self.home = Home(self.driver)
        self.productList = ProductList(self.driver)
        self.normal_cart = NormalCart(self.driver)
        with allure.step('---Start---\nenvironment: '+self.environment+'\nurl: '+self.url+'\n'):
            pass

    @allure.story('数量、复选框、商品详情跳转')
    def test_cart_check(self):
        allure.environment(report='Cart_Check Report', browser='Chrome 63', url='http://ps.ehsy.com')
        with allure.step('读取配置的普通产品SKU'):
            sku = self.page.config_reader('data.conf', '普通商品', 'product')
            allure.attach('SKU', sku)
        with allure.step('搜索SKU'):
            self.home.search_sku(sku)
        with allure.step('加入购物车'):
            self.productList.searchResult_add_to_cart()
        with allure.step('SKU数量加减'):
            self.normal_cart.quantity_add_or_sub()
        self.normal_cart.wait_to_stale(self.normal_cart.layer)
        with allure.step('SKU数量编辑'):
            self.normal_cart.quantity_edit_check()
        self.normal_cart.wait_to_stale(self.normal_cart.layer)
        with allure.step('复选框勾选'):
            self.normal_cart.cart_checkboxs_select()
        with allure.step('点击SKU图片跳转详情'):
            self.normal_cart.product_click()

    # def test_cart_areaLimit(self):
    #     ###购物车区域限制商品###
    #     sku = self.page.config_reader('data.conf', '区域限制产品', 'product')
    #     self.home.search_sku(sku)
    #     self.productList.searchResult_add_to_cart()
    #     self.normal_cart.area_limit_sku()

    @allure.story('跳转报价单')
    def test_cart_bj(self):
        allure.environment(report='Cart_BJ Report', browser='Chrome 63', url='http://ps.ehsy.com')
        sku = self.page.config_reader('data.conf', '普通商品', 'product')
        self.home.search_sku(sku)
        self.productList.searchResult_add_to_cart()
        self.normal_cart.bj_page()

    @allure.story('未登录—>登录购物车SKU合并')
    def test_cart_combine(self):
        sku = self.page.config_reader('data.conf', '普通商品', 'product')
        self.home.search_sku(sku)
        self.productList.searchResult_add_to_cart()
        self.normal_cart.cart_combine()

    @allure.story('商品删除')
    def test_cart_delete(self):
        sku = self.page.config_reader('data.conf', '区域限制产品', 'product')
        self.home.search_sku(sku)
        self.productList.searchResult_add_to_cart()
        loginname = self.page.config_reader('test_order.conf', '个人账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '个人账号', 'password')
        self.home.login(loginname, password)
        self.normal_cart.cart_delete()

    def teardown_method(self, method):
        test_method_name = self._testMethodName
        with allure.step('保存截图'):
            self.driver.save_screenshot('../TestResult/ScreenShot/%s.png' % test_method_name)
        f = open('../TestResult/ScreenShot/%s.png' % test_method_name, 'rb').read()
        allure.attach('IMG', f, allure.attach_type.PNG)
        with allure.step('End'):
            self.driver.quit()



