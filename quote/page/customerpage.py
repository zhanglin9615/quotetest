import time

from quote.base.usebrowser import UseBrowser
from quote.base.weboperation import WebOperation
from quote.page.loginpage import Loginpage
from quote.util.exloperation import ExlOperation


class Customerpage:

    def __init__(self):
        self.op = WebOperation(UseBrowser.driver)
        self.loginpage = Loginpage()
        self.exl = ExlOperation()

    # 客户添加
    def add_customer(self,customerNO,customerName,phone,address,relationman,otherInfo):
        self.loginpage.login('admin','admin')
        self.op.change_frame('/html/frameset/frame[1]')
        self.op.click_xpath('//*[@id="Bar_panel0_b0"]/img')
        self.op.change_frame('/html/frameset/frame[2]')
        self.op.click_xpath('/html/body/center/table[2]/tbody/tr[2]/td[2]/a')
        self.op.change_window('新增客户信息')
        self.op.input_text_name('customerNO',customerNO)
        self.op.input_text_name('customerName',customerName)
        self.op.input_text_name('phone',phone)
        self.op.input_text_name('address',address)
        self.op.input_text_name('relationman',relationman)
        self.op.input_text_name('otherInfo',otherInfo)
        self.op.click_xpath('/html/body/center/form/table[2]/tbody/tr/td/input[1]')


    # 客户修改
    def modify_customer(self,customer_no,customer_name):
        self.loginpage.login(self.exl.get_cell_value(1,2),self.exl.get_cell_value(1,3))
        self.op.change_frame('/html/frameset/frame[1]')
        self.op.click_xpath('//*[@id="Bar_panel0_b0"]/img')
        self.op.change_frame('/html/frameset/frame[2]')
        i = 0
        while True:
            i += 1
            id = self.op.get_text_xpath('/html/body/center/form/table[1]/tbody/tr[{}]/td[1]'.format(i))
            if customer_no == id:
                self.op.click_xpath('/html/body/center/form/table[1]/tbody/tr[{}]/td[7]/a[2]'.format(i))
                self.op.change_window('更新客户信息')
                self.op.clear_name('customerName')
                self.op.input_text_name('customerName',customer_name)
                self.op.click_xpath('/html/body/center/form/table[2]/tbody/tr/td/input[1]')

                break


    # 获取新增成功的文本
    def get_success_text(self):
        # print(self.op.driver.title)
        return self.op.driver.title

# if __name__ == '__main__':
#     ub = UseBrowser()
#     customer = Customerpage()
#     # customer.add_customer('10004','lily','1367540917','chengdu','张三','')
#     customer.modify_customer('0201306')
#     ub.quit()