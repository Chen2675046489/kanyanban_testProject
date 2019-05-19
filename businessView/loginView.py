import logging
from common.common_fun import Common
from common.desired_caps import app_desired
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class loginView(Common):
    username_type = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    password_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    loginBtn = (By.ID, 'com.tal.kaoyan:id/login_login_btn')

    tip_commit = (By.ID, 'com.tal.kaoyan:id/tip_commit')

    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')

    RightButton = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButtonWraper')
    logoutBtn = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')

    def login_action(self, username, password):
        """登录方法"""
        self.check_cancelBtn()
        self.check_skipBtn()
        logging.info('-------login_action-------')
        logging.info('username is:%s' % username)
        self.driver.find_element(*self.username_type).send_keys(username)
        logging.info('password is:%s' % password)
        self.driver.find_element(*self.password_type).send_keys(password)
        self.driver.find_element(*self.loginBtn).click()

    def check_account_alert(self):
        """检查是否有异常登录弹窗"""
        logging.info('------check_account_alert------')
        try:
            element = self.driver.find_element(*self.tip_commit)
        except NoSuchElementException:
            pass
        else:
            logging.info('-------close tip_commit------')
            element.click()

    def check_loginStatus(self):
        """检查是否登录成功"""
        logging.info('------check_loginStatus------')
        self.check_mmarket_ad()
        self.check_account_alert()

        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('------登录失败------')
            self.getScreenShot('login Fail')
            return False
        else:
            logging.info('------登录成功------')
            # self.logout_action()
            return True

    def logout_action(self):
        """退出登录"""
        logging.info('------logout_action------')
        self.driver.find_element(*self.RightButton).click()
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.tip_commit).click()


if __name__ == '__main__':
    driver = app_desired()
    l = loginView(driver)
    l.login_action('Chen2675046489', 'Chen123456')


