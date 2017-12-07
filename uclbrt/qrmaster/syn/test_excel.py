# encoding=utf-8
import xlrd
data  = xlrd.open_workbook('./excel.xlsx')
table = data.sheet_by_index(0)
qrm_client_data = {}
qrm_client_data['mobile'] = str(int(table.cell(1,1).value))
qrm_client_data['areaCode'] = str(int(table.cell(2,1).value))
qrm_client_data['password'] = str(table.cell(3,1).value)
print(qrm_client_data)
mz_login_data = {}
mz_login_data['mobile'] = str(int(table.cell(1,3).value))
mz_login_data['password'] = str(table.cell(2,3).value)
mz_login_data['areaCode'] = str(int(table.cell(3,3).value))
print(mz_login_data)
qrm_bpass_data = {}
qrm_bpass_data['areaCode'] = str(table.cell(1,5).value)
qrm_bpass_data['password'] = str(table.cell(2,5).value)

mz_bpass_login = {}
mz_bpass_login['username'] = str(table.cell(1,7).value)
mz_bpass_login['password'] = str(table.cell(2,7).value)

# 美住客栈信息
mz_hotel_data = {}
mz_hotel_data['hotel'] = str(table.cell(5,3).value)
mz_hotel_data['city'] = str(int(table.cell(6,3).value))
mz_hotel_data['district'] = str(int(table.cell(7,3).value))
mz_hotel_data['universalTime'] = str(int(table.cell(8,3).value))
print(mz_hotel_data)

qrm_community_data = {}
qrm_community_data['cname'] = str(table.cell(5, 1).value)
qrm_community_data['universalTime'] = str(int(table.cell(6, 1).value))
qrm_community_data['desc'] = str(table.cell(7, 1).value)
qrm_community_data['type'] = str(int(table.cell(8, 1).value))
qrm_community_data['addr'] = str(table.cell(9, 1).value)
qrm_community_data['cont'] = str(table.cell(10, 1).value)
qrm_community_data['phone'] = str(int(table.cell(11, 1).value))
qrm_community_data['areaCode'] = str(int(table.cell(12, 1).value))
print(qrm_community_data)


