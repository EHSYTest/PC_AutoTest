from Page_Base import Page
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ProductList(Page):
    """产品列表、大图、品牌页、sku搜索结果页"""
    # 大图页
    big_img_icon = ('by.class_name', 'bigImg-icon')
    bigImg_add_button = ('by.class_name', 'add-tip')
    cart = ('by.class_name', 'cart-wrap')
    go_cart = ('by.link_text', '去购物车结算')
    continue_shopping = ('by.class_name', 'continue-shopping')

    # 列表页
    list_add_button = ('by.class_name', 'a-add')
    cart_button = ('by.class_name', 'addInCart')

    # 品牌页
    brand_add_button = ('by.class_name', 'add-tip')

    # 搜索结果页
    sku_result_click = ('by.xpath', '//div/div/a/div/div/img')
    search_sku = ('by.class_name', 'glob-search-input')  # 搜索框
    search_button = ('by.class_name', 'glob-search-submit')  # 搜索

    # 产品详情页
    skuContent_add_button = ('by.class_name', 'add-to-cart-btn')

    #页面刷新浮层
    layer = ('by.id', 'ajax-layer-loading')
    #商品添加购物车提示
    layer_sku = ('by.id', 'ajax-layer-add-cart')

    def list_add_to_cart(self):
        self.element_find(self.list_add_button).click()
        self.element_find(self.cart_button).click()
        self.wait_to_unvisible(self.layer_sku)
        ActionChains(self.driver).move_to_element(self.element_find(self.cart)).perform()
        self.element_find(self.go_cart).click()

    def bigImg_add_to_cart(self):
        time.sleep(0.5)
        self.element_find(self.big_img_icon).click()
        self.element_find(self.bigImg_add_button).click()
        self.wait_to_unvisible(self.layer_sku)
        ActionChains(self.driver).move_to_element(self.element_find(self.cart)).perform()
        self.element_find(self.go_cart).click()

    def brand_add_to_cart(self):
        self.element_find(self.brand_add_button).click()
        self.wait_to_unvisible(self.layer_sku)
        ActionChains(self.driver).move_to_element(self.element_find(self.cart)).perform()
        self.element_find(self.go_cart).click()

    def search_add_to_cart(self):
        self.element_find(self.search_sku).clear()
        self.element_find(self.search_sku).send_keys('LAA444')  # 区域限制商品
        self.element_find(self.search_button).click()
        self.wait_to_stale(self.layer)
        self.element_find(self.bigImg_add_button).click()
        element = self.wait_to_clickable(self.cart)
        ActionChains(self.driver).move_to_element(element).perform()
        self.wait_to_clickable(self.go_cart).click()
