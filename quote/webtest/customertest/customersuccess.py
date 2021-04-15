from quote.base.usebrowser import UseBrowser
from quote.page.customerpage import Customerpage


class Customersuccess:

    def set_up(self):
        self.ub = UseBrowser()
        self.customer = Customerpage()

    def customer_1_case(self):
        self.customer.add_customer('10005','lily','1367540917','chengdu','张三','备注')

        if self.customer.get_success_text() == '添加记录成功':
            print('pass')
        else:
            print('failed')

    def customer_2_case(self):
        self.customer.add_customer('10004','lily','1367540917','chengdu','张三','')
        if self.customer.get_success_text() == '添加记录成功':
            print('pass')
        else:
            print('failed')

    def customer_3_case(self):
        self.customer.add_customer('10004','lily','1367540917','chengdu','','')
        if self.customer.get_success_text() == '添加记录成功':
            print('pass')
        else:
            print('failed')

    def tear_down(self):
        UseBrowser.quit()


if __name__ == '__main__':
    customer = Customersuccess()
    customer.set_up()
    customer.customer_1_case()
    customer.tear_down()