from Page_Base import Page
from selenium.common.exceptions import StaleElementReferenceException, ElementNotVisibleException


class QuickOrder(Page):
    """快速下单页"""
    sku_send = ('by.xpath', '//tr[1]/td[2]/span/form/input')
    quantity_send = ('by.xpath', '//tr[1]/td[3]/span/input')
    add_to_cart = ('by.class_name', 'add-to-cart-com')

    def quick_add_to_cart(self):
        while True:
            try:
                self.element_find(self.sku_send).send_keys('MAD618')
                break
            except StaleElementReferenceException:
                continue
        self.element_find(self.quantity_send).send_keys(10)
        for i in range(30):
            try:
                self.element_find(self.add_to_cart).click()
                break
            except ElementNotVisibleException:
                continue



