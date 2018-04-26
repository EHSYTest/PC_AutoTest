from Page_Base import Page
from selenium.webdriver.common.by import By
import allure, time


class OrderResult(Page):
    """订单提交成功页"""
    order_id = (By.XPATH, "//span[@ng-bind='orderId']")

    # 您提交的请购单已审批通过，请做好收货准备！
    eas_message = (By.XPATH, '//div[1]/strong')

    eis_message = (By.XPATH, '//h2/span')

    def get_so_by_url(self):
        order_id = ''
        for i in range(20):
            if not order_id.startswith('SO'):
                url = self.driver.current_url
                order_id = url[-20:]
                time.sleep(1)
                continue
            else:
                break
        allure.attach('SO单号', order_id)
        return order_id

    def get_pr_by_url(self):
        pr_number = ''
        for i in range(20):
            if not pr_number.startswith('PR'):
                url = self.driver.current_url
                pr_number = url[-21:]
                time.sleep(1)
                continue
            else:
                break
        allure.attach('PR单号', pr_number)
        return pr_number

    def get_order_id(self):
        orderId = self.element_find(self.order_id).text
        allure.attach('SO单号', orderId)
        return orderId