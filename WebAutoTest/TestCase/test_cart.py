import sys
sys.path.append('../Page')
import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from Page_NormalCart import NormalCart
from Page_MiniCart import MiniCart

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        self.driver.get('http://opc-test.ehsy.com/mall/index.php')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.normal_cart = NormalCart(self.driver)
        self.mini_cart = MiniCart(self.driver)

    def test_normal_cart(self):
        self.normal_cart.add_to_cart()

    def test_mini_cart(self):
        self.mini_cart.add_to_cart()
        self.mini_cart.sku_quantity_edit()
        # self.mini_cart.sku_delete()
        # self.mini_cart.enter_normal_cart1()
        # self.mini_cart.enter_normal_cart2()

    def tearDown(self):
        test_method_name = self._testMethodName
        self.driver.save_screenshot('../TestResult/ScreenShot/%s.png' % test_method_name)
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(TestCase('test_normal_cart'))
    suite.addTest(TestCase('test_mini_cart'))
    file = open('../TestResult/order.html' ,'wb')
    runner = HTMLTestRunner(stream=file, title='购物车测试' ,description='测试结果')
    runner.run(suite)
    file.close()
