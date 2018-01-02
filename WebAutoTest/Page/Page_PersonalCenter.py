from Page_Base import Page


class PersonalCenter(Page):

    menu_approve = ('by.link_text', '采购审批')
    first_pr_number = ('by.xpath', '//div[2]/div[2]/div[1]/div/span[3]')
    first_approve_status = ('by.xpath', '//div[1]/table/tbody/tr/td[3]/div[2]')
    first_approve_menu = ('by.link_text', '审批详情')

    # 审批详情页
    approve_pass = ('by.class_name', 'pass-order')
    approve_reject = ('by.class_name', 'sprite-ico_no')
    approve_contract_no = ('by.name', 'contract_no')
    approve_remark = ('by.name', 'approve_remark')
    approve_commit = ('by.xpath', '//div[3]/div/div/div[1]/a')

    approve_status = ('by.class_name', 'status-text')

    def approve_pr(self, status):
        if status == 'pass':
            self.wait_click(self.approve_pass)
        elif status == 'reject':
            self.wait_click(self.approve_reject)
        elif status == 'pass&reject':
            self.wait_click(self.approve_pass)
            self.elements_find(self.approve_reject)[1].click()
        else:
            raise Exception('status must in (pass & reject)')
        self.element_find(self.approve_contract_no).send_keys('EAS审批客户订单号')
        self.element_find(self.approve_remark).send_keys('EAS审批说明')
        self.wait_click(self.approve_commit)
        assert_status = self.elements_find(self.approve_status)
        if status == 'pass':
            assert assert_status[0].text == '通过'
        elif status == 'reject':
            assert assert_status[0].text == '驳回'
        elif status == 'pass&reject':
            assert assert_status[0].text == '通过'
            assert assert_status[1].text == '驳回'
