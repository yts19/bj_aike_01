import os
import sys

from get_driver import Driver
from tool.data_get import yaml_load

sys.path.append(os.getcwd())

import pytest


from page.page_login import PageLogin
def data():

    mylist = []
    for i in yaml_load().values():
        mylist.append(tuple(i.values()))
    return mylist


class TestLogin(object):
    # 初始化
    def setup_class(self):
        self.driver=Driver.get_driver()
        self.pagelogin=PageLogin()


    # 结束
    def teardown_class(self):
        Driver.quit_driver()

    # 测试方法
    @pytest.mark.parametrize('username,pwd',data())
    def test_login(self,username,pwd):
        self.pagelogin.page_login_proxy(username,pwd)

if __name__ == '__main__':
    pytest.main('test_login.py')