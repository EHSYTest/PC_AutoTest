from selenium import webdriver
import unittest
from Page_Base import Page


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://ps.ehsy.com')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_a(self):
        self.driver.find_element_by_xpath('//*[@id="js-logininfo"]/div[1]/div/a[1]')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()