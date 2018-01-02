from Page_Base import Page


class OrderResult(Page):
    """订单提交成功页"""
    order_id = ('by.xpath', "//span[@ng-bind='orderId']")

    # 您提交的请购单已审批通过，请做好收货准备！
    eas_message = ('by.xpath', '//div[1]/strong')

    eis_message = ('by.xpath', '//h2/span')

    def get_so_by_url(self):
        order_id = ''
        while not order_id.startswith('SO'):
            url = self.driver.current_url
            order_id = url[-20:]
        print(order_id)
        return order_id

    def get_pr_by_url(self):
        pr_number = ''
        while not pr_number.startswith('PR'):
            url = self.driver.current_url
            pr_number = url[-21:]
        print(pr_number)
        return pr_number

    def get_order_id(self):
        orderId = self.element_find(self.order_id).text
        print(orderId)
        return orderId