from Page_Base import Page
from Page_Home import Home
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
import time

class NormalCart(Page):

    product_name = ('by.class_name', 'product-title') #商品名称
    product_img = ('by.xpath', '//ul/li[1]/a/img') #商品图片
    skuContent_product_name = ('by.xpath', '//div[2]/div[2]/div[1]/a[2]') #详情页商品名称
    quantity_input = ('by.class_name', 'item-num-input')  ##购物车中商品数量文本框
    quantity_add = ('by.class_name', 'a-add')  #购物车中商品数量增加+
    quantity_sub = ('by.class_name', 'a-sub')  #购物车中商品数量减少-
    quantity_sub_disable = ('by.class_name', 'disable-sub')
    checkbox = ('by.class_name', 'check-box-center')  #选中某个商品
    checkboxs_top = ('by.class_name', 'check-box-top')  #全选
    checkboxs_bottom = ('by.class_name', 'check-box-bottom')  #全选
    collect = ('by.class_name', 'product-favorite')  #单个商品加入收藏
    collects = ('by.class_name', 'btn-add-favorite')  #购物车商品全部加入收藏
    delete = ('by.class_name', 'product-remove')  #单个商品删除
    deletes = ('by.class_name', 'btn-delete')  #购物车商品全部删除
    sku_num = ('by.class_name','price-num') #商品数量
    empty_cart = ('by.class_name', 'empty-cart-words') #购物车为空
    delete_prompt = ('by.xpath', '//div[1]/button[2]') #清空购物车确认提示
    collect_prompt = ('by.xpath', '//*[@id="js-layer-notice"]/div[1]/div/div') #加入收藏提示
    collects_prompt = ('by.xpath', '//*[@id="js-layer-notice"]/div[1]/div/div') #加入收藏提示
    cart_sku = ('by.xpath', '//p[1]/span') #购物车商品sku
    area_limit_flag = ('by.class_name', 'area-limit-span') #区域限制
    confirm_button = ('by.class_name', 'confirm') #区域限制弹窗确认
    bj_button = ('by.class_name', 'cart-to-bj-btn')  #报价单
    bj_Crumb = ('by.xpath', '//div[2]/div[2]/div[1]/a[3]') #报价单页面面包屑
    check_button = ('by.class_name', 'cart-to-checkout-btn') #去结算
    delivery_addr = ('by.xpath', '//div[2]/div/div/div[1]')#提交订单页面“送货地址”
    blank = ('by.xpath', '//div[2]/ul/li[4]')
    layer = ('by.id', 'ajax-layer-loading')
    layer_notice = ('by.id', 'js-layer-notice')

    def quantity_add_or_sub(self):
        sku_quantity_default = self.element_find(self.quantity_input).get_attribute('value')
        self.element_find(self.quantity_add).click()
        self.wait_to_stale(self.layer)
        sku_quantity_add = self.element_find(self.quantity_input).get_attribute('value')
        assert int(sku_quantity_add) == int(sku_quantity_default) + 1
        print("添加+数量成功")

        self.element_find(self.quantity_sub).click()
        self.wait_to_stale(self.layer)
        sku_quantity_sub = self.element_find(self.quantity_input).get_attribute('value')
        assert int(sku_quantity_sub) == int(sku_quantity_add) - 1
        print("减少-数量成功")
        ele = self.element_find(self.quantity_sub)
        if self.element_find(self.quantity_sub_disable):
            print("商品数量已减少到最小起定量")
        else:
            ele.click()

    def quantity_edit_check(self):
        sku_quantity_default = self.element_find(self.quantity_input).get_attribute('value')
        self.element_find(self.quantity_input).clear()
        self.element_find(self.quantity_input).send_keys(0)
        self.element_find(self.blank).click()
        sku_quantity_input = self.element_find(self.quantity_input).get_attribute('value')
        assert sku_quantity_input == sku_quantity_default
        print('商品数量不能小于最小起定量')

        self.element_find(self.quantity_input).clear()
        self.element_find(self.quantity_input).send_keys(-1)
        self.element_find(self.blank).click()
        sku_quantity_input = self.element_find(self.quantity_input).get_attribute('value')
        assert sku_quantity_input == sku_quantity_default
        print('商品数量不能小于最小起定量')

        self.element_find(self.quantity_input).clear()
        self.element_find(self.quantity_input).send_keys('0.1')
        self.element_find(self.blank).click()
        sku_quantity_input = self.element_find(self.quantity_input).get_attribute('value')
        assert sku_quantity_input == sku_quantity_default
        print('商品数量不能小于最小起定量')

        # self.element_find(self.quantity_input).clear()
        # self.element_find(self.quantity_input).send_keys('q')
        # self.element_find(self.blank).click()
        # sku_quantity_input = self.element_find(self.quantity_input).get_attribute('value')
        # assert sku_quantity_input == sku_quantity_default
        # print('商品数量不能小于最小起定量')

        self.element_find(self.quantity_input).clear()
        self.element_find(self.quantity_input).send_keys(int(sku_quantity_default)-1)
        self.element_find(self.blank).click()
        sku_quantity_input = self.element_find(self.quantity_input).get_attribute('value')
        assert sku_quantity_input == sku_quantity_default
        print('商品数量不能小于最小起定量')

        self.element_find(self.quantity_input).clear()
        self.element_find(self.quantity_input).send_keys(20)
        self.element_find(self.blank).click()
        self.wait_to_stale(self.layer)
        sku_quantity_input = self.element_find(self.quantity_input).get_attribute('value')
        assert int(sku_quantity_input) == 20
        print("编辑数量成功")

    def cart_checkboxs_select(self):
        ###默认选中情况###
        checkbox = self.elements_find(self.checkbox)
        assert checkbox[0].is_selected()
        assert checkbox[1].is_selected()
        checkboxs_top = self.element_find(self.checkboxs_top)
        assert checkboxs_top.is_selected()
        checkboxs_bottom = self.element_find(self.checkboxs_bottom)
        assert checkboxs_bottom.is_selected()
        sku_num = self.element_find(self.sku_num).text
        assert sku_num == '21'

        ###单个商品###
        self.element_find(self.checkbox).click() #点击商品复选框
        self.wait_to_stale(self.layer)
        sku_num = self.element_find(self.sku_num).text  # 商品数量
        assert sku_num == '1'
        print("取消勾选商品成功")
        self.element_find(self.checkbox).click()
        self.wait_to_stale(self.layer)
        sku_num = self.element_find(self.sku_num).text  # 商品数量
        assert sku_num == '21'
        print("勾选商品成功")

        ###全选-top###
        self.element_find(self.checkboxs_top).click()
        self.wait_to_stale(self.layer)
        sku_num = self.element_find(self.sku_num).text
        assert sku_num == '0'
        print("取消全选成功")
        self.element_find(self.checkboxs_top).click()
        self.wait_to_stale(self.layer)
        checkbox = self.elements_find(self.checkbox)
        assert checkbox[0].is_selected()
        assert checkbox[1].is_selected()
        checkboxs_bottom = self.element_find(self.checkboxs_bottom)
        assert checkboxs_bottom.is_selected()
        sku_num = self.element_find(self.sku_num).text
        assert sku_num == '21'
        print("全选成功")

        ###全选-buttom###
        self.element_find(self.checkboxs_bottom).click()
        self.wait_to_stale(self.layer)
        sku_num = self.element_find(self.sku_num).text
        assert sku_num == '0'
        print("取消全选成功")
        self.element_find(self.checkboxs_bottom).click()
        self.wait_to_stale(self.layer)
        checkbox = self.elements_find(self.checkbox)
        assert checkbox[0].is_selected()
        assert checkbox[1].is_selected()
        checkboxs_top = self.element_find(self.checkboxs_top)
        assert checkboxs_top.is_selected()
        sku_num = self.element_find(self.sku_num).text
        assert sku_num == '21'
        print("全选成功")

    def cart_delete(self):
        ### 单个商品删除 ###
        # sku_quantity = self.element_find(self.quantity_input).get_attribute('value')
        # sku_num1 = self.element_find(self.sku_num).text
        # self.element_find(self.delete).click()
        # self.wait_to_stale(self.layer)
        # sku_num2 = self.element_find(self.sku_num).text
        # assert int(sku_num2) == int(sku_num1) - int(sku_quantity)
        # print("删除商品成功")
        ## 清空购物车 ###
        self.element_find(self.deletes).click()
        self.element_find(self.delete_prompt).click()
        self.wait_to_stale(self.layer)
        empty_message = self.element_find(self.empty_cart).text
        assert empty_message == '购物车内暂时没有商品~'
        print("删除商品成功")

    def area_limit_sku(self):
        ###区域限制###
        self.element_find(self.area_limit_flag).click()
        self.element_find(self.confirm_button).click()

    def product_click(self):
        ###商品名称、图片点击###
        # self.element_find(self.product_name).click()
        self.element_find(self.product_img).click()
        ele = self.wait_to_visibility(self.skuContent_product_name)
        title_message = ele.text
        assert self.driver.title == title_message
        print('商品成功跳转到详情页')

    def cart_collect(self):
        ###单个商品收藏###
        self.element_find(self.collect).click()
        loginname = self.config_reader('test_order.conf', '个人账号', 'login_name')
        password = self.config_reader('test_order.conf', '个人账号', 'password')
        home = Home(self.driver)
        home.login_other(loginname,password)
        self.wait_to_stale(self.layer)
        self.element_find(self.collect).click()
        collect_message = self.element_find(self.collect_prompt).text
        assert collect_message == '此商品已成功加入收藏夹！'
        print('收藏成功')
        ###全部收藏###
        self.wait_to_stale(self.layer_notice)
        self.element_find(self.collects).click()
        self.wait_to_stale(self.layer)
        collects_message = self.element_find(self.collects_prompt).text
        assert collects_message == '选中的商品已收藏成功！'
        self.wait_to_stale(self.layer_notice)
        print('全部收藏成功')

    def bj_page(self):
        self.element_find(self.bj_button).click()
        loginname = self.config_reader('test_order.conf', '个人账号', 'login_name')
        password = self.config_reader('test_order.conf', '个人账号', 'password')
        home = Home(self.driver)
        home.login_other(loginname,password)
        self.wait_to_stale(self.layer)
        self.element_find(self.bj_button).click()
        self.wait_to_visibility(self.bj_Crumb)
        assert self.driver.title == '报价单-西域'
        print("成功进入报价单页面")

    def cart_combine(self):
        self.element_find(self.check_button).click()
        loginname = self.config_reader('test_order.conf', '个人账号', 'login_name')
        password = self.config_reader('test_order.conf', '个人账号', 'password')
        home = Home(self.driver)
        home.login_other(loginname,password)
        self.wait_to_stale(self.layer)
        sku_list = self.elements_find(self.cart_sku)
        list = []
        list.append(sku_list[0].text)
        list.append(sku_list[1].text)
        assert 'MAE475' in list and 'LAA444' in list
        print("登录成功后购物车商品合并")
        self.element_find(self.check_button).click()
        self.wait_to_clickable(self.delivery_addr)
        assert self.driver.title == '提交订单-西域'
        print("成功进入提交订单页面")



