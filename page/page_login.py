import page
from base.base_login import BaseLogin


class PageLogin(BaseLogin):
    """业务操作"""
    # 输手机号
    def page_input_phone(self,value):
        self.base_input(page.login_phone,value)
    # 输入密码
    def page_input_pwd(self,pwd):
        self.base_input(page.login_pwd,pwd)

    # 点击登录
    def page_click_login(self):
        self.base_click(page.login_btn)

    # 组合业务操作
    def page_login_proxy(self,value,pwd):
        self.page_input_phone(value)
        self.page_input_pwd(pwd)
        self.page_click_login()