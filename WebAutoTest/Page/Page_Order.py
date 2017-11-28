from Page_Base import Page
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, WebDriverException


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
    setDefaultAddress = ('by.name', 'is_default')
    add_confirm = ('by.class_name', 'confirm')
    receiving_address_layer = ('by.class_name', 'content')

    # 编辑收货地址
    address_edit = ('by.xpath', '//ul/li[1]/a[2]')
    edit_confirm = ('by.class_name', 'confirm')

    # 删除收货地址
    address_del = ('by.xpath', '//*[@id="js-shipping-address-id"]/ul/li[1]/a[1]')
    del_confirm = ('by.xpath', '//div[3]/div[1]/button[2]')

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

    close = ('by.class_name', 'close')

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

    def add_receiving_address(self):
        self.element_find(self.receiving_address_add).click()
        self.element_find(self.receiving_name).send_keys('自动化测试')
        self.element_find(self.company_name).send_keys('自动化测试公司')
        self.element_find(self.province).send_keys('安徽省')
        self.element_find(self.city).send_keys('安庆市')
        self.element_find(self.area).send_keys('望江县')
        self.element_find(self.detailed_address).send_keys('自动化测试地址')
        self.element_find(self.receiving_phone).send_keys('15150681507')
        self.element_find(self.setDefaultAddress).click()
        self.element_find(self.add_confirm).click()
        message = self.element_find(self.receiving_address_layer).text
        assert message == '地址添加成功！'
        self.wait_to_stale(self.receiving_address_layer)
        print('收货地址添加成功')

    def receiving_address_edit(self):
        element = self.element_find(self.address_edit)
        ActionChains(self.driver).move_to_element(element).perform()     # 鼠标悬停展现不可见的编辑按钮
        element = self.wait_to_clickable(self.address_edit)
        element.click()
        self.element_find(self.receiving_name).send_keys('修改')
        self.element_find(self.company_name).send_keys('修改')
        self.element_find(self.province).send_keys('江苏省')
        self.element_find(self.city).send_keys('南京市')
        self.element_find(self.area).send_keys('江宁区')
        self.element_find(self.detailed_address).send_keys('修改')
        mobile = self.element_find(self.receiving_phone)
        mobile.send_keys(Keys.BACK_SPACE)
        mobile.send_keys('8')
        self.element_find(self.edit_confirm).click()
        message = self.element_find(self.receiving_address_layer).text
        assert message == '地址编辑成功！'
        self.wait_to_stale(self.receiving_address_layer)
        print('收货地址修改成功')

    def receiving_address_delete(self):
        element = self.element_find(self.address_del)
        ActionChains(self.driver).move_to_element(element).perform()
        element = self.wait_to_clickable(self.address_del)
        element.click()
        self.element_find(self.del_confirm).click()
        message = self.element_find(self.receiving_address_layer).text
        assert message == '地址删除成功！'
        self.wait_to_stale(self.receiving_address_layer)
        print('收货地址删除成功')

    def invoice_normal_company_add(self):
        """新增公司抬头的普票"""
        self.element_find(self.choose).click()  # 请选择按钮
        self.element_find(self.normal_invoice_add).click()
        self.element_find(self.invoice_title).send_keys('公司抬头普票')
        self.element_find(self.tax_no).send_keys('1234567890qwert')
        self.element_find(self.normal_invoice_save).click()
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息添加成功！'
        self.wait_to_stale(self.invoice_layer)
        print('普通发票-公司抬头添加成功')

    def invoice_normal_personal_add(self):
        """新增个人抬头的普票"""
        self.element_find(self.choose).click()  # 请选择按钮
        self.element_find(self.normal_invoice_add).click()
        self.element_find(self.choose_invoice_title).send_keys('个人抬头')
        self.element_find(self.invoice_title).send_keys('个人抬头普票')
        self.element_find(self.normal_invoice_save).click()
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息添加成功！'
        self.wait_to_stale(self.invoice_layer)
        print('普通发票-个人抬头添加成功')

    def invoice_normal_personal_edit(self):
        self.element_find(self.choose).click()  # 请选择按钮
        element = self.element_find(self.first_normal_invoice)
        ActionChains(self.driver).move_to_element(element).perform()
        self.element_find(self.normal_invoice_edit).click()
        self.element_find(self.choose_invoice_title).send_keys('个人抬头')
        self.element_find(self.invoice_title).send_keys('修改')
        self.element_find(self.normal_invoice_save).click()
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息编辑成功！'
        self.wait_to_stale(self.invoice_layer)
        print('普通发票-个人抬头编辑成功')

    def invoice_normal_company_edit(self):
        self.element_find(self.choose).click()  # 请选择按钮
        element = self.element_find(self.first_normal_invoice)
        ActionChains(self.driver).move_to_element(element).perform()
        self.element_find(self.normal_invoice_edit).click()
        self.element_find(self.invoice_title).send_keys('修改')
        ele = self.element_find(self.tax_no)
        ele.send_keys(Keys.BACK_SPACE)
        ele.send_keys('1')
        self.element_find(self.normal_invoice_save).click()
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息编辑成功！'
        self.wait_to_stale(self.invoice_layer)
        print('普通发票-公司抬头编辑成功')

    def invoice_normal_delete(self):
        """删除普通发票"""
        self.element_find(self.choose).click()  # 请选择按钮
        self.element_find(self.normal_invoice_tab).click()
        element = self.element_find(self.first_normal_invoice)
        ActionChains(self.driver).move_to_element(element).perform()
        self.element_find(self.normal_invoice_del).click()
        self.element_find(self.normal_invoice_del_confirm).click()
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息删除成功！'
        self.wait_to_stale(self.invoice_layer)
        print('普通发票删除成功')

    def invoice_vat_delete(self):
        """删除增值税发票"""
        self.element_find(self.choose).click()  # 请选择按钮
        self.element_find(self.vat_invoice_tab).click()
        element = self.element_find(self.first_bill)
        ActionChains(self.driver).move_to_element(element).perform()
        self.element_find(self.bill_del).click()
        self.element_find(self.bill_del_confirm).click()
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息删除成功！'
        self.wait_to_stale(self.invoice_layer)
        print('增值税发票删除成功')

    def invoice_vat_add(self):
        self.element_find(self.choose).click()  # 请选择按钮
        self.element_find(self.vat_invoice_tab).click()
        self.element_find(self.bill_add).click()
        self.element_find(self.bill_title).send_keys('自动化测试增票')
        self.element_find(self.bill_tax_no).send_keys('1234567890123qwert')
        self.element_find(self.bill_address).send_keys('上海市浦东新区凌阳大厦')
        self.element_find(self.bill_phone).send_keys('15150681507')
        self.element_find(self.bill_bank).send_keys('上海银行')
        self.element_find(self.bill_bank_account).send_keys('123456')
        self.element_find(self.bill_set_default).click()
        self.element_find(self.bill_save).click()
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息添加成功！'
        self.wait_to_stale(self.invoice_layer)
        print('增值税发票添加成功')

    def invoice_vat_edit(self):
        """删除增值税发票"""
        self.element_find(self.choose).click()  # 请选择按钮
        self.element_find(self.vat_invoice_tab).click()
        element = self.element_find(self.first_bill)
        ActionChains(self.driver).move_to_element(element).perform()
        self.element_find(self.bill_edit).click()
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
        self.element_find(self.bill_set_default).click()
        self.element_find(self.bill_save).click()
        message = self.element_find(self.invoice_layer).text
        assert message == '发票信息编辑成功！'
        self.wait_to_stale(self.invoice_layer)
        print('增值税发票编辑成功')

    def choose_normal_invoice(self):
        """选择普票"""
        self.element_find(self.choose).click()
        self.element_find(self.normal_invoice_tab).click()
        self.element_find(self.first_normal_invoice).click()
        self.element_find(self.close).click()

    def choose_vat_invoice(self):
        """选择增票"""
        element = self.element_find(self.choose)
        element.click()
        self.element_find(self.vat_invoice_tab).click()
        self.element_find(self.first_bill).click()
        self.element_find(self.close).click()

    def choose_none_invoice(self):
        """选择不开票"""
        self.wait_click(self.choose)
        self.wait_click(self.none_invoice_tab)
        self.wait_click(self.close)

    def normal_invoice_check(self):
        self.element_find(self.choose).click()  # 请选择按钮
        self.element_find(self.normal_invoice_add).click()
        # self.element_find(self.invoice_title).send_keys('公司抬头普票')
        self.element_find(self.tax_no).send_keys('1234567890qwert')
        # self.element_find(self.normal_invoice_save).click()
        #
        # message = self.element_find(self.invoice_layer).text
        # self.element_find(self.choose_invoice_title).send_keys('个人抬头')
        # self.element_find(self.invoice_title).send_keys('个人抬头普票')
        # self.element_find(self.normal_invoice_save).click()
        # message = self.element_find(self.invoice_layer).text
        # assert message == '发票信息添加成功！'
        # self.wait_to_stale(self.invoice_layer)
        # print('普通发票-个人抬头添加成功')

