
from selenium.webdriver.support.wait import WebDriverWait

from get_driver import Driver


class BaseLogin(object):
    """公共方法"""

    # driver 对象
    def __init__(self):
        self.driver=Driver.get_driver()

    # 元素定位
    def base_find_element(self, loc, time=20, poll=0.5):
        return WebDriverWait(self.driver, timeout=time, poll_frequency=poll).until(lambda x: x.find_element(loc[0],loc[1]))

    # 输入方法
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()
