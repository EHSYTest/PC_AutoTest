from Page_Base import Page
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
import allure
from selenium.common.exceptions import NoSuchElementException

class UserAddress(Page):
    my_address = (By.LINK_TEXT, '我的地址') #进入我的（通用）地址标签页
    receive_address = (By.XPATH, '//div/div[1]/div[2]/a') #进入收货地址标签页
    invoice_address = (By.XPATH, '//div/div/div/div[1]/div[3]/a') #进入发票地址标签页
    add_address_btn = (By.CLASS_NAME, 'mod-ra-add-btn') #添加新地址按钮
    address_num = (By.XPATH, '//div/div/div/div[2]/div/div/span') #地址数量
    # 添加地址弹窗
    receiver_name = (By.NAME, 'receiver_name')
    company_name = (By.NAME, 'company_name')
    province = (By.NAME, 'province_id')
    city = (By.NAME, 'city_id')
    area = (By.NAME, 'area_id')
    detail_address = (By.NAME, 'detail_address')
    phone = (By.NAME, 'cell_phone')
    telephone = (By.NAME, 'telephone')
    checkbox_defaultAddress = (By.NAME, 'is_default')
    confirm_button = (By.CLASS_NAME, 'confirm')
    cancel_button = (By.CLASS_NAME, 'cancel')

    # 修改地址
    edit_address_btn = (By.XPATH, '//div/ul/li[2]/div[4]/a[1]')
    receiver = (By.XPATH, '//div/div/div[2]/div/div/ul/li[2]/div[1]')

    # 设置默认地址
    default_address_button = (By.CLASS_NAME, 'default-btn')
    default_address_lable = (By.XPATH, '//ul/li[2]/div[4]/span')

    # 删除地址
    delete_address_btn = (By.PARTIAL_LINK_TEXT, '删除')
    confirm = (By.XPATH, '//button[2]')

    # 地址条目
    address_count = (By.CLASS_NAME, 'ra-list-li-content')

    # loading
    layer = (By.ID, 'ajax-layer-loading')

    def add_address(self):
        '''添加地址'''
        with allure.step('添加地址'):
            address_num = self.element_find(self.address_num).text
            add_front_num = address_num[4:5]
            print(add_front_num)
            self.wait_click(self.add_address_btn)
            self.element_find(self.receiver_name).send_keys("测试")
            self.element_find(self.company_name).send_keys('测试公司')
            self.element_find(self.province).send_keys('安徽省')
            self.element_find(self.city).send_keys('安庆市')
            self.element_find(self.area).send_keys('迎江市')
            self.element_find(self.detail_address).send_keys('测试地址')
            self.element_find(self.phone).send_keys('13111111111')
            self.element_find(self.telephone).send_keys('020-88888888-8888')
            self.wait_click(self.checkbox_defaultAddress)
            self.wait_click(self.confirm_button)
            time.sleep(2)
            address_num = self.element_find(self.address_num).text
            add_after_num = address_num[4:5]
            assert int(add_after_num) == int(add_front_num) + 1
            print("地址添加成功！")

    def edit_address(self):
        '''编辑地址'''
        with allure.step('编辑地址'):
            self.wait_click(self.edit_address_btn)
            self.element_find(self.receiver_name).send_keys('-修改')
            self.element_find(self.company_name).send_keys('-修改')
            self.element_find(self.province).send_keys('江苏省')
            self.element_find(self.city).send_keys('宿迁市')
            self.element_find(self.area).send_keys('宿城区')
            self.element_find(self.detail_address).send_keys('-修改')
            self.element_find(self.phone).clear()
            self.element_find(self.phone).send_keys('14222222222')
            self.element_find(self.telephone).clear()
            self.element_find(self.telephone).send_keys('020-00000000-0000')
            self.wait_click(self.checkbox_defaultAddress)
            self.wait_click(self.confirm_button)
            time.sleep(2)
            receiver_name = self.element_find(self.receiver).text
            assert receiver_name == '测试-修改'
            print('地址修改成功！')

    def set_default_currency_address(self):
        '''设置默认通用地址'''
        with allure.step('设置默认通用地址'):
            receiver = self.element_find(self.receiver)
            ActionChains(self.driver).move_to_element(receiver).perform()
            self.wait_click(self.default_address_button)
            default_address_lable = self.element_find(self.default_address_lable).text
            assert default_address_lable == '默认通用地址'
            print('默认通用地址设置成功！')

    def delete_address(self):
        '''删除地址'''
        with allure.step('删除地址'):
            address_num = self.element_find(self.address_num).text
            del_front_num = address_num[4:5]
            self.wait_click(self.delete_address_btn)
            self.wait_click(self.confirm)
            time.sleep(2)
            address_num = self.element_find(self.address_num).text
            del_after_num = address_num[4:5]
            assert int(del_front_num) == int(del_after_num) + 1
            print('地址删除成功！')

    def set_default_receive_address(self):
        '''设置默认收货地址'''
        with allure.step('设置默认收货地址'):
            receiver = self.element_find(self.receiver)
            ActionChains(self.driver).move_to_element(receiver).perform()
            self.wait_click(self.default_address_button)
            default_address_lable = self.element_find(self.default_address_lable).text
            assert default_address_lable == '默认收货地址'
            print('默认收货地址设置成功！')

    def set_default_invoice_address(self):
        '''设置默认发票地址'''
        with allure.step('设置默认发票地址'):
            receiver = self.element_find(self.receiver)
            ActionChains(self.driver).move_to_element(receiver).perform()
            self.wait_click(self.default_address_button)
            default_address_lable = self.element_find(self.default_address_lable).text
            assert default_address_lable == '默认发票地址'
            print('默认发票地址设置成功！')

    def check_no_address(self):
        with allure.step('check_no_address'):
            time.sleep(3)
            try:
                self.element_find(self.address_count)
            except NoSuchElementException:
                return True
            else:
                count = len(self.elements_find(self.address_count))
                print('count: %s' % count)
                for i in range(count):
                    print('i: %s' % i)
                    self.wait_click(self.delete_address_btn)
                    self.wait_click(self.confirm)

