import sys
sys.path.append('D:\\python\\pythonWork')
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from HwTestReport import HTMLTestReportEN
from quote.base.usebrowser import UseBrowser
from quote.page.loginpage import Loginpage
from quote.util.exloperation import ExlOperation
from quote.webtest.customertest.customersuccesstest import CustomerSuccCase
from quote.webtest.customertest.custommodifysucctest import CustomModifyCase
from quote.webtest.logintest.loginfailedtest import LoginFailedCase


class LoginSuccessCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ub = UseBrowser()
        self.login_page = Loginpage()
        self.exl = ExlOperation()

    def test_1_case(self):
        self.login_page.login(self.exl.get_cell_value(1,2),self.exl.get_cell_value(1,3))
        self.assertEqual(self.login_page.get_success_text(),self.exl.get_cell_value(1,4))

    def tearDown(self) -> None:
        UseBrowser.quit()



if __name__ == '__main__':
    suite = unittest.TestSuite()

    case_login_success = unittest.TestLoader().loadTestsFromTestCase(LoginSuccessCase)
    case_login_failed = unittest.TestLoader().loadTestsFromTestCase(LoginFailedCase)
    case_customer_success = unittest.TestLoader().loadTestsFromTestCase(CustomerSuccCase)
    case_customer_modify_success = unittest.TestLoader().loadTestsFromTestCase(CustomModifyCase)

    case_content = [case_login_success,case_login_failed,case_customer_success,case_customer_modify_success]
    # case_content = [case_login_success,case_login_failed]
    suite.addTests(case_content)

    file_date = time.strftime('%Y-%m-%d %H_%M_%S')
    # 报告文件
    with open('../../report/report.html','wb+') as fp:
        runner = HTMLTestReportEN(stream=fp, verbosity=2, title='quote report', description='UI Automation')
        runner.run(suite)
    # unittest.main()
