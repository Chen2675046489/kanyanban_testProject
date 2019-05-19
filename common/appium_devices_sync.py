from common.multi_desired import app_desired
from common.multi_appium import appium_start
from common.check_port import check_port
from common.check_port import release_port
import multiprocessing
from time import sleep

devices_list = ['emulator-5554', '127.0.0.1:21503']# 连接IP地址


def start_appium_action(host, port):
    if check_port(host, port):
        appium_start(host, port)
        return True
    else:
        print('appium %s start fail' % port)
        return False


def start_devices_action(udid, port):
    host = '127.0.0.1'
    startc = start_appium_action(host, port)
    print(startc)
    if start_appium_action(host, port):# 判断appium是否启动成功【成功：True，失败：False】
        app_desired(udid, port)# 启动app
    else:
        release_port(port)# 释放端口


def appium_start_sync():
    print('------appium start sync------')
    # 构建appium进程
    # 构建appium进程
    appium_process = []
    # 加载appium进程
    for i in range(2):
        host = '127.0.0.1'
        port = 4723 + (2 * i)
        appium = multiprocessing.Process(target=start_appium_action, args=(host, port))
        appium_process.append(appium)

    for appium in appium_process:
        appium.start()
    for appium in appium_process:
        appium.join()


def devices_start_sync():
    # 构造desired进程组
    desired_process = []
    # 加载desired进程
    for i in range(len(devices_list)):
        port = 4723 + 2 * i
        desired = multiprocessing.Process(target=start_devices_action, args=(devices_list[i], port))
        desired_process.append(desired)

    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()


if __name__ == '__main__':
    appium_start_sync()
    devices_start_sync()
