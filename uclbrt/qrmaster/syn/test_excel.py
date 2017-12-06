# encoding=utf-8
import xlrd
data  = xlrd.open_workbook('./excel.xlsx')
table = data.sheet()[0]
print(table.row_values(2))