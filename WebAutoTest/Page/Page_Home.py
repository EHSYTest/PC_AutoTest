from Page_Base import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException
from selenium.webdriver.common.by import By
import allure, pytest


class Home(Page):
    """首页"""
    login_button = (By.XPATH, '//*[@id="js-logininfo"]/div[1]/div/a[1]')
    logout_button = (By.XPATH, '//div[1]/span/a[2]')
    username_send = (By.NAME, 'username')
    password_send = (By.NAME, 'password')
    login_action = (By.CLASS_NAME, 'loginpop-btn')
    my_ehsy = (By.CLASS_NAME, 'ehsy-a')

    # 个人中心
    my_address = (By.CLASS_NAME, 'active')  # 进入我的地址标签页

    category_tool = (By.XPATH, '//ul/li[1]/a[1]/span')
    category_taozhuang = (By.LINK_TEXT, '综合套装')
    category_knife = (By.XPATH, '//li[2]/a[1]/span')

    powerchina_l1_category = (By.LINK_TEXT, '主打装备 成套产品')
    powerchina_l2_category = (By.LINK_TEXT, '护理床')

    # my_ehsy = (By.CLASS_NAME, 'my-ehsy-show')
    # my_collection = (By.CLASS_NAME, 'header-my-collection')
    quick_order = (By.CLASS_NAME, 'member-discount')

    search_send = (By.NAME, 'search')
    search_button = (By.CLASS_NAME, 'btn-search')

    my_cart = (By.CLASS_NAME, 'cart-wrap')

    brand_center = (By.LINK_TEXT, '品牌中心')
    brand_bosch = (By.XPATH, "//div[5]/ul[1]/li[1]/a/img")

    layer = (By.ID, 'ajax-layer-loading')

    cxml_url = (By.XPATH, '//url')

    def login(self, login_name, password):
        with allure.step('登录'):
            self.wait_click(self.login_button)
            self.element_find(self.username_send).send_keys(login_name)
            self.element_find(self.password_send).send_keys(password)
            self.wait_click(self.login_action)

    def login_other(self, login_name, password):
        with allure.step('登录'):
            self.element_find(self.username_send).send_keys(login_name)
            self.element_find(self.password_send).send_keys(password)
            self.element_find(self.login_action).click()

    def category_tree_click(self, l1_category=category_tool, l2_category=category_taozhuang):
        with allure.step('点击产线进入产品列表页'):
            l1_category = self.element_find(l1_category)
            ActionChains(self.driver).move_to_element(l1_category).perform()
            self.wait_click(l2_category)

    def search_sku(self, sku='MAA904'):
        with allure.step('搜索SKU'):
            allure.attach('SKU', sku)
            self.element_find(self.search_send).send_keys(sku)
            self.wait_click(self.search_button)

    def quick_order_click(self):
        with allure.step('进入快速下单页'):
            self.wait_click(self.quick_order)

    def brand_click(self):
        with allure.step('进入品牌页'):
            self.wait_click(self.brand_center)
            self.wait_click(self.brand_bosch)

    def go_user_center(self):
        with allure.step('进入个人中心'):
            self.wait_click(self.my_ehsy)





