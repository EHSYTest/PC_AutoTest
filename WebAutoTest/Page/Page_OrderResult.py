from Page_Base import Page


class OrderResult(Page):
    """订单提交成功页"""
    order_id = ('by.xpath', "//span[@ng-bind='orderId']")

    # 您已成功提交请购单，等待审批结果！
    eas_message = ('by.xpath', 'html/body/div[1]/div[2]/div[2]/div[1]/div[1]/p[1]/strong')

    eis_message = ('by.xpath', '//h2/span')

    def get_so_by_url(self):
        order_id = ''
        while not order_id.startswith('SO'):
            url = self.driver.current_url
            order_id = url[-20:]
        print(order_id)
        return order_id

    def get_order_id(self):
        orderId = self.element_find(self.order_id).text
        print(orderId)
        return orderId