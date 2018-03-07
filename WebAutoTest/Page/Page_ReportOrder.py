from Page_Base import Page
from selenium.common.exceptions import StaleElementReferenceException
import time, allure
from selenium.webdriver.common.by import By


class ReportOrder(Page):
    """报价单页面"""
    report_order_title = (By.NAME, 'quotation_name')
    report_order_province = (By.NAME, 'province_id')
    report_order_city = (By.NAME, 'city_id')
    report_order_invoice = (By.NAME, 'receipt_type')
    report_order_price = (By.NAME, 'price_config')
    create_report_order = (By.CLASS_NAME, 'sub_cart_form')
    report_order_change_to_order = (By.CLASS_NAME, 'btn-change-order')

    layer = (By.ID, 'ajax-layer-loading')

    def create_order_by_report_order(self, province, city):
        with allure.step('创建报价单'):
            self.element_find(self.report_order_title).send_keys('测试报价单')
            self.element_find(self.report_order_province).send_keys(province)
            self.element_find(self.report_order_city).send_keys(city)
            self.wait_click(self.report_order_invoice)
            self.wait_click(self.report_order_price)
            self.wait_click(self.create_report_order)
        with allure.step('报价单转订单'):
            self.wait_click(self.report_order_change_to_order)

