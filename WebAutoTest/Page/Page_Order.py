from Page_Base import Page
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, WebDriverException


class Order(Page):
    """下单页"""
    # 新增收货地址
    receiving_address_add = ('by.xpath', '//div[2]/div[2]/div[1]/a')
    receiving_name = ('by.id', 'receiving_name')
    company_name = ('by.name', 'company_name')
    province = ('by.name', 'province_id')
    city = ('by.name', 'city_id')
    area = ('by.id', 'area_id')
    detailed_address = ('by.name', 'detailed_addr')
    receiving_phone = ('by.name', 'receiving_phone')
    setDefaultAddress = ('by.id', 'setDefaultAddr')
    add_confirm = ('by.xpath', '//form/p[9]/button[1]')
    receiving_address_layer = ('by.xpath', 'html/body/div[4]/div')

    # 编辑收货地址
    address_edit = ('by.xpath', '//div[2]/div[2]/ul/li[1]/a[2]')
    edit_confirm = ('by.xpath', '//form/p[9]/button[2]')

    # 删除收货地址
    address_del = ('by.xpath', '//div[2]/div[2]/div[2]/ul/li[1]/a[1]')
    del_confirm = ('by.xpath', '//div[4]/div[3]/a[1]')

    # 普通发票
    choose = ('by.class_name', 'edit_c_bill')
    normal_invoice_add = ('by.xpath', '//div[1]/div[3]/p/a')
    choose_invoice_title = ('by.class_name', 'select-type')
    company_title = ('by.class_name', 'company-title')
    tax_no = ('by.class_name', 'tax-no')
    normal_invoice_save = ('by.xpath', '//div[3]/div[2]/button[3]')
    invoice_layer = ('by.xpath', 'html/body/div[5]/div')
    first_normal_invoice = ('by.xpath', '//div[3]/div/p[1]')
    normal_invoice_confirm = ('by.xpath', '//div[2]/div[3]/div[2]/button[1]')
    personal_title = ('by.class_name', 'personal-title')
    normal_invoice_del = ('by.class_name', 'sprite-order_delete')
    normal_invoice_del_confirm = ('by.class_name', 'html/body/div[5]/div[3]/a[1]')
    normal_invoice_cancel = ('by.xpath', '//div[3]/div[2]/button[2]')
    normal_invoice_tab = ('by.xpath', "//ul/li[1][contains(text(),'普通发票')]")

    # 增值税发票
    vat_invoice_tab = ('by.xpath', "//ul/li[2][contains(text(),'增值税发票')]")
    bill_add = ('by.xpath', '//div/div[2]/div[4]/div[1]/a')
    bill_title = ('by.name', 'bill_title')
    bill_tax_no = ('by.name', 'bill_tax_no')
    bill_address = ('by.name', 'bill_com_addr')
    bill_phone = ('by.name', 'bill_tel_1')
    bill_bank = ('by.xpath', '//form/table/tbody/tr[5]/td[2]/input')
    bill_bank_account = ('by.xpath', '//tbody/tr[6]/td[2]/input')
    bill_set_default = ('by.xpath', '//form/p/label/i')
    bill_save = ('by.xpath', '//div[4]/div[3]/button[2]')
    first_bill = ('by.xpath', '//li[1]/table/tbody/tr[4]/td[2]')
    bill_confirm = ('by.xpath', '//div[4]/div[3]/button[1]')
    bill_del = ('by.xpath', '//div[4]/div[1]/ul/li[1]/div/a[2]/i')
    bill_del_confirm = ('by.xpath', 'html/body/div[5]/div[3]/a[1]')
    vat_invoice_cancel = ('by.xpath', '//div[4]/div[3]/button[3]')

    # 不开发票
    none_invoice_tab = ('by.xpath', "//ul/li[3][contains(text(),'不开发票')]")
    none_invoice_confirm = ('by.xpath', '//div/div/div[2]/div[2]/div/button[1]')

    # 提交订单
    submit_order_button = ('by.class_name', 'btn-order-submit')
    account_layer = ('by.class_name', 'layui-layer-btn0')
    none_invoice_layer = ('by.class_name', 'layui-layer-btn0')
    choose_approve_flow = ('by.name', 'approveFlowItem')
    submit_approve_flow = ('by.class_name', 'eps-submit-btn')

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
        time.sleep(0.5)
        message = self.element_find(self.receiving_address_layer).text
        assert message == '收货地址已添加'
        print('收货地址添加成功')
        time.sleep(4)

    def receiving_address_edit(self):
        element = self.element_find(self.address_edit)
        ActionChains(self.driver).move_to_element(element).perform()     # 鼠标悬停展现不可见的编辑按钮
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
        time.sleep(0.5)
        message = self.element_find(self.receiving_address_layer).text
        assert message == '收货地址已修改'
        print('收货地址修改成功')
        time.sleep(4)

    def receiving_address_delete(self):
        element = self.element_find(self.address_del)
        ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        self.element_find(self.del_confirm).click()
        time.sleep(0.5)
        message = self.element_find(self.receiving_address_layer).text
        assert message == '收货地址已删除'
        print('收货地址删除成功')
        time.sleep(4)

    def invoice_normal_company_add(self):
        """新增公司抬头的普票"""
        self.element_find(self.choose).click()  # 请选择按钮
        time.sleep(1)
        self.element_find(self.normal_invoice_add).click()
        self.element_find(self.company_title).send_keys('公司抬头普票')
        self.element_find(self.tax_no).send_keys('1234567890qwert')
        self.element_find(self.normal_invoice_save).click()
        time.sleep(0.5)
        message = self.element_find(self.invoice_layer).text
        assert message == '普通发票已添加'
        print('普通发票添加成功')
        time.sleep(4)
        self.element_find(self.first_normal_invoice).click()
        self.element_find(self.normal_invoice_confirm).click()
        time.sleep(0.5)

    def invoice_normal_personal_add(self):
        """新增个人抬头的普票"""
        self.element_find(self.choose).click()  # 请选择按钮
        time.sleep(0.5)
        self.element_find(self.normal_invoice_add).click()
        self.element_find(self.choose_invoice_title).send_keys('个人抬头')
        self.element_find(self.personal_title).send_keys('个人抬头普票')
        self.element_find(self.normal_invoice_save).click()
        time.sleep(0.5)
        message = self.element_find(self.invoice_layer).text
        assert message == '普通发票已添加'
        print('普通发票添加成功')
        time.sleep(4)
        self.element_find(self.first_normal_invoice).click()
        self.element_find(self.normal_invoice_confirm).click()
        time.sleep(0.5)

    def invoice_normal_delete(self):
        """删除普通发票"""
        self.element_find(self.choose).click()  # 请选择按钮
        time.sleep(0.5)
        self.element_find(self.normal_invoice_tab).click()
        try:
            """如果没有普票则不删除原发票"""
            element = self.element_find(self.first_normal_invoice)
            ActionChains(self.driver).move_to_element(element).perform()
            self.element_find(self.normal_invoice_del).click()
            self.element_find(self.normal_invoice_del_confirm).click()
            time.sleep(0.5)
            message = self.element_find(self.invoice_layer).text
            assert message == '普通发票已删除'
            print('普通发票删除成功')
            time.sleep(4)
        except NoSuchElementException:
            print('没有可以删除的普通发票')
        self.element_find(self.normal_invoice_cancel).click()
        time.sleep(0.5)

    def invoice_vat_delete(self):
        """删除增值税发票"""
        self.element_find(self.choose).click()  # 请选择按钮
        time.sleep(0.5)
        self.element_find(self.vat_invoice_tab).click()
        try:
            element = self.element_find(self.first_bill)
            ActionChains(self.driver).move_to_element(element).perform()
            self.element_find(self.bill_del).click()
            self.element_find(self.bill_del_confirm).click()
            time.sleep(0.5)
            message = self.element_find(self.invoice_layer).text
            assert message == '增值税发票已删除'
            print('增值税发票删除成功')
            time.sleep(4)
        except NoSuchElementException:
            print('没有可以删除的增值税发票')
        self.element_find(self.vat_invoice_cancel).click()
        time.sleep(0.5)

    def invoice_vat_add(self):
        self.element_find(self.choose).click()  # 请选择按钮
        time.sleep(0.5)
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
        time.sleep(1)
        self.element_find(self.first_bill).click()   # 选中第一张增票
        self.element_find(self.bill_confirm).click()
        print('增值税发票添加成功')
        time.sleep(0.5)

    def choose_normal_invoice(self):
        """选择普票"""
        while True:
            try:
                self.element_find(self.choose).click()
                break
            except ElementNotVisibleException:
                continue
            except WebDriverException:
                continue
        for i in range(30):
            try:
                self.element_find(self.normal_invoice_tab).click()
                self.element_find(self.first_normal_invoice).click()
                self.element_find(self.normal_invoice_confirm).click()
                break
            except ElementNotVisibleException:
                continue
            except WebDriverException:
                continue

    def choose_vat_invoice(self):
        """选择增票"""
        while True:
            try:
                element = self.element_find(self.choose)
                element.click()
                break
            except ElementNotVisibleException:
                continue
            except WebDriverException:
                continue
        for i in range(30):
            try:
                self.element_find(self.vat_invoice_tab).click()
                self.element_find(self.first_bill).click()
                self.element_find(self.bill_confirm).click()
                break
            except ElementNotVisibleException:
                continue
            except WebDriverException:
                continue

    def choose_none_invoice(self):
        """选择不开票"""
        while True:
            try:
                self.element_find(self.choose).click()
                break
            except ElementNotVisibleException:
                continue
            except WebDriverException:
                continue
        for i in range(30):
            try:
                self.element_find(self.none_invoice_tab).click()
                self.element_find(self.none_invoice_confirm).click()
                break
            except ElementNotVisibleException:
                continue
            except WebDriverException:
                continue

    def submit_order(self, none_invoice=False, account_period=False):
        element = self.element_find(self.submit_order_button)
        self.wait_visible_and_click(element)
        if none_invoice:
            self.element_find(self.none_invoice_layer).click()
        if account_period:
            self.element_find(self.account_layer).click()

    def submit_order_eas(self, none_invoice=False, account_period=False):
        element = self.element_find(self.submit_order_button)
        self.wait_visible_and_click(element)
        if none_invoice:
            self.element_find(self.none_invoice_layer).click()
        if account_period:
            self.element_find(self.account_layer).click()
        element = self.element_find(self.choose_approve_flow)
        self.wait_dom(element)
        element.click()
        self.element_find(self.submit_approve_flow).click()

