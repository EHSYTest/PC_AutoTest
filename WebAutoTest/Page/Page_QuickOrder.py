from Page.Page_Base import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, ElementNotVisibleException


class QuickOrder(Page):
    """快速下单页"""
    sku_send = ('by.xpath', '//tr[1]/td[2]/span/input')
    quantity_send = ('by.xpath', '//tr[1]/td[3]/span/input')
    add_to_cart = ('by.class_name', 'add-to-cart-com')
    cart = ('by.xpath', '/html/body/div[1]/div[2]/div[3]/a')
    go_cart = ('by.link_text', '去购物车结算')


    def quick_add_to_cart(self):
        self.element_find(self.sku_send).send_keys('MAD618')
        self.element_find(self.quantity_send).send_keys(10)
        self.element_find(self.add_to_cart).click()
        element = self.wait_to_clickable(self.cart)
        ActionChains(self.driver).move_to_element(element).perform()
        self.element_find(self.go_cart).click()

        # element.click()
        # self.element_find(element).click()
        # while True:
        #     try:
        #         self.element_find(self.sku_send).send_keys('MAD618')
        #         break
        #     except StaleElementReferenceException:
        #         continue
        # self.element_find(self.quantity_send).send_keys(10)
        # for i in range(30):
        #     try:
        #         self.element_find(self.add_to_cart).click()
        #         break
        #     except ElementNotVisibleException:
        #         continue



