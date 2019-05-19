"""公共类：进行app启动操作和日志输出"""
import os
import yaml
import logging
import logging.config
from appium import webdriver


CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging.getLogger()


def app_desired():
    with open('../config/kyb_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appName'])

    desired_caps = {
            # 设备的信息
            'platformName': data['platformName'],
            'deviceName': data['deviceName'],
            'platformVersion': data['platformVersion'],
            # App软件的信息

            'app': app_path,
            'appPackage': data['appPackage'],
            'appActivity': data['appActivity'],
            # 设备的设置
            'noReset': data['noReset'],
            'unicodeKeyboard': data['unicodeKeyboard'],
            'resetKeyboard': data['resetKeyboard'],
            # 进行automationName的切换
            'automationName': data['automationName']
        }

    logging.info('star app……')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    return driver


if __name__ == '__main__':
    app_desired()
