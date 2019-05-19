import yaml
import os
from appium import webdriver
from time import ctime
import multiprocessing# 多线程的模块

with open('../config/kyb_caps.yaml', 'r', encoding='utf-8') as file:
    data = yaml.load(file)

devices_list = ['emulator-5554', '127.0.0.1:21503']# 连接IP地址


def app_desired(udid, port):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appName'])

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['udid'] = udid
    # App软件的信息
    desired_caps['app'] = app_path
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    # 设备的设置
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    # 进行automationName的切换
    desired_caps['automationName'] = data['automationName']
    print('appium port:%s start run %s at %s' %(port, udid, ctime()))
    # logging.info('star app……')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(port)+'/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    return driver


# 构造desired进程组
desired_process = []
# 加载desired进程
for i in range(len(devices_list)):
    port = 4723+2*i
    desired = multiprocessing.Process(target=app_desired, args=(devices_list[i], port))
    desired_process.append(desired)


if __name__ == '__main__':
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()
