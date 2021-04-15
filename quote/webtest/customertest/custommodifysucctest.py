import unittest

from quote.base.usebrowser import UseBrowser
from quote.db.dbcustomer.dbcustomoperation import DbCustomoperation
from quote.page.customerpage import Customerpage
from quote.util.exloperation import ExlOperation


class CustomModifyCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ub = UseBrowser()
        self.customer_page = Customerpage()
        self.exl = ExlOperation('E:\\test\\logincase.xlsx','customer修改用例')
        self.db = DbCustomoperation()

    def test_1_customer_name(self):
        res = self.db.select_customer(self.exl.get_cell_value(1,2))
        self.customer_page.modify_customer(self.exl.get_cell_value(1,2),self.exl.get_cell_value(1,3))
        self.assertEqual(self.customer_page.get_success_text(),self.exl.get_cell_value(1,4))
        self.db.modify_customer([res[0]['customerName'],self.exl.get_cell_value(1,2)])

    def tearDown(self) -> None:
        UseBrowser.quit()


if __name__ == '__main__':
    unittest.main()
