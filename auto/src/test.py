#incoding=utf-8
import xlwt
import xlrd
import os
import requests
import json
from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd

class test:
    __title = ['Url','Method','Param','Head','Status','Reponse']
    def __init__(self):
        if not os.path.isfile('excel.xls'):
            wbk = xlwt.Workbook()  
            sheet = wbk.add_sheet('自动化测试')   
            for index, value in enumerate(self.__title):
                wbk(0, index, value)  
            wbk.save('excel.xls')  

    def write(self, row, status, text):
        rb = open_workbook('excel.xls', formatting_info=True)
		#获取工作表
        r_sheet = rb.sheet_by_index(0) # read only copy to introspect the file
        wb = copy(rb) # a writable copy (I can't read values out of this, only write to it)
        w_sheet = wb.get_sheet(0) # the sheet to write to within the writable copy
        w_sheet.write(row, 4, status)
        w_sheet.write(row, 5, text)
        wb.save('excel.xls')  
 
    def read(self):
        data = xlrd.open_workbook('excel.xls')
        table = data.sheets()[0]
        nrows = table.nrows
        for row in range(nrows): 
            if row != 0:
                url = table.cell(row, 0).value
                d = eval(table.cell(row,2).value)
                r = requests.post(url, data=d)
                self.write(row, r.status_code, r.text)
