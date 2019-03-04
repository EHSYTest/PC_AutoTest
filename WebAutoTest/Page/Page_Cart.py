from Page_Base import Page
import time, pytest, allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class Cart(Page):
    """购物车页面"""
    checkbox_top = (By.CLASS_NAME, 'check-box-top')
    checkbox_line = (By.CLASS_NAME, 'check-box-center')
    checkbox_bottom = (By.CLASS_NAME, 'check-box-bottom')

    quantity_input = (By.CLASS_NAME, 'item-num-input')
    quantity_add = (By.CLASS_NAME, 'a-add')
    quantity_sub = (By.CLASS_NAME, 'a-sub')

    collect_bottom = (By.CLASS_NAME, 'btn-add-favorite')

    delete_line = (By.CLASS_NAME, 'product-remove')
    delete_bottom = (By.CLASS_NAME, 'btn-delete')
    delete_all_confirm = (By.XPATH, '//div[1]/button[2]')
    product_line = (By.CLASS_NAME, 'product-list-body')

    go_to_order = (By.CLASS_NAME, 'cart-to-checkout-btn')
    report_order = (By.CLASS_NAME, 'cart-to-bj-btn')
    eis_confirm = (By.XPATH, '//div[1]/button[2]')

    unit_price = (By.CLASS_NAME, 'td_3')
    total_price = (By.CLASS_NAME, 'price-price')
    discount = (By.XPATH, '//div[2]/div/div[2]/span[2]')

    choose_company_eas = (By.XPATH, '//li[1]/div[2]/select/option[2]')
    choose_purchaseteam_eas = (By.XPATH, '//li[2]/div[2]/select/option[2]')
    eas_confirm = (By.CLASS_NAME, 'confirm')

    def checkbox_selected(self):
        """勾选复选框(限制数量为2）"""
        checkboxes = self.elements_find(self.checkbox_line)
        for i in range(min(len(checkboxes), 2)):
            checkboxes = self.elements_find(self.checkbox_line)
            if checkboxes[i].is_selected():
                pass
            else:
                self.wait_click(checkboxes[i])
                time.sleep(1)

    def checkbox_unselected(self):
        """取消勾选复选框（限制数量为2）"""
        checkboxes = self.elements_find(self.checkbox_line)
        for i in range(min(len(checkboxes), 2)):
            checkboxes = self.elements_find(self.checkbox_line)
            if checkboxes[i].is_selected():
                self.wait_click(checkboxes[i])
                time.sleep(1)
            else:
                pass

    def sku_del(self):
        """删除sku"""
        for i in range(30):
            try:
                del_list = self.elements_find(self.delete_line)
            except NoSuchElementException:
                break
            if del_list:
                self.wait_click(del_list)
                time.sleep(1)
                message = self.element_find(self.layer).text
                assert message == '已从购物车中删除此商品'
                time.sleep(1)

    def sku_del_all(self):
        """批量删除sku"""
        self.wait_click(self.delete_bottom)
        self.wait_click(self.delete_all_confirm)
        message = self.element_find(self.layer).text
        print(message)
        assert message == '已从购物车中删除此商品'

    def sku_collect(self):
        """加入收藏"""
        collect_list = self.element_find(self.collect_line)
        self.wait_click(collect_list)
        for j in range(30):
            message = self.element_find(self.layer).text
            if message == '加入收藏成功。':
                break
            else:
                continue
        print(message)
        assert message == '加入收藏成功。'
        time.sleep(1)

    def sku_collect_all(self):
        """批量加入收藏夹"""
        self.wait_click(self.collect_bottom)
        message = self.element_find(self.layer).text
        print(message)
        assert message == '加入收藏成功。'

    def sku_quantity_edit(self):
        """修改sku数量"""
        quantity = self.element_find(self.quantity_input)
        quantity_value1 = int(quantity.get_attribute('value'))
        self.wait_click(self.quantity_add)
        time.sleep(0.5)
        quantity = self.element_find(self.quantity_input)
        quantity_value2 = int(quantity.get_attribute('value'))
        assert quantity_value2 == quantity_value1 + 1
        print('数量+修改成功')

        self.wait_click(self.quantity_sub)
        time.sleep(0.5)
        quantity = self.element_find(self.quantity_input)
        quantity_value3 = int(quantity.get_attribute('value'))
        assert quantity_value3 == quantity_value1
        print('数量-修改成功')

        input_value = self.element_find(self.quantity_input)
        input_value.clear()
        input_value.send_keys(20)
        input_value.send_keys(Keys.ENTER)
        time.sleep(0.5)
        value2 = self.element_find(self.quantity_input).get_attribute('value')
        assert value2 == '20'
        print('数量输入修改成功')

    def check_cart_empty(self):
        with allure.step('检查购物车是否为空'):
            count = len(self.elements_find(self.product_line))
            allure.attach('购物车产品行:', 'Count: {}'.format({count}))
            if count <= 1:
                return True
            else:
                ele = self.element_find(self.checkbox_bottom)
                if not ele.is_selected():
                    ele.click()
                self.wait_click(self.checkbox_line)
                self.wait_click(self.delete_bottom)
                self.wait_click(self.delete_all_confirm)
            self.wait_click(self.checkbox_line)
            time.sleep(2)
