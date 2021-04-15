import xlrd


class ExlOperation:
    def __init__(self,path=None,sheet_name=None):
        if path == None:
            path = '../../config/Autocase.xlsx'
        else:
            path=path

        if sheet_name == None:
            sheet_name = '用例参数'
        else:
            sheet_name=sheet_name

        self.workbook = xlrd.open_workbook(path)
        self.sheet = self.workbook.sheet_by_name(sheet_name)

    # 获取行
    def get_row(self):
        return self.sheet.nrows

    # 获取列
    def get_col(self):
        return self.sheet.ncols

    # 获取单元格内容
    def get_cell_value(self,nrow,ncol):
        # print(self.workbook)
        return self.sheet.cell_value(nrow,ncol)



# ex = ExlOperation()
# print(ex.get_cell_value(1,2))