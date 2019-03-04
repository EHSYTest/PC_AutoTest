from Page_Base import Page
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import allure, pytest

class ProductList(Page):
    """产品列表、大图、品牌页、sku搜索结果页"""
    # 大图页
    big_img_icon = (By.CLASS_NAME, 'bigImg-icon')
    bigImg_add_button = (By.CLASS_NAME, 'add-tip')
    cart = (By.CLASS_NAME, 'cart-wrap')
    go_cart = (By.LINK_TEXT, '去购物车结算')
    continue_shopping = (By.CLASS_NAME, 'continue-shopping')

    # 列表页
    list_add_button = (By.CLASS_NAME, 'a-add')
    cart_button = (By.CLASS_NAME, 'addInCart')

    # 品牌页
    brand_add_button = (By.CLASS_NAME, 'add-tip')

    # 搜索结果页
    sku_result_click = (By.XPATH, '//div/div/a/div/div/img')
    search_sku = (By.CLASS_NAME, 'glob-search-input')  # 搜索框
    search_button = (By.CLASS_NAME, 'glob-search-submit')  # 搜索
    unit_price = (By.XPATH, '//span/span[2]')

    # 产品详情页
    skuContent_add_button = (By.CLASS_NAME, 'add-to-cart-btn')
    discount_price = (By.CLASS_NAME, 'show-price')
    del_price = (By.XPATH, '//del/span')
    ajax_refresh_content = (By.CLASS_NAME, 'icon-product-info-0')    # 其他型号-下方总计（用于判断ajax刷新完成）

    # 去购物车结算按钮
    jump_to_cart = (By.CLASS_NAME, 'jumpToCart')
    # 页面刷新浮层
    layer = (By.ID, 'ajax-layer-loading')
    # 商品添加购物车提示
    layer_sku = (By.ID, 'ajax-layer-add-cart')

    def list_add_to_cart(self):
        with allure.step('产线页加入购物车'):
            self.wait_click(self.list_add_button)
            self.wait_click(self.cart_button)
            self.wait_click(self.go_cart)

    def bigImg_add_to_cart(self):
        with allure.step('大图页加入购物车'):
            self.wait_click(self.big_img_icon)
            self.wait_click(self.bigImg_add_button)
            self.wait_click(self.go_cart)

    def brand_add_to_cart(self):
        with allure.step('品牌页加入购物车'):
            self.wait_click(self.brand_add_button)
            self.wait_click(self.go_cart)

    def searchResult_add_to_cart(self):
        with allure.step('搜索结果页加入购物车'):
            self.wait_click(self.bigImg_add_button)
            self.wait_click(self.jump_to_cart)

    def detail_add_to_cart(self, switch=True):
        with allure.step('详情页加入购物车'):
            self.wait_click(self.sku_result_click)
            if switch:
                self.switch_to_new_window()
            for i in range(3):
                try:
                    self.wait_click(self.skuContent_add_button)
                    self.wait_click(self.jump_to_cart)
                except NoSuchElementException:
                    continue
                else:
                    break

