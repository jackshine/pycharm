# coding=utf-8
import unittest
import xlrd
import xlwt
import requests
from  xlutils.copy import copy
if __name__ == '__main__':
    # 读取账号
    #         rb = xlrd.open_workbook('./meizhu_account.xlsx')
    #         # 将结果写入excel
    #         wb = copy(rb)
    #         w_sheet = wb.get_sheet(0)
    #         w_sheet.write(5, 5, '444')
    #         wb.save('./meizhu_account.xlsx')
    rb =  xlrd.open_workbook('./meizhu_account.xls')

    # 通过sheet_by_index()获取的sheet没有write()方法
    rs = rb.sheet_by_index(0)

    wb = copy(rb)

    # 通过get_sheet()获取的sheet有write()方法
    ws = wb.get_sheet(0)
    ws.write(0, 0, 'changed!')

    wb.save('./meizhu_account.xls')







