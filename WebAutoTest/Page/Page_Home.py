from Page_Base import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException
import time, pytest, allure


class Home(Page):
    """首页"""
    login_button = ('by.id', 'refresh-name')
    logout_button = ('by.id', 'refresh-loginout')
    frame = 'loginpop-iframe'
    username_send = ('by.class_name', 'login_messageName')
    password_send = ('by.class_name', 'pwd')
    login_action = ('by.class_name', 'loginpop-btn')

    category_tool = ('by.xpath', '//ul/li[1]/a[1]/span')
    category_taozhuang = ('by.link_text', '综合套装')

    my_ehsy = ('by.class_name', 'my-ehsy-show')
    my_collection = ('by.class_name', 'header-my-collection')
    quick_order = ('by.link_text', '快速下单')

    search_send = ('by.class_name', 's-input')
    search_button = ('by.class_name', 's-btn')

    my_cart = ('by.link_text', '我的购物车')

    brand_bosch = ('by.xpath', "//a[@href='/brand-57']")

    def login(self, login_name, password):
        with allure.step('登陆'):
            self.element_find(self.login_button).click()
            time.sleep(1)
            self.driver.switch_to_frame(self.frame)
            self.element_find(self.username_send).send_keys(login_name)
            self.element_find(self.password_send).send_keys(password)
            self.element_find(self.login_action).click()
            self.driver.switch_to_default_content

    def category_tree_click(self):
        with allure.step('进入二级产线产品列表'):
            category_tool = self.element_find(self.category_tool)
            ActionChains(self.driver).move_to_element(category_tool).perform()
            self.element_find(self.category_taozhuang).click()

    def search_sku(self):
        with allure.step('搜索SKU-MAD618'):
            self.element_find(self.search_send).send_keys('MAD618')
            self.element_find(self.search_button).click()

    def quick_order_click(self):
        with allure.step('进入快速下单页'):
            self.element_find(self.quick_order).click()
            self.switch_to_new_window()

    def brand_click(self):
        with allure.step('进入品牌页'):
            self.element_find(self.brand_bosch).click()
            self.switch_to_new_window()

    def go_my_collection(self):
        with allure.step('进入个人中心-我的收藏'):
            element = self.element_find(self.my_ehsy)
            ActionChains(self.driver).move_to_element(element).perform()
            for i in range(10):
                try:
                    self.element_find(self.my_collection).click()
                    break
                except ElementNotVisibleException:
                    continue
                except WebDriverException:
                    continue




