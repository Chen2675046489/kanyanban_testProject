"""进行设备的初始化和元素定位"""


class BaseView(object):
    # 进行初始化
    def __init__(self, driver):
        """进行初始化"""
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # 获取屏幕的方法封装
    def get_window_size(self):
        """获取屏幕的方法封装"""
        return self.driver.get_window_size()

    # 进行滑动方法的封装
    def swipe(self, start_x, start_y, end_x, end_y, duration):
        """进行滑动方法的封装"""
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)
