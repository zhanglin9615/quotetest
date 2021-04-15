from quote.base.usebrowser import UseBrowser
from quote.base.weboperation import WebOperation
from quote.util.exloperation import ExlOperation
from quote.util.loginfo import Loginfo
from quote.util.yamloperation import Yamloperation


class Loginpage:

    def __init__(self):
        self.op = WebOperation(UseBrowser.driver)
        self.exl = ExlOperation()
        self.yam = Yamloperation('../../config/ecation.yaml')
        self.log = Loginfo()

    def login(self,username,password):
        self.log.set_message('info','打开网址')
        self.op.open_url(self.exl.get_cell_value(1,1))
        self.log.set_message('info','输入用户名'+username)
        self.op.input_text_name(self.yam.get_locator('LoginPage','username'),username)
        self.log.set_message('info', '输入密码' + password)
        self.op.input_text_name(self.yam.get_locator('LoginPage','password'),password)
        self.op.click_xpath(self.yam.get_locator('LoginPage','submit'))

    # 获取正确信息功能
    def get_success_text(self):
        self.op.change_frame(self.yam.get_locator('LoginPage','framemain'))
        return self.op.get_text_xpath(self.yam.get_locator('LoginPage','successinfo'))
        # print(self.op.get_text_xpath('/html/body/table/tbody/tr[1]/td/span'))

    # 获取登录失败的文本信息
    def get_failed_text(self):
        return self.op.get_text_xpath(self.yam.get_locator('LoginPage','failedinfo'))


# if __name__ == '__main__':
#     ub = UseBrowser()
#     login = Loginpage()
#     login.login('admin','admin')
#     print(login.get_success_text())
#     # print(login.get_failed_text())
#     ub.quit()