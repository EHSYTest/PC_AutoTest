import sys
sys.path.append('../Page')
import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from Page_Base import Page
from Page_NormalCart import NormalCart
from Page_MiniCart import MiniCart
from Page_Home import Home
from Page_ProductList import ProductList

class TestCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = Page(self.driver)
        self.environment = self.page.config_reader('environment.conf', 'Environment', 'environment')
        if self.environment == 'staging':
            self.driver.get('http://opc-test.ehsy.com/mall/index.php')
        else:
            self.driver.get('http://opc.ehsy.com/mall/index.php')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.home = Home(self.driver)
        self.productList = ProductList(self.driver)
        self.normal_cart = NormalCart(self.driver)
        self.mini_cart = MiniCart(self.driver)

    def test_cart_check(self):
        """购物车收藏、删除、数量加减、数量编辑、复选框、区域限制校验、商品详情跳转"""
        self.home.search_sku()
        self.productList.wait_to_stale(self.productList.layer)
        self.productList.element_find(self.productList.bigImg_add_button).click()
        self.productList.wait_to_unvisible(self.productList.layer_sku)
        self.productList.search_add_to_cart()
        self.normal_cart.cart_quantity_edit()
        self.normal_cart.cart_checkboxs_select()
        # self.normal_cart.cart_delete()
        self.normal_cart.cart_collect()
        self.normal_cart.area_limit_sku()
        self.normal_cart.product_click()

    def test_cart_bj(self):
        """购物车报价单生成按钮"""
        self.home.search_sku()
        self.productList.wait_to_stale(self.productList.layer)
        self.productList.element_find(self.productList.bigImg_add_button).click()
        self.productList.wait_to_unvisible(self.productList.layer_sku)
        self.productList.search_add_to_cart()
        self.normal_cart.bj_page()

    def test_cart_combine(self):
        """未登录——>登录购物车SKU合并"""
        self.home.search_sku()
        self.productList.wait_to_stale(self.productList.layer)
        self.productList.element_find(self.productList.bigImg_add_button).click()
        self.productList.wait_to_unvisible(self.productList.layer_sku)
        self.productList.search_add_to_cart()
        self.normal_cart.cart_combine()

    def tearDown(self):
        test_method_name = self._testMethodName
        self.driver.save_screenshot('../TestResult/ScreenShot/%s.png' % test_method_name)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

