from Page_Base import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException

class Home(Page):
    """首页"""
    login_button = ('by.link_text', '登录')
    logout_button = ('by.link_text', '退出')
    frame = 'loginpop-iframe'
    username_send = ('by.name', 'username')
    password_send = ('by.name', 'password')
    login_action = ('by.class_name', 'loginpop-btn')
    my_ehsy = ('by.class_name', 'ehsy-a')

    #个人中心
    my_address = ('by.class_name', 'active')  # 进入我的地址标签页

    category_tool = ('by.xpath', '//ul/li[1]/a[1]/span')
    category_taozhuang = ('by.link_text', '综合套装')

    # my_ehsy = ('by.class_name', 'my-ehsy-show')
    # my_collection = ('by.class_name', 'header-my-collection')
    quick_order = ('by.class_name', 'member-discount')

    search_send = ('by.name', 'search')
    search_button = ('by.class_name', 'btn-search')

    my_cart = ('by.class_name', 'cart-wrap')

    brand_center = ('by.link_text', '品牌中心')
    brand_bosch = ('by.xpath', "//div[5]/ul[1]/li[1]/a/img")

    def login(self, login_name, password):
        self.element_find(self.login_button).click()
        self.element_find(self.username_send).send_keys(login_name)
        self.element_find(self.password_send).send_keys(password)
        self.element_find(self.login_action).click()

    def login_other(self, login_name, password):
        self.element_find(self.username_send).send_keys(login_name)
        self.element_find(self.password_send).send_keys(password)
        self.element_find(self.login_action).click()

    def category_tree_click(self):
        category_tool = self.element_find(self.category_tool)
        ActionChains(self.driver).move_to_element(category_tool).perform()
        self.element_find(self.category_taozhuang).click()

    def search_sku(self):
        self.element_find(self.search_send).send_keys('MAE475')
        self.wait_to_clickable(self.search_button).click()

    def quick_order_click(self):
        self.element_find(self.quick_order).click()
        # self.switch_to_new_window()

    def brand_click(self):
        self.wait_to_clickable(self.brand_center).click()
        self.element_find(self.brand_bosch).click()

    def go_user_center(self):
        self.wait_to_clickable(self.my_ehsy).click()

    def go_my_collection(self):
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




