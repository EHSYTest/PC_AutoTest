from Page_Base import Page
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, WebDriverException
from selenium.webdriver.common.alert import Alert


class Order(Page):
    """下单页"""
    # 新增收货地址
    receiving_address_add = ('by.link_text', '+添加新地址')
    receiving_name = ('by.name', 'receiver_name')
    company_name = ('by.name', 'company_name')
    province = ('by.name', 'province_id')
    city = ('by.name', 'city_id')
    area = ('by.name', 'area_id')
    detailed_address = ('by.name', 'detail_address')
    receiving_phone = ('by.name', 'cell_phone')
    receiving_telephone = ('by.name', 'telephone')
    setDefaultAddress = ('by.name', 'is_default')
    add_confirm = ('by.class_name', 'confirm')
    receiving_address_layer = ('by.class_name', 'content')
    receiving_address = ('by.class_name', 'list-li')   # find elements

    # 编辑收货地址
    address_edit = ('by.xpath', '//ul/li[1]/a[2]')
    edit_confirm = ('by.class_name', 'confirm')

    # 删除收货地址
    address_del = ('by.xpath', '//*[@id="js-shipping-address-id"]/ul/li[1]/a[1]')
    del_confirm = ('by.xpath', '//div[3]/div[1]/button[2]')

    # 收货地址填写提示
    address_alert = ('by.class_name', 'error')
    phone_alert = ('by.xpath', '//p[7]/span')

    # 普通发票
    choose = ('by.link_text', '请选择')
    normal_invoice_add = ('by.link_text', '+新增普通发票')
    choose_invoice_title = ('by.name', 'sub_type')
    invoice_title = ('by.name', 'title')
    tax_no = ('by.name', 'tax_no')
    normal_invoice_save = ('by.class_name', 'confirm')
    invoice_layer = ('by.xpath', '//*[@id="js-layer-notice"]')
    first_normal_invoice = ('by.xpath', '//div[2]/div/p[1]')
    normal_invoice_del = ('by.xpath', '//p[1]/span[2]/a[2]')
    normal_invoice_edit = ('by.xpath', '//*[@id="js-invoice-info-1"]/p[1]/span[2]/a[1]')
    normal_invoice_del_confirm = ('by.xpath', '//div[3]/div[1]/button[2]')
    normal_invoice_tab = ('by.xpath', "//ul/li[1][contains(text(),'普通发票')]")
    div_alert = ('by.xpath', '//*[@id="js-layer-alert"]/div[1]/div[2]/div')    
    alert_confirm = ('by.xpath', '//div[1]/div[3]/div[1]/button')
    confirm = ('by.class_name', 'confirm')

    # 增值税发票
    vat_invoice_tab = ('by.xpath', "//ul/li[2][contains(text(),'增值税发票')]")
    bill_add = ('by.link_text', '+新增增值税发票')
    bill_title = ('by.name', 'title')
    bill_tax_no = ('by.name', 'tax_no')
    bill_address = ('by.name', 'company_address')
    bill_phone = ('by.name', 'telephone')
    bill_bank = ('by.name', 'bank_name')
    bill_bank_account = ('by.name', 'bank_account')
    bill_set_default = ('by.name', 'is_default_invoice')
    bill_save = ('by.class_name', 'confirm')
    first_bill = ('by.xpath', '//*[@id="js-invoice-info-2"]/p')
    bill_del = ('by.xpath', '//*[@id="js-invoice-info-2"]/p[1]/span[2]/a[2]')
    bill_edit = ('by.xpath', '//*[@id="js-invoice-info-2"]/p[1]/span[2]/a[1]')
    bill_del_confirm = ('by.xpath', '//div[3]/div[1]/button[2]')

    # 不开发票
    none_invoice_tab = ('by.xpath', "//ul/li[3][contains(text(),'不开发票')]")

    # 提交订单
    submit_order_button = ('by.class_name', 'btn-order-submit')
    notice_layer = ('by.xpath', '//button[@class="confirm"]')
    # none_invoice_layer = ('by.class_name', 'layui-layer-btn0')
    # choose_approve_flow = ('by.name', 'approveFlowItem')
    # submit_approve_flow = ('by.class_name', 'eps-submit-btn')

    choose_eas_flow = ('by.class_name', 'eps-approveflowId ')

    def add_receiving_address(self):
        self.wait_click(self.receiving_address_add)
        self.element_find(self.receiving_name).send_keys('自动化测试')
        self.element_find(self.company_name).send_keys('自动化测试公司')
        self.element_find(self.province).send_keys('安徽省')
        self.element_find(self.city).send_keys('安庆市')
        self.element_find(self.area).send_keys('望江县')
        self.element_find(self.detailed_address).send_keys('自动化测试地址')
        self.element_find(self.receiving_phone).send_keys('15150681507')
        self.wait_click(self.setDefaultAddress)
        self.wait_click(self.add_confirm)
        message = self.element_find(self.receiving_address_layer).text
        assert message == '地址添加成功！'
        print('收货地址添加成功')

    def receiving_address_edit(self):
        element = self.element_find(self.address_edit)
        ActionChains(self.driver).move_to_element(element).perform()     # 鼠标悬停展现不可见的编辑按钮
        self.wait_click(self.address_edit)
        self.element_find(self.receiving_name).send_keys('修改')
        self.element_find(self.company_name).send_keys('修改')
        self.element_find(self.province).send_keys('江苏省')
        self.element_find(self.city).send_keys('南京市')
        self.element_find(self.area).send_keys('江宁区')
        self.element_find(self.detailed_address).send_keys('修改')
        mobile = self.element_find(self.receiving_phone)
        mobile.send_keys(Keys.BACK_SPACE)
        mobile.send_keys('8')
        self.wait_click(self.edit_confirm)
        message = self.element_find(self.receiving_address_layer).text
        assert message == '地址编辑成功！'
        print('收货地址修改成功')

    def receiving_address_delete(self):
        element = self.element_find(self.address_del)
        ActionChains(self.driver).move_to_element(element).perform()
        self.wait_click(self.address_del)
        self.wait_click(self.del_confirm)
        message = self.element_find(self.receiving_address_layer).text
        assert message == '地址删除成功！'
        print('收货地址删除成功')

    def receiving_address_check(self):
        self.wait_click(self.receiving_address_add)     # 添加收货地址按钮

        # 收货人不能为空
        self.element_find(self.company_name).send_keys('自动化测试公司')
        self.element_find(self.province).send_keys('安徽省')
        self.element_find(self.city).send_keys('安庆市')
        self.element_find(self.area).send_keys('望江县')
        self.element_find(self.detailed_address).send_keys('自动化测试地址')
        self.element_find(self.receiving_phone).send_keys('15150681507')
        self.element_find(self.receiving_telephone).send_keys('021-05562345')
        self.wait_click(self.add_confirm)
        message = self.element_find(self.address_alert).text
        assert message == '请填写收件人名称'

        # 省市区不能为空
        self.element_find(self.receiving_name).send_keys('自动化测试')
        self.element_find(self.province).send_keys('请选择省份')
        self.wait_click(self.add_confirm)
        message = self.element_find(self.address_alert).text
        assert message == '请选择省、市、区'
        self.element_find(self.province).send_keys('安徽省')
        self.wait_click(self.add_confirm)
        message = self.element_find(self.address_alert).text
        assert message == '请选择省、市、区'
        self.element_find(self.city).send_keys('安庆市')
        self.wait_click(self.add_confirm)
        message = self.element_find(self.address_alert).text
        assert message == '请选择省、市、区'

        # 详细地址不能为空
        self.element_find(self.area).send_keys('望江县')
        self.element_find(self.detailed_address).clear()
        self.wait_click(self.add_confirm)
        message = self.element_find(self.address_alert).text
        assert message == '请填写详细地址'

        # 手机号不能为10位
        self.element_find(self.detailed_address).send_keys('自动化测试地址')
        self.element_find(self.receiving_phone).send_keys(Keys.BACK_SPACE)
        self.wait_click(self.add_confirm)
        message = self.element_find(self.address_alert).text
        assert message == '请输入正确的手机号码'

        # 手机号不能为12位
        self.element_find(self.receiving_phone).send_keys('77')
        self.wait_click(self.add_confirm)
        message = self.element_find(self.address_alert).text
        assert message == '请输入正确的手机号码'

        # 手机号首位为1
        for i in ('0', '2', '3', '4', '5', '6', '7', '8', '9'):
            self.element_find(self.receiving_phone).clear()
            self.element_find(self.receiving_phone).send_keys(i+'5150681507')
            self.wait_click(self.add_confirm)
            message = self.element_find(self.address_alert).text
            assert message == '请输入正确的手机号码'

        # 手机号第二位为3,4,5,7,8
        for i in ('0', '1', '2', '6', '9'):
            self.element_find(self.receiving_phone).clear()
            self.element_find(self.receiving_phone).send_keys('1'+i+'150681507')
            self.wait_click(self.add_confirm)
            message = self.element_find(self.address_alert).text
            assert message == '请输入正确的手机号码'
        self.element_find(self.receiving_phone).clear()
        self.element_find(self.receiving_phone).send_keys('13150681507')
        self.wait_click(self.add_confirm)
        message = self.element_find(self.receiving_address_layer).text
        assert message == '地址添加成功！'
        for i in ('4', '5', '7', '8'):
            element = self.element_find(self.address_edit)
            ActionChains(self.driver).move_to_element(element).perform()  # 鼠标悬停展现不可见的编辑按钮
            self.wait_click(self.address_edit)
            self.element_find(self.receiving_phone).clear()
            self.element_find(self.receiving_phone).send_keys('1' + i + '150681507')
            self.wait_click(self.add_confirm)
            message = self.element_find(self.receiving_address_layer).text
            assert message == '地址编辑成功！'

        # 手机固话至少填一个
        element = self.element_find(self.address_edit)
        ActionChains(self.driver).move_to_element(element).perform()  # 鼠标悬停展现不可见的编辑按钮
        self.wait_click(self.address_edit)
        self.element_find(self.receiving_phone).clear()
        self.element_find(self.receiving_telephone).clear()
        self.element_find(self.receiving_phone).send_keys('15150681507')
        self.wait_click(self.add_confirm)
        message = self.element_find(self.receiving_address_layer).text
        assert message == '地址编辑成功！'

        element = self.element_find(self.address_edit)
        ActionChains(self.driver).move_to_element(element).perform()  # 鼠标悬停展现不可见的编辑按钮
        self.wait_click(self.address_edit)
        self.element_find(self.receiving_phone).clear()
        self.element_find(self.receiving_telephone).clear()
        self.element_find(self.receiving_telephone).send_keys('021-05562345')
        self.wait_click(self.add_confirm)
        message = self.element_find(self.receiving_address_layer).text
        assert message == '地址编辑成功！'

        element = self.element_find(self.address_edit)
        ActionChains(self.driver).move_to_element(element).perform()  # 鼠标悬停展现不可见的编辑按钮
        self.wait_click(self.address_edit)
        self.element_find(self.receiving_phone).clear()
        self.element_find(self.receiving_telephone).clear()
        self.element_find(self.receiving_phone).send_keys('15150681507')
        self.element_find(self.receiving_telephone).send_keys('021-05562345')
        self.wait_click(self.add_confirm)
        message = self.element_find(self.receiving_address_layer).text
        assert message == '地址编辑成功！'

        # 公司名称选填
        element = self.element_find(self.address_edit)
        ActionChains(self.driver).move_to_element(element).perform()  # 鼠标悬停展现不可见的编辑按钮
        self.wait_click(self.address_edit)
        self.element_find(self.company_name).clear()
        self.wait_click(self.add_confirm)
        message = self.element_find(self.receiving_address_layer).text
        assert message == '地址编辑成功！'

    def invoice_normal_company_add(self):
        """新增公司抬头的普票"""
        self.wait_click(self.choose)  # 请选择按钮
        self.wait_click(self.normal_invoice_add)
        self.element_find(self.invoice_title).send_keys('公司抬头普票')
        self.element_find(self.tax_no).send_keys('1234567890qwert')
        self.wait_click(self.normal_invoice_save)
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息添加成功！'
        print('普通发票-公司抬头添加成功')

    def invoice_normal_personal_add(self):
        """新增个人抬头的普票"""
        self.wait_click(self.choose)  # 请选择按钮
        self.wait_click(self.normal_invoice_add)
        self.element_find(self.choose_invoice_title).send_keys('个人抬头')
        self.element_find(self.invoice_title).send_keys('个人抬头普票')
        self.wait_click(self.normal_invoice_save)
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息添加成功！'
        print('普通发票-个人抬头添加成功')

    def invoice_normal_personal_edit(self):
        self.wait_click(self.choose) # 请选择按钮
        element = self.element_find(self.first_normal_invoice)
        ActionChains(self.driver).move_to_element(element).perform()
        self.wait_click(self.normal_invoice_edit)
        self.element_find(self.choose_invoice_title).send_keys('个人抬头')
        self.element_find(self.invoice_title).send_keys('修改')
        self.wait_click(self.normal_invoice_save)
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息编辑成功！'
        print('普通发票-个人抬头编辑成功')

    def invoice_normal_company_edit(self):
        self.wait_click(self.choose)   # 请选择按钮
        element = self.element_find(self.first_normal_invoice)
        ActionChains(self.driver).move_to_element(element).perform()
        self.wait_click(self.normal_invoice_edit)
        self.element_find(self.invoice_title).send_keys('修改')
        ele = self.element_find(self.tax_no)
        ele.send_keys(Keys.BACK_SPACE)
        ele.send_keys('1')
        self.wait_click(self.normal_invoice_save)
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息编辑成功！'
        print('普通发票-公司抬头编辑成功')

    def invoice_normal_delete(self):
        """删除普通发票"""
        self.wait_click(self.choose)  # 请选择按钮
        self.wait_click(self.normal_invoice_tab)
        element = self.element_find(self.first_normal_invoice)
        ActionChains(self.driver).move_to_element(element).perform()
        self.wait_click(self.normal_invoice_del)
        self.wait_click(self.normal_invoice_del_confirm)
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息删除成功！'
        print('普通发票删除成功')

    def invoice_vat_delete(self):
        """删除增值税发票"""
        self.wait_click(self.choose)   # 请选择按钮
        self.wait_click(self.vat_invoice_tab)
        element = self.element_find(self.first_bill)
        ActionChains(self.driver).move_to_element(element).perform()
        self.wait_click(self.bill_del)
        self.wait_click(self.bill_del_confirm)
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息删除成功！'
        print('增值税发票删除成功')

    def invoice_vat_add(self):
        self.wait_click(self.choose)# 请选择按钮
        self.wait_click(self.vat_invoice_tab)
        self.wait_click(self.bill_add)
        self.element_find(self.bill_title).send_keys('自动化测试增票')
        self.element_find(self.bill_tax_no).send_keys('1234567890123qwert')
        self.element_find(self.bill_address).send_keys('上海市浦东新区凌阳大厦')
        self.element_find(self.bill_phone).send_keys('15150681507')
        self.element_find(self.bill_bank).send_keys('上海银行')
        self.element_find(self.bill_bank_account).send_keys('123456')
        self.wait_click(self.bill_set_default)
        self.wait_click(self.bill_save)
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息添加成功！'
        print('增值税发票添加成功')

    def invoice_vat_edit(self):
        """删除增值税发票"""
        self.wait_click(self.choose)  # 请选择按钮
        self.wait_click(self.vat_invoice_tab)
        element = self.element_find(self.first_bill)
        ActionChains(self.driver).move_to_element(element).perform()
        self.wait_click(self.bill_edit)
        self.element_find(self.bill_title).send_keys('修改')
        ele = self.element_find(self.bill_tax_no)
        ele.send_keys(Keys.BACK_SPACE)
        ele.send_keys('w')
        self.element_find(self.bill_address).send_keys('修改')
        ele = self.element_find(self.bill_phone)
        ele.send_keys(Keys.BACK_SPACE)
        ele.send_keys('6')
        self.element_find(self.bill_bank).send_keys('修改')
        self.element_find(self.bill_bank_account).send_keys('78')
        self.wait_click(self.bill_set_default)
        self.wait_click(self.bill_save)
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息编辑成功！'
        print('增值税发票编辑成功')

    def choose_normal_invoice(self):
        """选择普票"""
        self.wait_click(self.choose)
        self.wait_click(self.normal_invoice_tab)
        self.wait_click(self.first_normal_invoice)
        self.wait_click(self.confirm)

    def choose_vat_invoice(self):
        """选择增票"""
        self.wait_click(self.choose)
        self.wait_click(self.vat_invoice_tab)
        self.wait_click(self.first_bill)
        self.wait_click(self.confirm)

    def choose_none_invoice(self):
        """选择不开票"""
        self.wait_click(self.choose)
        self.wait_click(self.none_invoice_tab)
        self.wait_click(self.confirm)

    def normal_invoice_check(self):
        self.wait_click(self.choose)  # 请选择按钮
        self.wait_click(self.normal_invoice_tab)
        self.wait_click(self.normal_invoice_add)

        # 发票抬头不为空
        self.element_find(self.choose_invoice_title).send_keys('个人抬头')
        self.wait_click(self.normal_invoice_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入发票抬头'
        self.wait_click(self.alert_confirm)

        # 税号不为空
        self.element_find(self.choose_invoice_title).send_keys('公司抬头')
        self.element_find(self.invoice_title).send_keys('测试发票')
        self.wait_click(self.normal_invoice_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入税号'
        self.wait_click(self.alert_confirm)

        # 税号不能为14位
        self.element_find(self.tax_no).send_keys('12345678909876')
        self.wait_click(self.normal_invoice_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入15位或18位纳税人识别码'
        self.wait_click(self.alert_confirm)

        # 税号不能为16位
        self.element_find(self.tax_no).send_keys(54)
        self.wait_click(self.normal_invoice_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入15位或18位纳税人识别码'
        self.wait_click(self.alert_confirm)

        # 税号不能为17位
        self.element_find(self.tax_no).send_keys(3)
        self.wait_click(self.normal_invoice_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入15位或18位纳税人识别码'
        self.wait_click(self.alert_confirm)

        # 税号不能为19位
        self.element_find(self.tax_no).send_keys(21)
        self.wait_click(self.normal_invoice_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入15位或18位纳税人识别码'
        self.wait_click(self.alert_confirm)

        # 税号不能含特殊字符
        self.element_find(self.tax_no).send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, '$')
        self.wait_click(self.normal_invoice_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入15位或18位纳税人识别码'
        self.wait_click(self.alert_confirm)

        # 发票抬头不能为空
        self.element_find(self.invoice_title).clear()
        self.element_find(self.tax_no).send_keys(Keys.BACK_SPACE, 'A')
        self.wait_click(self.normal_invoice_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入发票抬头'
        self.wait_click(self.alert_confirm)

        # 发票抬头不能全数字
        self.element_find(self.invoice_title).send_keys('111')
        self.wait_click(self.normal_invoice_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '公司名称不能全数字！'
        self.wait_click(self.alert_confirm)

        # 公司名称不能全字母
        self.element_find(self.invoice_title).clear()
        self.element_find(self.invoice_title).send_keys('AAA')
        self.wait_click(self.normal_invoice_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '公司名称不能全字母！'
        self.wait_click(self.alert_confirm)

        # 发票抬头不能包含特殊字符
        self.element_find(self.invoice_title).clear()
        self.element_find(self.invoice_title).send_keys('@123')
        self.wait_click(self.normal_invoice_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '公司名称只能由中文、英文、数字（）()组成'
        self.wait_click(self.alert_confirm)

        # 发票抬头可以包含中文、英文、数字（）()和_-
        self.element_find(self.invoice_title).clear()
        self.element_find(self.invoice_title).send_keys('（Test测试111_-()）')
        self.wait_click(self.normal_invoice_save)
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息添加成功！'

        # 删除添加的发票
        element = self.element_find(self.first_normal_invoice)
        ActionChains(self.driver).move_to_element(element).perform()
        self.wait_click(self.normal_invoice_del)
        self.wait_click(self.normal_invoice_del_confirm)
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息删除成功！'

    def vat_invoice_check(self):
        self.wait_click(self.choose)    # 请选择按钮
        self.wait_click(self.vat_invoice_tab)
        self.wait_click(self.bill_add)

        # 单位名称不为空
        self.element_find(self.bill_tax_no).send_keys('1234567890123qwert')
        self.element_find(self.bill_address).send_keys('上海市浦东新区凌阳大厦')
        self.element_find(self.bill_phone).send_keys('15150681507')
        self.element_find(self.bill_bank).send_keys('上海银行')
        self.element_find(self.bill_bank_account).send_keys('123456')
        self.wait_click(self.bill_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入单位名称'
        self.wait_click(self.alert_confirm)

        # 发票抬头不能全数字
        self.element_find(self.bill_title).send_keys('111')
        self.wait_click(self.normal_invoice_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '公司名称不能全数字！'
        self.wait_click(self.alert_confirm)

        # 公司名称不能全字母
        self.element_find(self.bill_title).clear()
        self.element_find(self.bill_title).send_keys('AAA')
        self.wait_click(self.normal_invoice_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '公司名称不能全字母！'
        self.wait_click(self.alert_confirm)

        # 发票抬头不能包含特殊字符
        self.element_find(self.bill_title).clear()
        self.element_find(self.bill_title).send_keys('@123')
        self.wait_click(self.normal_invoice_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '公司名称只能由中文、英文、数字（）()组成'
        self.wait_click(self.alert_confirm)

        # 注册地址不为空
        self.element_find(self.bill_title).clear()
        self.element_find(self.bill_title).send_keys('（Test测试111_-()）')
        self.element_find(self.bill_address).clear()
        self.wait_click(self.bill_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入注册地址'
        self.wait_click(self.alert_confirm)

        # 注册电话不为空
        self.element_find(self.bill_address).send_keys('上海市浦东新区凌阳大厦')
        self.element_find(self.bill_phone).clear()
        self.wait_click(self.bill_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入注册电话'
        self.wait_click(self.alert_confirm)

        # 开户银行不为空
        self.element_find(self.bill_phone).send_keys('15150681507')
        self.element_find(self.bill_bank).clear()
        self.wait_click(self.bill_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入开户银行'
        self.wait_click(self.alert_confirm)

        # 银行账号不为空
        self.element_find(self.bill_bank).send_keys('上海银行')
        self.element_find(self.bill_bank_account).clear()
        self.wait_click(self.bill_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入银行账号'
        self.wait_click(self.alert_confirm)

        # 税号不为空
        self.element_find(self.bill_bank_account).send_keys('123456')
        self.element_find(self.bill_tax_no).clear()
        self.wait_click(self.bill_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入纳税人识别码'
        self.wait_click(self.alert_confirm)

        # 税号不为14位
        self.element_find(self.bill_tax_no).send_keys('12345678901234')
        self.wait_click(self.bill_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入15位或18位纳税人识别码'
        self.wait_click(self.alert_confirm)

        # 税号不为16位
        self.element_find(self.bill_tax_no).send_keys('56')
        self.wait_click(self.bill_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入15位或18位纳税人识别码'
        self.wait_click(self.alert_confirm)

        # 税号不为17位
        self.element_find(self.bill_tax_no).send_keys('7')
        self.wait_click(self.bill_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入15位或18位纳税人识别码'
        self.wait_click(self.alert_confirm)

        # 税号不为19位
        self.element_find(self.bill_tax_no).send_keys('89')
        self.wait_click(self.bill_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入15位或18位纳税人识别码'
        self.wait_click(self.alert_confirm)

        # 税号不含特殊字符
        self.element_find(self.bill_tax_no).send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, '￥')
        self.wait_click(self.bill_save)
        alert_text = self.element_find(self.div_alert).text
        assert alert_text == '请输入15位或18位纳税人识别码'
        self.wait_click(self.alert_confirm)

        self.element_find(self.bill_tax_no).send_keys(Keys.BACK_SPACE, 'A')
        self.wait_click(self.bill_save)
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息添加成功！'

        # 删除添加的发票
        element = self.element_find(self.first_bill)
        ActionChains(self.driver).move_to_element(element).perform()
        self.wait_click(self.bill_del)
        self.wait_click(self.bill_del_confirm)
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息删除成功！'
