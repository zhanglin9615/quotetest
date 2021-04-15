import unittest

from quote.base.usebrowser import UseBrowser
from quote.page.loginpage import Loginpage
from quote.util.exloperation import ExlOperation


class LoginFailedCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ub = UseBrowser()
        self.login_page = Loginpage()
        self.exl = ExlOperation()

    def test_1_name_pwd_null(self):
        self.login_page.login(self.exl.get_cell_value(2,2),self.exl.get_cell_value(2,3))
        self.assertEqual(self.login_page.get_failed_text(),self.exl.get_cell_value(2,4))


    def test_2_pwd_error(self):
        self.login_page.login(self.exl.get_cell_value(3,2),self.exl.get_cell_value(3,3))
        self.assertEqual(self.login_page.get_failed_text(),self.exl.get_cell_value(3,4))

    def tearDown(self) -> None:
        UseBrowser.quit()


if __name__ == '__main__':
    unittest.main()
