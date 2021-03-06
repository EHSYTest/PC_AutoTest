from Page_Base import Page
import allure, pytest


class OrderResult(Page):
    """订单提交成功页"""
    order_id = ('by.xpath', "//span[@ng-bind='orderId']")

    # 您已成功提交请购单，等待审批结果！
    eas_message = ('by.xpath', 'html/body/div[1]/div[2]/div[2]/div[1]/div[1]/p[1]/strong')

    eis_staging_url = 'http://www-staging.ehsy.com/utils/punchout-request'
    eis_production_url = 'http://www.ehsy.com/utils/punchout-request'

    def get_so_by_url(self):
        with allure.step('通过URL获取SO单号'):
            order_id = ''
            while not order_id.startswith('SO'):
                url = self.driver.current_url
                order_id = url[-20:]
            print(order_id)
            return order_id

    def get_order_id(self):
        with allure.step('通过文本获取SO单号'):
            orderId = self.element_find(self.order_id).text
            print(orderId)
            return orderId