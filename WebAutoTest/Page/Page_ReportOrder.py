from Page_Base import Page
from selenium.common.exceptions import StaleElementReferenceException
import time


class ReportOrder(Page):
    """报价单页面"""
    report_order_title = ('by.name', 'quotation_name')
    report_order_province = ('by.name', 'province_id')
    report_order_city = ('by.name', 'city_id')
    report_order_invoice = ('by.name', 'receipt_type')
    report_order_price = ('by.name', 'price_config')
    create_report_order = ('by.class_name', 'sub_cart_form')
    report_order_change_to_order = ('by.class_name', 'btn-change-order')

    layer = ('by.id', 'ajax-layer-loading')

    def create_order_by_report_order(self):
        self.element_find(self.report_order_title).send_keys('测试报价单')
        self.element_find(self.report_order_province).send_keys('江苏省')
        self.element_find(self.report_order_city).send_keys('南京市')
        self.wait_click(self.report_order_invoice)
        self.wait_click(self.report_order_price)
        self.wait_click(self.create_report_order)
        self.wait_click(self.report_order_change_to_order)

