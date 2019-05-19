import unittest
from common.desired_caps import app_desired
from time import sleep
import logging


class StartEnd(unittest.TestCase):

    def setUp(self):
        logging.info('-------setUp-------')
        self.driver = app_desired()

    def tearDown(self):
        logging.info('-------tearDown-------')
        sleep(5)
        self.driver.close_app()


