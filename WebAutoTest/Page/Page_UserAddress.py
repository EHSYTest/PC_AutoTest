from Page_Base import Page

class UserAddress(Page):
    my_address = ('by.xpath', '//div/ul/li[8]/p/a') #进入我的地址标签页
    add_address = ('by.class_name', 'mod-ra-add-btn') #添加地址按钮
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

    #loading
    layer = ('by.id', 'ajax-layer-loading')

    def add_receive_address(self):
        # self.wait_to_stale(self.layer)
        self.element_find(self.my_address).click()
        address_num = self.element_find(self.address_num).text
        add_front_num = address_num[4:5]
        self.element_find(self.add_address).click()
        self.element_find(self.receiver_name).send_keys('测试')
        self.element_find(self.company_name).send_keys('测试公司')
        self.element_find(self.province).send_keys('安徽省')
        self.element_find(self.city).send_keys('安庆市')
        self.element_find(self.area).send_keys('迎江区')
        self.element_find(self.detail_address).send_keys('测试地址')
        self.element_find(self.phone).send_keys('13111111111')
        self.element_find(self.telephone).send_keys('020-88888888-8888')
        self.element_find(self.checkbox_defaultAddress).click()
        self.element_find(self.confirm_button).click()
        self.wait_to_stale(self.layer)
        address_num = self.element_find(self.address_num).text
        add_after_num = address_num[4:5]
        assert int(add_after_num) == int(add_front_num) + 1
        print('添加地址成功')
