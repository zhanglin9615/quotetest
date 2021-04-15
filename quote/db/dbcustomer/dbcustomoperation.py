from quote.db.dbhandle import DbHandle


class DbCustomoperation:
    def __init__(self):
        self.db_handle = DbHandle('localhost', 3306, 'quote', 'root', '123456')

    # 删除
    def delete_customer_account(self,customer_no):
        self.db_handle.sql_modify('delete from tb_customer where customerNO=%s',[customer_no])

    def select_customer(self,para):
        # print(para)
        return self.db_handle.sql_search('select * from tb_customer where customerNO=%s',para)

    # 修改
    def modify_customer(self,para):
        # print(para)
        self.db_handle.sql_modify('update tb_customer set customerName=%s where customerNO=%s',para)


# dbcustomer = DbCustomoperation()
# # dbcustomer.delete_customer_account()
# # dbcustomer.select_customer('0201306')
# dbcustomer.modify_customer(['周氏','0201306'])
