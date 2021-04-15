import unittest

from quote.base.usebrowser import UseBrowser
from quote.db.dbcustomer.dbcustomoperation import DbCustomoperation
from quote.page.customerpage import Customerpage


class CustomerSuccCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)
    def setUp(self) -> None:
        self.ub = UseBrowser()
        self.customer = Customerpage()
        self.dbcustomer = DbCustomoperation()

    def test_1_no(self):
        self.dbcustomer.delete_customer_account('10007')
        self.customer.add_customer('10007','lily','1367540917','chengdu','张三', '备注')
        self.assertEqual(self.customer.get_success_text(),'添加记录成功')


    def tearDown(self) -> None:
        UseBrowser.quit()

if __name__ == '__main__':
    unittest.main()
