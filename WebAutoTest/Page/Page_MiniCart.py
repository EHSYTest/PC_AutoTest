from Page_Base import Page
from selenium.webdriver.common.action_chains import ActionChains
import time

class MiniCart(Page):

    search_sku = ('by.class_name', 'glob-search-input')  #搜索框
    search_button = ('by.class_name', 'glob-search-submit')  #搜索
    add_cart = ('by.class_name', 'add-to-cart')  #加入购物车
    cart_windows = ('by.class_name', 'cart-wrap')  #购物车小窗口
    quantity_input = ('by.class_name', 'item-num-input')  ##迷你购物车中商品数量文本框
    quantity_add = ('by.class_name', 'a-add')  #购物车中商品数量增加+
    quantity_sub = ('by.class_name', 'a-sub')  #购物车中商品数量减少-
    delete_sku = ('by.xpath', '/html/body/div[1]/div[2]/div[3]/div/div/div/ul/li/a[2]/img')  #迷你购物车中商品删除
    empty_prompt = ('by.xpath', '//div[3]/div/div/div/div/span')  #空的迷你购物车
    go_to_cart = ('by.class_name', 'accounts-now') #去购物车结算按钮

    def add_to_cart(self):
        self.element_find(self.search_sku).send_keys('MAE475')
        self.element_find(self.search_button).click()
        element = self.wait_to_clickable(self.add_cart)
        element.click()

    def sku_quantity_edit(self):
        element = self.wait_to_clickable(self.cart_windows)
        # self.cart_windows = self.element_find(self.cart_windows)
        ActionChains(self.driver).move_to_element(element).perform()
        sku_quantity_default = self.element_find(self.quantity_input).get_attribute('value')
        print(sku_quantity_default)
        self.wait_to_clickable(self.quantity_add).click()
        ele = self.wait_to_clickable(self.quantity_input)
        sku_quantity_add = self.element_find(self.quantity_input).get_attribute('value')
        print(sku_quantity_add)
        assert int(sku_quantity_add) == int(sku_quantity_default) + 1
        print("添加+数量成功")

        ele = self.wait_to_clickable(self.quantity_sub)
        self.element_find(self.quantity_sub).click()
        ele = self.wait_to_clickable(self.quantity_input)
        sku_quantity_sub = self.element_find(self.quantity_input).get_attribute('value')
        print (sku_quantity_sub)
        assert int(sku_quantity_sub) == int(sku_quantity_add) - 1
        print("减少-数量成功")

        # self.wait_to_clickable(self.quantity_input).clear()
        # self.element_find(self.quantity_input).send_keys(20)
        # sku_quantity_input = self.wait_to_visibility(self.quantity_input).get_attribute('value')
        # print(sku_quantity_input)
        # assert int(sku_quantity_input) == 20
        # print("编辑数量成功")

    def sku_delete(self):
        self.wait_to_clickable(self.delete_sku).click()
        empty_message = self.wait_to_visibility(self.empty_prompt).text
        print(empty_message)

    def enter_normal_cart1(self):
        time.sleep(3)
        self.element_find(self.cart_windows).click()
        title = self.driver.title
        assert title == '购物车-西域'
        print("跳转购物车成功")

    def enter_normal_cart2(self):
        self.wait_to_clickable(self.go_to_cart).click()
        title = self.driver.title
        assert title == '购物车-西域'
        print("跳转购物车成功")


