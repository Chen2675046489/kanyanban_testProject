from common.StartEnd import StartEnd
from businessView.loginView import loginView
import unittest
import logging


class TestLogin(StartEnd):
    csv_file = '../data/account.csv'

    def test_login1(self):
        logging.info('------test login1-----')
        l = loginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus())

    @unittest.skip('skip test_login2')
    def test_login2(self):
        logging.info('------test login2-----')
        l = loginView(self.driver)
        data = l.get_csv_data(self.csv_file, 2)
        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus())

    @unittest.skip('skip test_login3')
    def test_login3(self):
        logging.info('------test login2-----')
        l = loginView(self.driver)
        data = l.get_csv_data(self.csv_file, 3)
        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus(), msg='login fail')


if __name__ == '__main__':
    unittest.main()
