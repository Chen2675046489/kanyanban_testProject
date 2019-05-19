import unittest
import logging
from common.StartEnd import StartEnd
from selenium.webdriver.common.by import By
from businessView.loginView import loginView
from selenium.webdriver.support.expected_conditions import NoSuchElementException


class TestRunwu(StartEnd):
    mainactivity_button = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_calendar')
    task_no_task = (By.ID, 'com.tal.kaoyan:id/task_no_task')

    def test_runwe(self):
        logging.info('------进行任务选择-------')
        l = loginView(self.driver)
        l.login_action('Chen2675046489', 'Chen123456')
        status = l.check_loginStatus()
        self.driver.find_element(*self.mainactivity_button).click()
        try:
            task = self.driver.find_element(*self.task_no_task)
        except NoSuchElementException:
            logging.info('------没有指导页面------')
            pass
        else:
            logging.info('-----close_task------')
            task.click()
        l.check_account_alert()






