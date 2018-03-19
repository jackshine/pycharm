# coding=utf-8
from openpyxl import Workbook
from openpyxl import load_workbook
if __name__ == '__main__':
    wb = load_workbook('./abc.xlsx')
    sheet = wb.active
    list = []
    b2 = sheet.cell(row=2, column=1).value
    b3 = sheet.cell(row=3, column=1).value
    list.append(b2)
    list.append(b3)
    print(list)








