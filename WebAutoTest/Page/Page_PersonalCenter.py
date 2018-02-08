from Page_Base import Page
from selenium.webdriver.common.by import By


class PersonalCenter(Page):

    menu_approve = (By.LINK_TEXT, '采购审批')
    first_pr_number = (By.XPATH, '//div[2]/div[2]/div[1]/div/span[3]')
    first_approve_status = (By.XPATH, '//div[1]/table/tbody/tr/td[3]/div[2]')
    first_approve_menu = (By.LINK_TEXT, '审批详情')

    # 审批详情页
    approve_pass = (By.CLASS_NAME, 'pass-order')
    approve_reject = (By.CLASS_NAME, 'sprite-ico_no')
    approve_contract_no = (By.NAME, 'contract_no')
    approve_remark = (By.NAME, 'approve_remark')
    approve_commit = (By.XPATH, '//div[3]/div/div/div[1]/a')

    approve_status = (By.CLASS_NAME, 'status-text')

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
