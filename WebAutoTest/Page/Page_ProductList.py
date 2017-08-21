from Page_Base import Page
from selenium.common.exceptions import ElementNotVisibleException
import time


class ProductList(Page):
    """产品列表、大图、品牌页、sku搜索结果页"""
    # 大图页
    big_img_icon = ('by.class_name', 'bigImg-icon')
    bigImg_add_button = ('by.class_name', 'add-tip')
    jump_to_cart = ('by.class_name', 'jumpToCart')
    continue_shopping = ('by.class_name', 'continue-shopping')

    # 列表页
    list_add_button = ('by.class_name', 'a-add')
    cart_button = ('by.class_name', 'addInCart')

    # 品牌页
    brand_add_button = ('by.class_name', 'add-tip')

    # 搜索结果页
    sku_result_click = ('by.xpath', '//div[4]/div/div[2]/a/span')

    # 产品详情页
    skuContent_add_button = ('by.class_name', 'add-to-cart-com')
    skuContent_jump_to_cart = ('by.class_name', 'jumpToCart')

    def list_add_to_cart(self):
        self.element_find(self.list_add_button).click()
        self.element_find(self.cart_button).click()

    def bigImg_add_to_cart(self):
        self.element_find(self.big_img_icon).click()
        self.element_find(self.bigImg_add_button).click()
        self.element_find(self.jump_to_cart).click()

    def brand_add_to_cart(self):
        for i in range(10):
            try:
                self.element_find(self.brand_add_button).click()
                break
            except ElementNotVisibleException:
                time.sleep(0.2)
                continue
        self.element_find(self.jump_to_cart).click()
