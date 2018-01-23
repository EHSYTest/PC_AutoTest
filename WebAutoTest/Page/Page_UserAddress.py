from Page_Base import Page
from selenium.webdriver.common.action_chains import ActionChains
import time


class UserAddress(Page):
    my_address = ('by.link_text', '我的地址') #进入我的（通用）地址标签页
    receive_address = ('by.xpath', '//div/div[1]/div[2]/a') #进入收货地址标签页
    invoice_address = ('by.xpath', '//div/div/div/div[1]/div[3]/a') #进入发票地址标签页
    add_address = ('by.class_name', 'mod-ra-add-btn') #添加新地址按钮
    address_num = ('by.xpath', '//div/div/div/div[2]/div/div/span') #地址数量
    #添加地址弹窗
    receiver_name = ('by.name', 'receiver_name')
    company_name = ('by.name', 'company_name')
    province = ('by.name', 'province_id')
    city = ('by.name', 'city_id')
    area = ('by.name', 'area_id')
    detail_address = ('by.name', 'detail_address')
    phone = ('by.name', 'cell_phone')
    telephone = ('by.name', 'telephone')
    checkbox_defaultAddress = ('by.name', 'is_default')
    confirm_button = ('by.class_name', 'confirm')
    cancel_button = ('by.class_name', 'cancel')

    #修改地址
    edit_address = ('by.xpath', '//div/ul/li[2]/div[4]/a[1]')
    receiver = ('by.xpath', '//div/div/div[2]/div/div/ul/li[2]/div[1]')

    #设置默认地址
    default_address_button = ('by.class_name', 'default-btn')
    default_address_lable = ('by.xpath', '//ul/li[2]/div[4]/span')

    #删除地址
    delete_address = ('by.xpath', '//ul/li[2]/div[4]/a[2]')
    confirm = ('by.xpath', '//button[2]')

    #loading
    layer = ('by.id', 'ajax-layer-loading')

    def add_currency_address(self):
        ###添加通用地址###
        address_num = self.element_find(self.address_num).text
        add_front_num = address_num[4:5]
        self.wait_click(self.add_address)
        self.element_find(self.receiver_name).send_keys("测试")
        self.element_find(self.company_name).send_keys('测试公司')
        self.element_find(self.province).send_keys('安徽省')
        self.element_find(self.city).send_keys('安庆市')
        self.element_find(self.area).send_keys('迎江市')
        self.element_find(self.detail_address).send_keys('测试地址')
        self.element_find(self.phone).send_keys('13111111111')
        self.element_find(self.telephone).send_keys('020-88888888-8888')
        self.wait_click(self.checkbox_defaultAddress)
        self.wait_click(self.confirm_button)
        time.sleep(2)
        address_num = self.element_find(self.address_num).text
        add_after_num = address_num[4:5]
        assert int(add_after_num) == int(add_front_num) + 1
        print("通用地址添加成功！")

    def edit_currency_address(self):
        ###编辑通用地址###
        self.wait_click(self.edit_address)
        self.element_find(self.receiver_name).send_keys('-修改')
        self.element_find(self.company_name).send_keys('-修改')
        self.element_find(self.province).send_keys('江苏省')
        self.element_find(self.city).send_keys('宿迁市')
        self.element_find(self.area).send_keys('宿城区')
        self.element_find(self.detail_address).send_keys('-修改')
        self.element_find(self.phone).clear()
        self.element_find(self.phone).send_keys('14222222222')
        self.element_find(self.telephone).clear()
        self.element_find(self.telephone).send_keys('020-00000000-0000')
        self.wait_click(self.checkbox_defaultAddress)
        self.wait_click(self.confirm_button)
        time.sleep(2)
        receiver_name = self.element_find(self.receiver).text
        assert receiver_name == '测试-修改'
        print('通用地址修改成功！')

    def set_default_currency_address(self):
        ###设置默认通用地址###
        receiver = self.element_find(self.receiver)
        ActionChains(self.driver).move_to_element(receiver).perform()
        self.wait_click(self.default_address_button)
        default_address_lable = self.element_find(self.default_address_lable).text
        assert default_address_lable == '默认通用地址'
        print('默认通用地址设置成功！')

    def delete_currency_address(self):
        ###删除通用地址###
        address_num = self.element_find(self.address_num).text
        del_front_num = address_num[4:5]
        self.wait_click(self.delete_address)
        self.wait_click(self.confirm)
        time.sleep(2)
        address_num = self.element_find(self.address_num).text
        del_after_num = address_num[4:5]
        assert int(del_front_num) == int(del_after_num) + 1
        print('通用地址删除成功！')

    def add_receive_address(self):
        ###添加收货地址###
        self.wait_click(self.receive_address)
        address_num = self.element_find(self.address_num).text
        add_front_num = address_num[4:5]
        self.wait_click(self.add_address)
        self.element_find(self.receiver_name).send_keys('测试')
        self.element_find(self.company_name).send_keys('测试公司')
        self.element_find(self.province).send_keys('安徽省')
        self.element_find(self.city).send_keys('安庆市')
        self.element_find(self.area).send_keys('迎江区')
        self.element_find(self.detail_address).send_keys('测试地址')
        self.element_find(self.phone).send_keys('13111111111')
        self.element_find(self.telephone).send_keys('020-88888888-8888')
        self.wait_click(self.checkbox_defaultAddress)
        self.wait_click(self.confirm_button)
        time.sleep(2)
        address_num = self.element_find(self.address_num).text
        add_after_num = address_num[4:5]
        assert int(add_after_num) == int(add_front_num) + 1
        print('收货地址添加成功！')

    def edit_receive_address(self):
        ###编辑收货地址###
        self.wait_click(self.edit_address)
        self.element_find(self.receiver_name).send_keys('-修改')
        self.element_find(self.company_name).send_keys('-修改')
        self.element_find(self.province).send_keys('江苏省')
        self.element_find(self.city).send_keys('宿迁市')
        self.element_find(self.area).send_keys('宿城区')
        self.element_find(self.detail_address).send_keys('-修改')
        self.element_find(self.phone).clear()
        self.element_find(self.phone).send_keys('14222222222')
        self.element_find(self.telephone).clear()
        self.element_find(self.telephone).send_keys('020-00000000-0000')
        self.wait_click(self.checkbox_defaultAddress)
        self.wait_click(self.confirm_button)
        time.sleep(2)
        receiver_name = self.element_find(self.receiver).text
        assert receiver_name == '测试-修改'
        print('收货地址修改成功！')

    def set_default_receive_address(self):
        ###设置默认收货地址###
        receiver = self.element_find(self.receiver)
        ActionChains(self.driver).move_to_element(receiver).perform()
        self.wait_click(self.default_address_button)
        default_address_lable = self.element_find(self.default_address_lable).text
        assert default_address_lable == '默认收货地址'
        print('默认收货地址设置成功！')

    def delete_receive_address(self):
        ###删除收货地址###
        address_num = self.element_find(self.address_num).text
        del_front_num = address_num[4:5]
        self.wait_click(self.delete_address)
        self.wait_click(self.confirm)
        time.sleep(2)
        address_num = self.element_find(self.address_num).text
        del_after_num = address_num[4:5]
        assert int(del_front_num) == int(del_after_num) + 1
        print('收货地址删除成功！')

    def add_invoice_address(self):
        ###添加发票地址###
        self.wait_click(self.invoice_address)
        address_num = self.element_find(self.address_num).text
        add_front_num = address_num[4:5]
        self.wait_click(self.add_address)
        self.element_find(self.receiver_name).send_keys('测试')
        self.element_find(self.company_name).send_keys('测试公司')
        self.element_find(self.province).send_keys('安徽省')
        self.element_find(self.city).send_keys('安庆市')
        self.element_find(self.area).send_keys('迎江区')
        self.element_find(self.detail_address).send_keys('测试地址')
        self.element_find(self.phone).send_keys('13111111111')
        self.element_find(self.telephone).send_keys('020-88888888-8888')
        self.wait_click(self.checkbox_defaultAddress)
        self.wait_click(self.confirm_button)
        time.sleep(2)
        address_num = self.element_find(self.address_num).text
        add_after_num = address_num[4:5]
        assert int(add_after_num) == int(add_front_num) + 1
        print('发票地址添加成功！')

    def edit_invoice_address(self):
        ###编辑发票地址###
        self.wait_click(self.edit_address)
        self.element_find(self.receiver_name).send_keys('-修改')
        self.element_find(self.company_name).send_keys('-修改')
        self.element_find(self.province).send_keys('江苏省')
        self.element_find(self.city).send_keys('宿迁市')
        self.element_find(self.area).send_keys('宿城区')
        self.element_find(self.detail_address).send_keys('-修改')
        self.element_find(self.phone).clear()
        self.element_find(self.phone).send_keys('14222222222')
        self.element_find(self.telephone).clear()
        self.element_find(self.telephone).send_keys('020-00000000-0000')
        self.wait_click(self.checkbox_defaultAddress)
        self.wait_click(self.confirm_button)
        time.sleep(2)
        receiver_name = self.element_find(self.receiver).text
        assert receiver_name == '测试-修改'
        print('发票地址修改成功！')

    def set_default_invoice_address(self):
        ###设置默认发票地址###
        receiver = self.element_find(self.receiver)
        ActionChains(self.driver).move_to_element(receiver).perform()
        self.wait_click(self.default_address_button)
        default_address_lable = self.element_find(self.default_address_lable).text
        assert default_address_lable == '默认发票地址'
        print('默认发票地址设置成功！')

    def delete_invoice_address(self):
        ###删除发票地址###
        address_num = self.element_find(self.address_num).text
        del_front_num = address_num[4:5]
        self.wait_click(self.delete_address)
        self.wait_click(self.confirm)
        time.sleep(2)
        address_num = self.element_find(self.address_num).text
        del_after_num = address_num[4:5]
        assert int(del_front_num) == int(del_after_num) + 1
        print('发票地址删除成功！')