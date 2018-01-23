from Page_Base import Page
from selenium.webdriver.common.action_chains import ActionChains
import time


class UserInvoice(Page):
    my_invoice = ('by.link_text', '我的发票')
    invoice_num = ('by.class_name', 'ii-list-title')
    receipt_invoice = ('by.link_text', '增值税发票')

    #添加普通发票
    add_invoice = ('by.class_name', 'mod-ra-add-btn')
    invoice_type = ('by.name', 'sub_type')
    invoice_title = ('by.xpath', '//p[2]/span[2]/input')
    tax_no = ('by.name', 'tax_no')
    default_invoice = ('by.name', 'is_default_invoice')
    confirm_button = ('by.xpath', '//button[2]')
    serial_number = ('by.xpath', '//div[2]/ul/li[2]/div[1]')

    # 普票修改
    edit_invoice_btn = ('by.link_text', '修改')
    invoice_title_name = ('by.xpath', '//ul/li[2]/div[3]')
    invoice_type_name = ('by.xpath', '//ul/li[2]/div[2]')
    invoice_tax_no = ('by.xpath', '//div/div[2]/ul/li[2]/div[4]')

    # 添加增值税发票
    add_receipt_invoice_btn = ('by.class_name', 'mod-ra-add-btn')
    company_name = ('by.xpath', '//p[1]/span[2]/input')
    receipt_tax_no = ('by.name', 'tax_no')
    company_address = ('by.name', 'company_address')
    contact_number = ('by.xpath', '//p[4]/span[2]/input')
    bank_name = ('by.name', 'bank_name')
    bank_account = ('by.name', 'bank_account')
    default_receipt_invoice = ('by.name', 'is_default_invoice')

    #增票修改
    edit_receipt_invoice_btn = ('by.link_text', '修改')
    invoice_company_name = ('by.xpath', '//ul/li[2]/div[1]/p[1]')

    # 设置默认发票
    set_default_invoice_btn = ('by.class_name', 'default-btn')
    default_invoice_lable = ('by.xpath', '//ul/li[2]/div[5]/span')

    # 删除发票
    del_invoice_btn = ('by.link_text', '删除')

    def add_company_invoice(self):
        """新增公司类型发票"""
        invoice_num = self.element_find(self.invoice_num).text
        add_front_num = invoice_num[2:3]
        self.wait_click(self.add_invoice)
        self.element_find(self.invoice_type).send_keys('公司抬头')
        self.element_find(self.invoice_title).send_keys('测试公司发票')
        self.element_find(self.tax_no).send_keys('123456789123456789')
        self.wait_click(self.default_invoice)
        self.wait_click(self.confirm_button)
        time.sleep(2)
        invoice_num = self.element_find(self.invoice_num).text
        add_after_num = invoice_num[2:3]
        assert int(add_after_num) == int(add_front_num) + 1
        print('公司类型发票添加成功！')

    def edit_company_invoice(self):
        """编辑公司类型发票"""
        self.wait_click(self.edit_invoice_btn)
        self.element_find(self.invoice_title).send_keys('-修改')
        self.element_find(self.tax_no).clear()
        self.element_find(self.tax_no).send_keys('qqqqqqqqqwwwwwwwww')
        self.wait_click(self.default_invoice)
        self.wait_click(self.confirm_button)
        invoice_title_name = self.element_find(self.invoice_title_name).text
        assert invoice_title_name == '测试公司发票-修改'
        print('公司类型发票修改成功！')

    def company_change_personal(self):
        ###公司类型发票转换成个人类型###
        self.wait_click(self.edit_invoice_btn)
        self.element_find(self.invoice_type).send_keys('个人抬头')
        self.wait_click(self.confirm_button)
        invoice_type_name = self.element_find(self.invoice_type_name).text
        # invoice_tax_no = self.element_find(self.invoice_tax_no).text
        assert invoice_type_name == '个人'
        # assert invoice_tax_no == '无'
        print('公司类型发票转换成个人类型发票成功！')

    def set_default_invoice(self):
        ###设置默认发票（公司/个人）###
        invoice_type_name = self.element_find(self.invoice_type_name)
        ActionChains(self.driver).move_to_element(invoice_type_name).perform()
        self.wait_click(self.set_default_invoice_btn)
        default_invoice_lable = self.element_find(self.default_invoice_lable).text
        assert default_invoice_lable == '默认发票'
        print('默认发票设置成功！')

    def delete_normal_invoice(self):
        ###删除发票（公司/个人）###
        invoice_num = self.element_find(self.invoice_num).text
        del_front_num = invoice_num[2:3]
        self.wait_click(self.del_invoice_btn)
        self.wait_click(self.confirm_button)
        time.sleep(2)
        invoice_num = self.element_find(self.invoice_num).text
        del_after_num = invoice_num[2:3]
        print(del_after_num, del_front_num)
        assert int(del_front_num) == int(del_after_num) + 1
        print('发票删除成功！')

    def add_personal_invoice(self):
        ###新增个人类型发票###
        invoice_num = self.element_find(self.invoice_num).text
        add_front_num = invoice_num[2:3]
        self.wait_click(self.add_invoice)
        self.element_find(self.invoice_type).send_keys('个人抬头')
        self.element_find(self.invoice_title).send_keys('测试个人发票')
        self.wait_click(self.default_invoice)
        self.wait_click(self.confirm_button)
        time.sleep(2)
        invoice_num = self.element_find(self.invoice_num).text
        add_after_num = invoice_num[2:3]
        assert int(add_after_num) == int(add_front_num) + 1
        print('个人类型发票添加成功！')

    def edit_personal_invoice(self):
        ###编辑个人类型发票###
        self.wait_click(self.edit_invoice_btn)
        self.element_find(self.invoice_title).send_keys('-修改')
        self.wait_click(self.default_invoice)
        self.wait_click(self.confirm_button)
        invoice_title_name = self.element_find(self.invoice_title_name).text
        assert invoice_title_name == '测试个人发票-修改'
        print('个人类型发票修改成功！')

    def personal_change_company(self):
        ###个人类型发票转换成公司类型###
        self.wait_click(self.edit_invoice_btn)
        self.element_find(self.invoice_type).send_keys('公司抬头')
        self.element_find(self.tax_no).send_keys('123456789123456789')
        self.wait_click(self.confirm_button)
        invoice_type_name = self.element_find(self.invoice_type_name).text
        invoice_tax_no = self.element_find(self.invoice_tax_no).text
        assert invoice_type_name == '公司'
        assert invoice_tax_no == '123456789123456789'
        print('个人类型发票转换成公司类型发票成功！')

    def add_receipt_invoice(self):
        ###新增增值税发票###
        self.wait_click(self.receipt_invoice)
        invoice_num = self.element_find(self.invoice_num).text
        add_front_num = invoice_num[2:3]
        self.wait_click(self.add_receipt_invoice_btn)
        self.element_find(self.company_name).send_keys('测试公司')
        self.element_find(self.receipt_tax_no).send_keys('123456789123456789')
        self.element_find(self.company_address).send_keys('测试地址')
        self.element_find(self.contact_number).send_keys('13111111111')
        self.element_find(self.bank_name).send_keys('招商银行')
        self.element_find(self.bank_account).send_keys('1234123412341234')
        self.wait_click(self.default_receipt_invoice)
        self.wait_click(self.confirm_button)
        time.sleep(2)
        invoice_num = self.element_find(self.invoice_num).text
        add_after_num = invoice_num[2:3]
        assert int(add_after_num) == int(add_front_num) + 1
        print('增值税发票添加成功！')

    def edit_receipt_invoice(self):
        ###编辑增值税发票###
        self.wait_click(self.edit_receipt_invoice_btn)
        self.element_find(self.company_name).send_keys('-修改')
        self.element_find(self.receipt_tax_no).clear()
        self.element_find(self.receipt_tax_no).send_keys('987654321987654321')
        self.element_find(self.company_address).send_keys('-修改')
        self.element_find(self.contact_number).clear()
        self.element_find(self.contact_number).send_keys('13000000000')
        self.element_find(self.bank_name).clear()
        self.element_find(self.bank_name).send_keys('江苏银行')
        self.element_find(self.bank_account).clear()
        self.element_find(self.bank_account).send_keys('4321432143214321')
        self.wait_click(self.default_receipt_invoice)
        self.wait_click(self.confirm_button)
        time.sleep(2)
        invoice_company_name = self.element_find(self.invoice_company_name).text
        assert invoice_company_name == '测试公司-修改'
        print('增值税发票修改成功！')

    def set_default_receipt_invoice(self):
        ###设置默认增票###
        invoice_company_name = self.element_find(self.invoice_company_name)
        ActionChains(self.driver).move_to_element(invoice_company_name).perform()
        self.wait_click(self.set_default_invoice_btn)
        default_invoice_lable = self.element_find(self.default_invoice_lable).text
        assert default_invoice_lable == '默认发票'
        print('设置默认增票成功！')

    def del_receipt_invoice(self):
        ###删除增票###
        invoice_num = self.element_find(self.invoice_num).text
        del_front_num = invoice_num[2:3]
        self.wait_click(self.del_invoice_btn)
        self.wait_click(self.confirm_button)
        time.sleep(2)
        invoice_num = self.element_find(self.invoice_num).text
        del_after_num = invoice_num[2:3]
        assert int(del_front_num) == int(del_after_num) + 1
        print('增值税发票删除成功！')



