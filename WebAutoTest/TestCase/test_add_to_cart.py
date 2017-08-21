import sys
sys.path.append('../Page')
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from AddToCart import AddToCart
from login import login
from configobj import ConfigObj


class testcase(unittest.TestCase):
    def setUp(self):
        self.config_environment = ConfigObj("../config/environment.conf")
        self.environment = self.config_environment['Environment']['environment']
        self.driver = webdriver.Chrome()
        if self.environment == 'staging':
            self.driver.get('http://www-staging.ehsy.com')
        elif self.environment == 'production':
            self.driver.get('http://www.ehsy.com')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_category_page_list_addtocart(self):
        """产线列表页页面加入购物车"""
        add_to_cart = AddToCart(self.driver)
        add_to_cart.category_page_list_add()

    def test_category_page_bigimg_addtocart(self):
        """产线大图页加入购物车"""
        add_to_cart = AddToCart(self.driver)
        add_to_cart.category_page_bigimg_add()

    def test_content_page_addtocart(self):
        """详情页加入购物车"""
        add_to_cart = AddToCart(self.driver)
        add_to_cart.content_page_add()

    def test_quick_order_addtocart(self):
        """快速下单页加入购物车"""
        add_to_cart = AddToCart(self.driver)
        add_to_cart.quick_order_add()
        
    def test_brand_page_addtocart(self):
        """品牌页加入购物车"""
        add_to_cart = AddToCart(self.driver)
        add_to_cart.brand_page_add()

    def test_buy_again_addtocart(self):
        """个人中心-重新选购加入购物车"""
        add_to_cart = AddToCart(self.driver)
        login(self.driver, 'Rick自动化测试', '111qqq')
        add_to_cart.buy_again_add()

    def tearDown(self):
        test_method_name = self._testMethodName
        self.driver.save_screenshot("../TestResult/ScreenShot/%s.png" % test_method_name)
        super(testcase, self).tearDown()
        self.driver.quit()

if __name__ == '__main__':
    suit = unittest.TestSuite()
    case_list = [
                  testcase('test_category_page_list_addtocart'),
                  testcase('test_category_page_bigimg_addtocart'),
                  testcase('test_content_page_addtocart'),
                  testcase('test_quick_order_addtocart'),
                  testcase('test_brand_page_addtocart'),
                  testcase('test_buy_again_addtocart')
                  ]
    suit.addTests(case_list)
    # now = time.strftime("%Y_%m_%d %H_%M_%S")
    file = open('../TestResult/add_to_cart.html', 'wb')
    runner = HTMLTestRunner(stream=file, title='加入购物车——测试报告', description='用例执行情况')
    runner.run(suit)
    file.close()

