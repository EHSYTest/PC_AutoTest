from Page_Base import Page
from Page_Home import Home
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
import time
from selenium.webdriver.common.by import By
import pytest, allure


class NormalCart(Page):

    product_name = (By.CLASS_NAME, 'product-title') #商品名称
    product_img = (By.XPATH, '//ul/li[1]/a/img') #商品图片
    skuContent_product_name = (By.XPATH, '//div[2]/div[2]/div[1]/a[2]') #详情页商品名称
    quantity_input = (By.CLASS_NAME, 'item-num-input')  ##购物车中商品数量文本框
    quantity_add = (By.CLASS_NAME, 'a-add')  #购物车中商品数量增加+
    quantity_sub = (By.CLASS_NAME, 'a-sub')  #购物车中商品数量减少-
    quantity_sub_disable = (By.CLASS_NAME, 'disable-sub')
    checkbox = (By.CLASS_NAME, 'check-box-center')  #选中某个商品
    checkboxs_top = (By.CLASS_NAME, 'check-box-top')  #全选
    checkboxs_bottom = (By.CLASS_NAME, 'check-box-bottom')  #全选
    collect = (By.CLASS_NAME, 'product-favorite')  #单个商品加入收藏
    collects = (By.CLASS_NAME, 'btn-add-favorite')  #购物车商品全部加入收藏
    delete = (By.CLASS_NAME, 'product-remove')  #单个商品删除
    deletes = (By.CLASS_NAME, 'btn-delete')  #购物车商品全部删除
    sku_num = (By.CLASS_NAME,'price-num') #商品数量
    empty_cart = (By.CLASS_NAME, 'empty-cart-words') #购物车为空
    delete_confirm = (By.XPATH, '//div[1]/button[2]') #清空购物车确认提示
    collect_prompt = (By.XPATH, '//*[@id="js-layer-notice"]/div[1]/div/div') #加入收藏提示
    collects_prompt = (By.XPATH, '//*[@id="js-layer-notice"]/div[1]/div/div') #加入收藏提示
    cart_sku = (By.XPATH, '//p[1]/span') #购物车商品sku
    area_limit_flag = (By.CLASS_NAME, 'area-limit-span') #区域限制
    confirm_button = (By.CLASS_NAME, 'confirm') #区域限制弹窗确认
    bj_button = (By.CLASS_NAME, 'cart-to-bj-btn')  #报价单
    bj_Crumb = (By.XPATH, '//div[2]/div[2]/div[1]/a[3]') #报价单页面面包屑
    check_button = (By.CLASS_NAME, 'cart-to-checkout-btn') #去结算
    delivery_addr = (By.XPATH, '//div[2]/div/div/div[1]')#提交订单页面“送货地址”
    blank = (By.XPATH, '//div[2]/ul/li[4]')
    layer = (By.ID, 'ajax-layer-loading')
    layer_notice = (By.ID, 'js-layer-notice')

    def quantity_add_or_sub(self):
        with allure.step('SKU数量加'):
            sku_quantity_default = self.element_find(self.quantity_input).get_attribute('value')
            self.wait_click(self.quantity_add)
            sku_quantity_add = self.element_find(self.quantity_input).get_attribute('value')
            allure.attach('参数值: ', 'sku_quantity_default: '+sku_quantity_default+'\nsku_quantity_add: '+sku_quantity_add)
            with allure.step('断言: sku_quantity_add==sku_quantity_default+1'):
                assert int(sku_quantity_add) == int(sku_quantity_default) + 1
        with allure.step('SKU数量减'):
            self.wait_click(self.quantity_sub)
            sku_quantity_sub = self.element_find(self.quantity_input).get_attribute('value')
            allure.attach('参数值: ', 'sku_quantity_sub: '+sku_quantity_sub)
            with allure.step('断言: sku_quantity_sub==sku_quantity_add-1'):
                assert int(sku_quantity_sub) == int(sku_quantity_add) - 1

            # ele = self.element_find(self.quantity_sub)
            # if self.element_find(self.quantity_sub_disable):
            #     print("商品数量已减少到最小起定量")
            # else:
            #     wait_click(ele)

    def quantity_edit_check(self):
        with allure.step('SKU数量编辑'):

            with allure.step('SKU数量输入0'):
                sku_quantity_default = self.element_find(self.quantity_input).get_attribute('value')
                self.element_find(self.quantity_input).clear()
                self.element_find(self.quantity_input).send_keys(0)
                self.wait_click(self.blank)
                sku_quantity_input = self.element_find(self.quantity_input).get_attribute('value')
                allure.attach('参数值: ', 'sku_quantity_default: '+sku_quantity_default+'\nsku_quantity_input: '+sku_quantity_input)
                assert sku_quantity_input == sku_quantity_default

            with allure.step('SKU数量输入-1'):
                self.element_find(self.quantity_input).clear()
                self.element_find(self.quantity_input).send_keys(-1)
                self.wait_click(self.blank)
                sku_quantity_input = self.element_find(self.quantity_input).get_attribute('value')
                allure.attach('参数值: ', 'sku_quantity_default: '+sku_quantity_default+'\nsku_quantity_input: '+sku_quantity_input)
                assert sku_quantity_input == sku_quantity_default

            with allure.step('SKU数量输入0.1'):
                self.element_find(self.quantity_input).clear()
                self.element_find(self.quantity_input).send_keys('0.1')
                self.wait_click(self.blank)
                sku_quantity_input = self.element_find(self.quantity_input).get_attribute('value')
                allure.attach('参数值: ', 'sku_quantity_default: '+sku_quantity_default+'\nsku_quantity_input: '+sku_quantity_input)
                assert sku_quantity_input == sku_quantity_default

            with allure.step('SKU数量输入字母'):
                self.element_find(self.quantity_input).clear()
                self.element_find(self.quantity_input).send_keys('q')
                self.wait_click(self.blank)
                sku_quantity_input = self.element_find(self.quantity_input).get_attribute('value')
                allure.attach('参数值: ', 'sku_quantity_default: '+sku_quantity_default+'\nsku_quantity_input: '+sku_quantity_input)
                assert sku_quantity_input == sku_quantity_default

            with allure.step('SKU数量输入原数量-1'):
                self.element_find(self.quantity_input).clear()
                self.element_find(self.quantity_input).send_keys(int(sku_quantity_default)-1)
                self.wait_click(self.blank)
                sku_quantity_input = self.element_find(self.quantity_input).get_attribute('value')
                allure.attach('参数值: ', 'sku_quantity_default: '+sku_quantity_default+'\nsku_quantity_input: '+sku_quantity_input)
                assert sku_quantity_input == sku_quantity_default

            with allure.step('SKU数量输入20'):
                self.element_find(self.quantity_input).clear()
                self.element_find(self.quantity_input).send_keys(20)
                self.wait_click(self.blank)
                sku_quantity_input = self.element_find(self.quantity_input).get_attribute('value')
                allure.attach('参数值: ', 'sku_quantity_input: '+sku_quantity_input)
                assert int(sku_quantity_input) == 20

    def cart_checkboxs_select(self):
        assert self.element_find(self.checkbox).is_selected()
        assert self.element_find(self.checkboxs_top).is_selected()
        assert self.element_find(self.checkboxs_bottom).is_selected()
        assert self.element_find(self.sku_num).text == '20'

        with allure.step('复选框取消勾选'):
            self.wait_click(self.checkbox)      # 点击商品复选框
            self.wait_to_stale(self.layer)
            sku_num = self.element_find(self.sku_num).text      # 商品数量
            assert sku_num == '0'
        with allure.step('复选框勾选'):
            self.wait_click(self.checkbox)
            self.wait_to_stale(self.layer)
            sku_num = self.element_find(self.sku_num).text  # 商品数量
            assert sku_num == '20'

        with allure.step('取消全选'):
            self.wait_click(self.checkboxs_top)
            self.wait_to_stale(self.layer)
            sku_num = self.element_find(self.sku_num).text
            assert sku_num == '0'
        with allure.step('全选'):
            self.wait_click(self.checkboxs_top)
            self.wait_to_stale(self.layer)
            checkbox = self.element_find(self.checkbox)
            assert checkbox.is_selected()
            checkboxs_bottom = self.element_find(self.checkboxs_bottom)
            assert checkboxs_bottom.is_selected()
            sku_num = self.element_find(self.sku_num).text
            assert sku_num == '20'

            self.wait_click(self.checkboxs_bottom)
            self.wait_to_stale(self.layer)
            sku_num = self.element_find(self.sku_num).text
            assert sku_num == '0'
            print('取消全选成功！')
            self.wait_click(self.checkboxs_bottom)
            self.wait_to_stale(self.layer)
            checkbox = self.element_find(self.checkbox)
            assert checkbox.is_selected()
            checkboxs_top = self.element_find(self.checkboxs_top)
            assert checkboxs_top.is_selected()
            sku_num = self.element_find(self.sku_num).text
            assert sku_num == '20'

    def cart_collect(self):
        ###单个商品收藏###
        self.wait_click(self.collect)
        loginname = self.config_reader('test_order.conf', '个人账号', 'login_name')
        password = self.config_reader('test_order.conf', '个人账号', 'password')
        home = Home(self.driver)
        home.login_other(loginname,password)
        if self.isElementExist(self.collect):
            self.wait_click(self.collect)
            collect_message = self.element_find(self.collect_prompt).text
            self.wait_to_stale(self.layer_notice)
            assert collect_message == '此商品已成功加入收藏夹！'
            print('收藏成功！')
        else:
            print('商品已加入收藏夹！')
        ###全部收藏###
        self.wait_click(self.collects)
        collects_message = self.element_find(self.collects_prompt).text
        assert collects_message == '选中的商品已收藏成功！'
        print('全部收藏成功！')

    def product_click(self):
        with allure.step('点击SKU图片跳转详情'):
            self.wait_click(self.product_img)
            ele = self.wait_to_visibility(self.skuContent_product_name)
            title_message = ele.text
            explore_title = self.driver.title[:-19]
            assert explore_title == title_message

    def area_limit_sku(self):
        with allure.step('点击区域限制标签'):
            self.wait_click(self.area_limit_flag)
            self.wait_click(self.confirm_button)

    def bj_page(self):
        with allure.step('未登录-点击报价单'):
            self.wait_click(self.bj_button)
            loginname = self.config_reader('test_order.conf', '个人账号', 'login_name')
            password = self.config_reader('test_order.conf', '个人账号', 'password')
            home = Home(self.driver)
            home.login_other(loginname, password)
            self.wait_click(self.bj_button)
            self.wait_to_visibility(self.bj_Crumb)
            assert self.driver.title == '报价单-西域'

    def cart_combine(self):
        with allure.step('购物车合并'):
            self.wait_click(self.check_button)
            loginname = self.config_reader('test_order.conf', '个人账号', 'login_name')
            password = self.config_reader('test_order.conf', '个人账号', 'password')
            home = Home(self.driver)
            home.login_other(loginname,password)
            sku_list = self.elements_find(self.cart_sku)
            list = []
            for i in range(len(sku_list)):
                list.append(sku_list[i-1].text)
            sku = self.config_reader('data.conf', '普通商品', 'product')
            assert sku in list
            print('登录成功后购物车商品合并！')
            self.wait_click(self.check_button)
            self.wait_to_clickable(self.delivery_addr)
            assert self.driver.title == '提交订单-西域'
            print('成功进入提交订单页面！')

    def cart_delete(self):
        with allure.step('购物车删除商品'):
            with allure.step('单个商品删除'):
                sku_quantity = self.element_find(self.quantity_input).get_attribute('value')
                sku_num1 = self.element_find(self.sku_num).text
                self.wait_click(self.delete)
                self.wait_to_stale(self.layer_notice)
                sku_num2 = self.element_find(self.sku_num).text
                assert int(sku_num2) == int(sku_num1) - int(sku_quantity)
                print('删除商品成功！')
            with allure.step('清空购物车'):
                self.wait_click(self.deletes)
                self.wait_click(self.delete_confirm)
                self.wait_to_stale(self.layer_notice)
                empty_message = self.element_find(self.empty_cart).text
                assert empty_message == '购物车内暂时没有商品~'
                print('删除商品成功！')


