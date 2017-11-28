import requests, time
from selenium.common.exceptions import ElementNotVisibleException
from configobj import ConfigObj
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import exceptions


class Page():

    def __init__(self, driver):
        self.driver = driver

    def element_find(self, element):
        if element[0] == 'by.id':
            element_find = self.driver.find_element_by_id(element[1])
        if element[0] == 'by.xpath':
            element_find = self.driver.find_element_by_xpath(element[1])
        if element[0] == 'by.class_name':
            element_find = self.driver.find_element_by_class_name(element[1])
        if element[0] == 'by.name':
            element_find = self.driver.find_element_by_name(element[1])
        if element[0] == 'by.tag_name':
            element_find = self.driver.find_element_by_tag_name(element[1])
        if element[0] == 'by.link_text':
            element_find = self.driver.find_element_by_link_text(element[1])
        if element[0] == 'by.partial_link_text':
            element_find = self.driver.find_element_by_partial_link_text(element[1])
        return element_find

    def elements_find(self, element):
        if element[0] == 'by.id':
            elements_find = self.driver.find_elements_by_id(element[1])
        if element[0] == 'by.xpath':
            elements_find = self.driver.find_elements_by_xpath(element[1])
        if element[0] == 'by.class_name':
            elements_find = self.driver.find_elements_by_class_name(element[1])
        if element[0] == 'by.name':
            elements_find = self.driver.find_elements_by_name(element[1])
        if element[0] == 'by.tag_name':
            elements_find = self.driver.find_elements_by_tag_name(element[1])
        if element[0] == 'by.link_text':
            elements_find = self.driver.find_elements_by_link_text(element[1])
        if element[0] == 'by.partial_link_text':
            elements_find = self.driver
        return elements_find

    def switch_to_new_window(self, handle_quantity=2):
        # 切换到刚打开的新窗口
        while True:
            all_handle = self.driver.window_handles
            if len(all_handle) == handle_quantity:
                break
            else:
                pass
        self.driver.switch_to_window(all_handle[handle_quantity-1])


    @staticmethod
    def cancel_order(orderId, environment='test', userId='508107841'):
        if environment == 'staging':
            url = 'http://oc-staging.ehsy.com/orderCenter/cancel'
        elif environment == 'production':
            url = 'http://oc.ehsy.com/orderCenter/cancel'
        data = {'orderId': orderId, 'userId': userId}
        r = requests.post(url, data=data)
        result = r.json()
        print(result['message'])
        assert result['message'] == '订单取消申请提交成功'

    @staticmethod
    def config_reader(file, section, option):
        config = ConfigObj('../config/' + file)
        content = config[section][option]
        return content

    def wait_to_unvisible(self, ele):
        for i in range(30):
            if self.element_find(ele).is_displayed():
                time.sleep(0.1)
                continue
            else:
                break

    def wait_to_clickable(self, ele):
        if ele[0] == 'by.id':
            way = By.ID
        if ele[0] == 'by.class_name':
            way = By.CLASS_NAME
        if ele[0] == 'by.xpath':
            way = By.XPATH
        if ele[0] == 'by.link_text':
            way = By.LINK_TEXT
        if ele[0] == 'by.name':
            way = By.NAME
        if ele[0] == 'by.partial_link_text':
            way = By.PARTIAL_LINK_TEXT
        if ele[0] == 'by.tag_name':
            way = By.TAG_NAME
        element = WebDriverWait(self.driver, 10, 0.5).until(
            expected_conditions.element_to_be_clickable(
                (way, ele[1])
            )
        )
        return element

    def wait_to_visibility(self,ele):
        if ele[0] == 'by.id':
            way = By.ID
        if ele[0] == 'by.class_name':
            way = By.CLASS_NAME
        if ele[0] == 'by.xpath':
            way = By.XPATH
        if ele[0] == 'by.link_text':
            way = By.LINK_TEXT
        if ele[0] == 'by.name':
            way = By.NAME
        if ele[0] == 'by.partial_link_text':
            way = By.PARTIAL_LINK_TEXT
        if ele[0] == 'by.tag_name':
            way = By.TAG_NAME
        element = WebDriverWait(self.driver, 10, 0.2).until(
            expected_conditions.visibility_of_element_located(
                (way,ele[1])
            )
        )
        return element

    def wait_to_stale(self, ele):
        try:
            element = self.element_find(ele)
            WebDriverWait(self.driver, 20, 0.5).until(
                expected_conditions.staleness_of(element)
            )
        except exceptions.NoSuchElementException:
            print('wait_to_stale: exceptions.NoSuchElementException')
        except exceptions.TimeoutException:
            print('wait_to_stale: exceptions.NoSuchElementException')

    def wclick(self, element):
        for i in range(30):
            if element.is_enabled():
                element.click()
                break
            else:
                time.sleep(0.3)
                continue
