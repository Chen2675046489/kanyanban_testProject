import logging
import random
from time import sleep
from common.common_fun import Common
from common.desired_caps import app_desired
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class RegisterView(Common):
    # 登录注册按钮
    register_text = (By.ID, 'com.tal.kaoyan:id/login_register_text')

    # 头像设置相关元素
    userheader = (By.ID, 'com.tal.kaoyan:id/activity_register_userheader')
    item_image = (By.ID, 'com.tal.kaoyan:id/item_image')
    saveBtn = (By.ID, 'com.tal.kaoyan:id/save')

    # 注册个人信息元素
    register_username = (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')
    register_password = (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')
    register_email = (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')
    register_btn = (By.ID, 'com.tal.kaoyan:id/activity_register_register_btn')

    # 完善信息列表元素
    perfectinfomation_school = (By.ID, 'com.tal.kaoyan:id/perfectinfomation_edit_school_name')
    perfectinfomation_major = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_major')
    perfectinfomation_goBtn = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')

    # 院校信息元素
    forum_title = (By.ID, 'com.tal.kaoyan:id/more_forum_title')
    university = (By.ID, 'com.tal.kaoyan:id/university_search_item_name')

    # 专业列表信息
    major_subject_title = (By.ID, 'com.tal.kaoyan:id/major_subject_title')
    major_group_title = (By.ID, 'com.tal.kaoyan:id/major_group_title')
    major_search_item_name = (By.ID, 'com.tal.kaoyan:id/major_search_item_name')

    # 个人中心元素
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')

    # 个人信息进行填写和调用院校和专业选择的方法以及检查是否注册成功
    def register_action(self, re_username, re_password, re_email):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info('------开始注册账号------')
        self.driver.find_element(*self.register_text).click()

        # 头像设置
        logging.info('------设置头像中------')
        self.driver.find_element(*self.userheader).click()
        self.driver.find_elements(*self.item_image)[5].click()
        self.driver.find_element(*self.saveBtn).click()

        # 用户名和密码设置
        logging.info('------注册账号: %s' % re_username)
        self.driver.find_element(*self.register_username).send_keys(re_username)

        logging.info('------注册密码: %s' % re_password)
        self.driver.find_element(*self.register_password).send_keys(re_password)

        logging.info('------注册邮箱: %s' % re_email)
        self.driver.find_element(*self.register_email).send_keys(re_email)
        sleep(2)

        logging.info('-----click register------')
        self.driver.find_element(*self.register_btn).click()

        # 判断是否进行到院校信息里欸表，注册太频繁会报显示无法进入
        try:
            self.driver.find_element(*self.perfectinfomation_school)
        except NoSuchElementException:
            logging.error('------进行院校信息列表失败------')
            self.getScreenShot('进行院校信息列表失败')
            return False
        else:
            self.add_register()# 调用院校和专业选择的方法
        # 注册结果判断
            if self.check_register(): # 调用注册信息方法
                return True
            else:
                return False

    # 对院校和专业进行选择
    def add_register(self):
        logging.info('------进行院校和专业选择中------')

        # 进行院校选择
        logging.info('------选择院校中------')
        self.driver.find_element(*self.perfectinfomation_school).click()
        self.driver.find_elements(*self.forum_title)[1].click()
        self.driver.find_elements(*self.university)[1].click()

        # 进行专业选择
        logging.info('------选择专业中------')
        self.driver.find_element(*self.perfectinfomation_major).click()
        self.driver.find_elements(*self.major_subject_title)[1].click()
        self.driver.find_elements(*self.major_group_title)[2].click()
        self.driver.find_elements(*self.major_search_item_name)[1].click()

        self.driver.find_element(*self.perfectinfomation_goBtn).click()

    # 检查是否注册成功
    def check_register(self):
        logging.info('------检查是否注册成功------')
        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('------注册失败------')
            self.getScreenShot('注册账号失败')
            return False
        else:
            logging.info('------注册成功------')
            self.getScreenShot('注册账号成功')
            return True


if __name__ == '__main__':
    driver = app_desired()
    register = RegisterView(driver)
    username = 'Chen'+str(random.randint(100001, 100099))
    password = 'Chen'+str(random.randint(100000, 565656))
    email = str(random.randint(10000000, 999999999))+'@qq.com'
    register.register_action(username, password, email)
