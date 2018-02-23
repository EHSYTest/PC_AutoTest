import requests, time
from selenium.common.exceptions import ElementNotVisibleException
from configobj import ConfigObj
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import exceptions
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import pytest, allure


class Page(object):

    def __init__(self, driver):
        self.driver = driver

    def element_find(self, element):
        element_find = self.driver.find_element(element[0], element[1])
        return element_find

    def elements_find(self, element):
        elements_find = self.driver.find_elements(element[0], element[1])
        return elements_find

    def switch_to_new_window(self, handle_quantity=2):
        # 切换到刚打开的新窗口
        while True:
            all_handle = self.driver.window_handles
            if len(all_handle) == handle_quantity:
                break
            else:
                time.sleep(1)
                pass
        self.driver.switch_to_window(all_handle[handle_quantity-1])


    @staticmethod
    def cancel_order(orderId, environment='staging', userId='508107841'):
        with allure.step('接口取消订单'):
            if environment == 'staging':
                url = 'http://oc-staging.ehsy.com/orderCenter/cancel'
            elif environment == 'production':
                url = 'http://oc.ehsy.com/orderCenter/cancel'
            data = {'orderId': orderId, 'userId': userId}
            r = requests.post(url, data=data)
            result = r.json()
            allure.attach('接口返回message', result['message'])
            with allure.step("断言result['message']==订单取消申请提交成功"):
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
        element = WebDriverWait(self.driver, 10, 0.5).until(
            expected_conditions.element_to_be_clickable(
                (ele[0], ele[1])
            )
        )
        return element

    def wait_to_visibility(self,ele):
        element = WebDriverWait(self.driver, 10, 0.2).until(
            expected_conditions.visibility_of_element_located(
                (ele[0], ele[1])
            )
        )
        return element

    def wait_to_stale(self, ele):
        try:
            WebDriverWait(self.driver, 5, 0.5).until(
                expected_conditions.staleness_of(self.element_find(ele))
            )
        except exceptions.NoSuchElementException:
            print('wait_to_stale: exceptions.NoSuchElementException')
        except exceptions.TimeoutException:
            print('wait_to_stale: exceptions.TimeoutException')

    def wait_click(self, ele):
        for i in range(50):
            if i == 40:     # 长时间点击无效，刷新页面
                self.driver.refresh()
            try:
                self.element_find(ele).click()
                break
            except exceptions.WebDriverException:
                time.sleep(1)
                continue

    def isElementExist(self, ele):
        try:
            self.element_find(ele)
            return True
        except:
            return False

    @staticmethod
    def db_con(database, sql):
        if database == 'staging':
            con = pymysql.connect(
                    host='118.178.189.137',
                    user='root',
                    password='ehsy2017',
                    port=3306,
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor   # sql查询结果转为字典类型
                )
        if database == 'production':
            con = pymysql.connect(
                host='112.124.96.28',
                user='ehsy_readonly',
                password='Ehsy2017',
                port=4040,
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor  # sql查询结果转为字典类型
            )
        cr = con.cursor()
        cr.execute(sql)
        con.commit()
        result = cr.fetchall()
        con.close()
        return result


class AssistFunction():

    @staticmethod
    def send_email(dir, flag):
        report = open(dir, 'rb')
        mail_body = report.read()
        report.close()
        msg = MIMEText(mail_body, 'html', 'utf-8')
        msg['Subject'] = Header('EHSY-自动化测试报告-' + flag, 'utf-8')
        msg['From'] = 'EHSY自动化测试'
        msg['To'] = 'it-test@ehsy.com'
        smtp = smtplib.SMTP()
        smtp.connect('smtp.exmail.qq.com')
        smtp.login('rick_zhang@ehsy.com', '690903Zr')
        smtp.sendmail('rick_zhang@ehsy.com', ['it-test@ehsy.com'], msg.as_string())
        smtp.quit()
