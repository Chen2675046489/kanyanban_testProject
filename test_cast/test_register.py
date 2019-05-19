from common.StartEnd import StartEnd
from businessView.registerView import RegisterView
import logging
import random
import unittest


class RegisterTest(StartEnd):
    def test_user_register(self):
        logging.info('------test_user_register-------')
        r = RegisterView(self.driver)
        username = 'Chen' + 'fly' + str(random.randint(20001, 90001))
        password = 'Chen123456'
        email = str(random.randint(111111111, 888888888))+'@qq.com'
        self.assertTrue(r.register_action(username, password, email))


if __name__ == '__main__':
    unittest.main()
