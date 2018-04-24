from Page_Base import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, ElementNotVisibleException
from selenium.webdriver.common.by import By
import allure, pytest

class QuickOrder(Page):
    """快速下单页"""
    sku_send = (By.XPATH, '//tr[1]/td[2]/span/input')
    quantity_send = (By.XPATH, '//tr[1]/td[3]/span/input')
    add_to_cart = (By.CLASS_NAME, 'add-to-cart-com')
    cart = (By.XPATH, '/html/body/div[1]/div[2]/div[3]/a')
    go_cart = (By.LINK_TEXT, '去购物车结算')

    def quick_add_to_cart(self, product='MAA904'):
        with allure.step('快速下单页加入购物车'):
            self.element_find(self.sku_send).send_keys(product)
            self.element_find(self.quantity_send).send_keys(10)
            self.wait_click(self.add_to_cart)





