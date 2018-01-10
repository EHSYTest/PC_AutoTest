from Page_Base import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, ElementNotVisibleException


class QuickOrder(Page):
    """快速下单页"""
    sku_send = ('by.xpath', '//tr[1]/td[2]/span/input')
    quantity_send = ('by.xpath', '//tr[1]/td[3]/span/input')
    add_to_cart = ('by.class_name', 'add-to-cart-com')
    cart = ('by.xpath', '/html/body/div[1]/div[2]/div[3]/a')
    go_cart = ('by.link_text', '去购物车结算')

    def quick_add_to_cart(self, product='MAD618'):
        self.element_find(self.sku_send).send_keys(product)
        self.element_find(self.quantity_send).send_keys(10)
        self.wait_click(self.add_to_cart)





