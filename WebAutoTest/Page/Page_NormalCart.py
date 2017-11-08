from Page_Base import Page
from Page_Home import Home
from selenium.webdriver.common.action_chains import ActionChains
import time

class NormalCart(Page):

    search_sku = ('by.class_name', 'glob-search-input')  #搜索框
    search_button = ('by.class_name', 'glob-search-submit')  #搜索
    add_cart = ('by.class_name', 'add-to-cart')  #加入购物车
    cart_windows = ('by.class_name', 'cart-wrap')  #购物车小窗口
    quantity_input = ('by.class_name', 'item-num-input')  ##迷你购物车中商品数量文本框
    quantity_add = ('by.class_name', 'a-add')  #购物车中商品数量增加+
    quantity_sub = ('by.class_name', 'a-sub')  #购物车中商品数量减少-
    checkbox = ('by.class_name', 'check-box-center')  #选中某个商品
    checkboxs_top = ('by.class_name', 'check-box-top')  #全选
    checkboxs_bottom = ('by.class_name', 'check-box-bottom')  #全选
    collect = ('by.class_name', 'product-favorite')  #单个商品加入收藏
    collects = ('by.class_name', 'btn-add-favorite')  #购物车商品全部加入收藏
    delete = ('by.class_name', 'product-remove')  #单个商品删除
    deletes = ('by.class_name', 'btn-delete')  #购物车商品全部删除
    sku_price = ('by.xpath','//div[3]/ul/li[5]') #商品价格
    all_price = ('by.class_name', 'price-price') #订单总价
    empty_cart = ('by.class_name', 'empty-cart-words')
    delete_prompt = ('by.xpath', '//div[1]/button[2]')
    collect_prompt = ('by.xpath', '//*[@id="js-layer-notice"]/div[1]/div/div')
    collects_prompt = ('by.xpath', '//*[@id="js-layer-notice"]/div[1]/div/div')

    def add_to_cart(self):
        self.element_find(self.search_sku).send_keys('MAE475')
        self.element_find(self.search_button).click()
        element = self.wait_to_clickable(self.add_cart)
        element.click()
        time.sleep(3)
        self.element_find(self.cart_windows).click()

    def nomal_cart_quantity(self):
        sku_quantity_default = self.element_find(self.quantity_input).get_attribute('value')
        print(sku_quantity_default)
        self.element_find(self.quantity_add).click()
        time.sleep(3)
        sku_quantity_add = self.element_find(self.quantity_input).get_attribute('value')
        print(sku_quantity_add)
        assert int(sku_quantity_add) == int(sku_quantity_default) + 1
        print("添加+数量成功")

        self.element_find(self.quantity_sub).click()
        time.sleep(3)
        sku_quantity_sub = self.element_find(self.quantity_input).get_attribute('value')
        assert int(sku_quantity_sub) == int(sku_quantity_add) - 1
        print("减少-数量成功")

        time.sleep(3)
        self.element_find(self.quantity_input).clear()
        self.element_find(self.quantity_input).send_keys(20)
        time.sleep(3)
        sku_quantity_input = self.element_find(self.quantity_input).get_attribute('value')
        print(sku_quantity_input)
        assert int(sku_quantity_input) == 20
        print("编辑数量成功")

    def checkboxs_select(self):
        ###单个商品###
        sku_price = self.element_find(self.sku_price).text  #选中商品总价
        sku_price = sku_price.split(' ')
        all_price = self.element_find(self.all_price).text   #订单总价
        all_price = all_price.split(' ')
        assert all_price[1] == sku_price[1]
        print("商品加入购物车默认选中")
        self.element_find(self.checkbox).click() #单个商品复选框
        time.sleep(3)
        all_price = self.element_find(self.all_price).text  # 订单总价
        all_price = all_price.split(' ')
        assert all_price[1] == '0.00'
        print("取消勾选商品成功")

        ###全选-top###
        time.sleep(3)
        self.element_find(self.checkboxs_top).click()
        time.sleep(3)
        checkbox = self.element_find(self.checkbox)
        assert checkbox.is_selected()
        print("全选成功")
        self.element_find(self.checkboxs_top).click()
        time.sleep(3)
        all_price = self.element_find(self.all_price).text  # 订单总价
        all_price = all_price.split(' ')
        assert all_price[1] == '0.00'
        print("取消全选成功")

        ###全选-buttom###
        time.sleep(3)
        self.element_find(self.checkboxs_bottom).click()
        time.sleep(3)
        checkbox = self.element_find(self.checkbox)
        assert checkbox.is_selected()
        print("全选成功")
        self.element_find(self.checkboxs_bottom).click()
        time.sleep(3)
        all_price = self.element_find(self.all_price).text
        all_price = all_price.split(' ')
        assert all_price[1] == '0.00'
        print("取消全选成功")

    def normal_cart_delete(self):
        ### 单个商品删除 ###
        # time.sleep(3)
        # self.element_find(self.delete).click()
        # time.sleep(3)
        # empty_message = self.element_find(self.empty_cart).text
        # assert empty_message == '购物车内暂时没有商品~'
        # print("删除商品成功")
        ### 清空购物车 ###
        self.element_find(self.checkboxs_top).click()
        time.sleep(3)
        self.element_find(self.deletes).click()
        self.element_find(self.delete_prompt).click()
        time.sleep(3)
        empty_message = self.element_find(self.empty_cart).text
        assert empty_message == '购物车内暂时没有商品~'
        print("删除商品成功")

    def normal_cart_collect(self):
        ###单个商品收藏###
        time.sleep(3)
        self.element_find(self.collect).click()
        home = Home(self.driver)
        home.login('13111111111', 'qqq111')
        self.element_find(self.collect).click()
        collect_message = self.element_find(self.collect_prompt).text
        assert collect_message == '此商品已成功加入收藏夹！'
        print('收藏成功')
        ###全部收藏###
        # self.element_find(self.checkboxs_top).click()
        time.sleep(3)
        self.element_find(self.collects).click()
        collects_message = self.element_find(self.collects_prompt).text
        assert collects_message == '选中的商品已收藏成功！'
        print('收藏成功')