import sys
sys.path.append('../Page')
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from Cart import cart
from Create_Order import Order
from login import login
from configobj import ConfigObj
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException


class testcase(unittest.TestCase):

    def setUp(self):
        self.config_environment = ConfigObj("../config/environment.conf")
        self.environment = self.config_environment['Environment']['environment']
        self.driver = webdriver.Chrome()
        if self.environment == 'staging':
            self.driver.get('http://www-staging.ehsy.com')
        elif self.environment == 'production':
            self.driver.get('http://www.ehsy.com')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.cart = cart(driver=self.driver)
        self.order = Order(self.driver)

    def test_checkbox(self):
            """购物车选中与取消选中"""
            self.driver.find_element_by_name('k').send_keys('MAD617')
            self.driver.find_element_by_class_name('s-btn').click()
            elements = self.driver.find_elements_by_class_name('add-tip')
            for element in elements:
                element.click()
                self.driver.find_element_by_class_name('continue-shopping').click()
            self.driver.find_element_by_link_text('我的购物车').click()
            self.cart.checkbox_unselected()
            time.sleep(1)
            self.cart.checkbox_selected()

    def test_delete(self):
        """购物车sku删除"""
        self.driver.find_element_by_name('k').send_keys('MAD617')
        self.driver.find_element_by_class_name('s-btn').click()
        elements = self.driver.find_elements_by_class_name('add-tip')
        for element in elements:
            element.click()
            self.driver.find_element_by_class_name('continue-shopping').click()
        self.driver.find_element_by_link_text('我的购物车').click()
        self.cart.sku_del()
        self.driver.find_element_by_xpath('//div[2]/ul/li[1]/p[4]').click()
        for i in range(10):
            try:
                self.driver.find_element_by_xpath('//div[2]/ul/li[2]/p[4]').click()
                break
            except WebDriverException:
                continue
        time.sleep(1)
        self.cart.sku_del_all()

    def test_collect(self):
        """购物车收藏"""
        login(self.driver, 'Rick自动化测试', '111qqq')
        self.cart.sku_collect()

    def test_quantity(self):
        """购物车修改sku数量"""
        self.driver.find_element_by_link_text('我的购物车').click()
        for i in range(10):
            try:
                self.driver.find_element_by_xpath('//div[2]/ul/li[1]/p[4]').click()
                break
            except ElementNotVisibleException:
                continue
        time.sleep(1)
        self.cart.sku_quantity_edit()

    def test_receiving_address(self):
        """下单页收货地址新增、编辑、删除"""
        login(self.driver, 'Rick自动化测试', '111qqq')
        self.driver.find_element_by_link_text('我的购物车').click()
        self.driver.find_element_by_class_name('submit-order').click()
        self.order.receiving_address_add()
        self.order.receiving_address_edit()
        self.order.receiving_address_delete()

    def test_invoice(self):
        """新增、删除发票（包括增票和普票）"""
        login(self.driver, 'Rick自动化测试', '111qqq')
        self.driver.find_element_by_link_text('我的购物车').click()
        self.driver.find_element_by_class_name('submit-order').click()
        self.order.invoice_normal_company_add()
        self.order.invoice_normal_personal_add()
        self.order.invoice_VAT_add()
        self.order.invoice_normal_delete()
        self.order.invoice_VAT_delete()

    def tearDown(self):
        test_method_name = self._testMethodName
        self.driver.save_screenshot("../TestResult/ScreenShot/%s.png" % test_method_name)
        super(testcase, self).tearDown()
        self.driver.quit()

if __name__ == '__main__':
    suit = unittest.TestSuite()
    case_list = [
                  testcase('test_checkbox'),
                  testcase('test_delete'),
                  testcase('test_collect'),
                  testcase('test_quantity'),
                  testcase('test_invoice'),
                  testcase('test_receiving_address'),
                  ]
    suit.addTests(case_list)
    # now = time.strftime("%Y_%m_%d %H_%M_%S")
    file = open('../TestResult/cart&invoice_report.html', 'wb')
    runner = HTMLTestRunner(stream=file, title='购物车&发票——测试报告', description='用例执行情况')
    runner.run(suit)
    file.close()
