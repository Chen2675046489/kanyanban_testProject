"""公共类：更新跳过和启动页跳过"""
import logging
import csv
import time
import os
from baseView.baseView import BaseView
from common.desired_caps import app_desired
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class Common(BaseView):
    cancelBtn = (By.ID, 'android:id/button2')
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')
    wemedia_cacel = (By.ID, 'com.tal.kaoyan:id/view_wemedia_cacel')

    def check_cancelBtn(self):
        """检查是否有更新提示"""
        logging.info('--------check cancelBtn--------')
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('no cancelBtn')
        else:
            cancelBtn.click()

    def check_skipBtn(self):
        """跳过广告"""
        logging.info('--------check skipBtn--------')
        try:
            skipBtn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('no skipBtn')
        else:
            skipBtn.click()

    def get_size(self):
        """获取当前手机size"""
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        """向左滑动"""
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 1000)

    def swipeRight(self):
        """向右滑动"""
        logging.info('swipeRight')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x2, y1, x1, y1, 1000)

    def swipeUp(self):
        """向上滑动"""
        logging.info('swipeUp')
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.8)
        y2 = int(l[1] * 0.2)
        self.swipe(x1, y1, x1, y2, 1000)

    def swipeDown(self):
        """向下滑动"""
        logging.info('swipeUp')
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.8)
        y2 = int(l[1] * 0.2)
        self.swipe(x1, y2, x1, y1, 1000)

    def getTime(self):
        """获取当前系统时间并以%Y-%m-%d_%H_%M_%S格式返回"""
        self.now = time.strftime("%Y-%m-%d_%H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        """进行当前位置截图"""
        current_time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' % (module, current_time)
        logging.info('获取 %s 成功' % module)
        self.driver.get_screenshot_as_file(image_file)

    def check_mmarket_ad(self):
        """检查是否有推送消息"""
        logging.info('------check_market_ad------')
        try:
            element = self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info('------close market_ad------')
            element.click()

    def get_csv_data(self, csv_file, line):
        """进行cvs数据的读取"""
        logging.info('------get _csv_data------')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    def get_toast_text(self, text,  timeout=10, poll_frequency=0.5):
        """获取Toast弹窗文字"""
        try:
            toast_element = (By.XPATH, "//*[contains(@text, " + "'" + text + "'" + ")]")
            toast = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_element))
            self.getScreenShot(text)
            return True
        except:
            return False


if __name__ == '__main__':
    driver = app_desired()
    com = Common(driver)
    com.check_cancelBtn()
    # com.check_skipBtn()
    com.swipeLeft()
    com.getScreenShot('startApp')







