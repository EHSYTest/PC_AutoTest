from Page_Base import Page
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class Cart(Page):

    checkbox_top = ('by.id', 'cart-checkbox-top')
    checkbox_line = ('by.class_name', 'check-box-line')
    checkbox_bottom = ('by.id', 'cart-checkbox-bottom')

    quantity_input = ('by.class_name', 'item-num-input')
    quantity_add = ('by.class_name', 'a-add')
    quantity_sub = ('by.class_name', 'a-sub')

    collect_line = ('by.class_name', 'cart-add-collect')
    collect_bottom = ('by.class_name', 'footer-add-collection-span')

    delete_line = ('by.class_name', 'cart-del')
    delete_bottom = ('by.class_name', 'footer-del-span')
    layer = ('by.xpath', 'html/body/div[2]/div')
    delete_all_confirm = ('by.xpath', 'html/body/div[3]/div[3]/a[1]')

    go_to_order = ('by.class_name', 'submit-order')
    report_order = ('by.class_name', 'submit-bj')
    eis_layer = ('by.class_name', 'layui-layer-btn0')

    del_unvalued_product = ('by.class_name', 'footer-clear-span')
    product_bottom_add = ('by.xpath', '//div[2]/ul/li[1]/p[4]')

    def checkbox_selected(self):
        """勾选复选框(限制数量为2）"""
        checkboxes = self.elements_find(self.checkbox_line)
        for i in range(min(len(checkboxes), 2)):
            checkboxes = self.elements_find(self.checkbox_line)
            if checkboxes[i].is_selected():
                pass
            else:
                checkboxes[i].click()
                time.sleep(1)

    def checkbox_unselected(self):
        """取消勾选复选框（限制数量为2）"""
        checkboxes = self.elements_find(self.checkbox_line)
        for i in range(min(len(checkboxes), 2)):
            checkboxes = self.elements_find(self.checkbox_line)
            if checkboxes[i].is_selected():
                checkboxes[i].click()
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
                del_list.click()
                time.sleep(1)
                message = self.element_find(self.layer).text
                assert message == '已从购物车中删除此商品'
                time.sleep(1)

    def sku_del_all(self):
        """批量删除sku"""
        self.element_find(self.delete_bottom).click()
        self.element_find(self.delete_all_confirm).click()
        message = self.element_find(self.layer).text
        print(message)
        assert message == '已从购物车中删除此商品'

    def sku_collect(self):
        """加入收藏"""
        collect_list = self.element_find(self.collect_line)
        collect_list.click()
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
        self.element_find(self.collect_bottom).click()
        message = self.element_find(self.layer).text
        print(message)
        assert message == '加入收藏成功。'

    def sku_quantity_edit(self):
        """修改sku数量"""
        quantity = self.element_find(self.quantity_input)
        quantity_value1 = int(quantity.get_attribute('value'))
        self.element_find(self.quantity_add).click()
        time.sleep(0.5)
        quantity = self.element_find(self.quantity_input)
        quantity_value2 = int(quantity.get_attribute('value'))
        assert quantity_value2 == quantity_value1 + 1
        print('数量+修改成功')

        self.element_find(self.quantity_sub).click()
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

    def submit_order_eis(self):
        self.element_find(self.go_to_order).click()
        self.element_find(self.eis_layer).click()
