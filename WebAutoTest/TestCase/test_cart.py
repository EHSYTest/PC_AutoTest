import sys
sys.path.append('../Page')
import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from Page_Base import Page
from Page_NormalCart import NormalCart
from Page_Home import Home
from Page_ProductList import ProductList
import pytest


class TestCart(unittest.TestCase):

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.page = Page(self.driver)
        self.environment = self.page.config_reader('environment.conf', 'Environment', 'environment')
        if self.environment == 'staging':
            self.driver.get('http://ps.ehsy.com')
        else:
            self.driver.get('http://new.ehsy.com')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.home = Home(self.driver)
        self.productList = ProductList(self.driver)
        self.normal_cart = NormalCart(self.driver)

    def test_cart_check(self):
        ###购物车数量加减、数量编辑、复选框、收藏、商品详情跳转###
        sku = self.page.config_reader('data.conf' , '普通商品', 'product')
        self.home.search_sku(sku)
        self.productList.searchResult_add_to_cart()
        self.normal_cart.quantity_add_or_sub()
        self.normal_cart.wait_to_stale(self.normal_cart.layer)
        self.normal_cart.quantity_edit_check()
        self.normal_cart.wait_to_stale(self.normal_cart.layer)
        self.normal_cart.cart_checkboxs_select()
        # self.normal_cart.cart_collect()
        self.normal_cart.product_click()

    # def test_cart_areaLimit(self):
    #     ###购物车区域限制商品###
    #     sku = self.page.config_reader('data.conf', '区域限制产品', 'product')
    #     self.home.search_sku(sku)
    #     self.productList.searchResult_add_to_cart()
    #     self.normal_cart.area_limit_sku()

    def test_cart_bj(self):
        ###购物车报价单生成按钮###
        sku = self.page.config_reader('data.conf', '普通商品', 'product')
        self.home.search_sku(sku)
        self.productList.searchResult_add_to_cart()
        self.normal_cart.bj_page()

    def test_cart_combine(self):
        ###未登录——>登录购物车SKU合并###
        sku = self.page.config_reader('data.conf', '普通商品', 'product')
        self.home.search_sku(sku)
        self.productList.searchResult_add_to_cart()
        self.normal_cart.cart_combine()

    def test_cart_delete(self):
        ###购物车商品删除###
        sku = self.page.config_reader('data.conf', '区域限制产品', 'product')
        self.home.search_sku(sku)
        self.productList.searchResult_add_to_cart()
        loginname = self.page.config_reader('test_order.conf', '个人账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '个人账号', 'password')
        self.home.login(loginname, password)
        self.normal_cart.cart_delete()

    def teardown_method(self, method):
        test_method_name = self._testMethodName
        self.driver.save_screenshot('../TestResult/ScreenShot/%s.png' % test_method_name)
        self.driver.quit()
# if __name__ == '__main__':
#     # unittest.main()
#     suite = unittest.TestSuite()
#     suite.addTest(TestCart('test_cart_bj'))
#     file = open('../TestResult/EHSY_AutoTest.html', 'wb')
#     runner = HTMLTestRunner(stream=file, title='WWW下单——测试报告', description='测试情况')
#     runner.run(suite)
#     file.close()


