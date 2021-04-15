import pymysql


class DbHandle:
    def __init__(self, host, path, database, username, password):
        self.host = host
        self.path = path
        self.database = database
        self.username = username
        self.password = password

    # 获取数据库链接
    def get_connect(self):
        try:
            conn = pymysql.connect(host=self.host, port=self.path, database=self.database, user=self.username,
                                   password=self.password, charset="utf8")
            return conn
        except Exception as e:
            print(e, 'connect failed')

    def sql_search(self,sql,para):
        res = None
        try:
            conn = self.get_connect()
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute(sql,para)
            conn.commit()
            res = cursor.fetchall()

        except Exception as e:
            conn.rollback()
            print(e, 'sql operation error')
        finally:
            cursor.close()
            conn.close()

        return res

    # 增、删、改
    def sql_modify(self,sql,para):
        try:
            conn = self.get_connect()
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute(sql,para)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e, 'sql operation error')
        finally:
            cursor.close()
            conn.close()



# db = DbHandle('localhost', 3306, 'quote', 'root', '123456')
# print(db.sql_search('select * from tb_customer where customerNO=%s','0201306'))
# db.sql_modify('delete from tb_customer where customerNO=%s',['23'])