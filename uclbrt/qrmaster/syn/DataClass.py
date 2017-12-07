# encoding=utf-8
import xlrd
class DataClass:
    def __init__(self):
        pass
    def get_sheet(self):
        data = xlrd.open_workbook('./excel.xlsx')
        sheet = data.sheet_by_index(0)
        return sheet
    def get_qrm_login_data(self):
        sheet = DataClass.get_sheet(self)
        qrm_client_data = {}
        qrm_client_data['mobile'] = str(int(sheet.cell(1, 1).value))
        qrm_client_data['areaCode'] = str(int(sheet.cell(2, 1).value))
        qrm_client_data['password'] = str(sheet.cell(3, 1).value)
        qrm_bpass_data = {}
        qrm_bpass_data['username'] = str(sheet.cell(1, 5).value)
        qrm_bpass_data['password'] = str(sheet.cell(2, 5).value)
        return qrm_client_data, qrm_bpass_data
    def get_mz_login_data(self):
        sheet = DataClass.get_sheet(self)
        mz_login_data = {}
        mz_login_data['mobile'] = str(int(sheet.cell(1, 3).value))
        mz_login_data['password'] = str(sheet.cell(2, 3).value)
        mz_login_data['areaCode'] = str(int(sheet.cell(3, 3).value))
        mz_bpass_login = {}
        mz_bpass_login['username'] = str(sheet.cell(1, 7).value)
        mz_bpass_login['password'] = str(sheet.cell(2, 7).value)
        return mz_login_data, mz_bpass_login
    def get_qrm_data(self):
        sheet = DataClass.get_sheet(self)
        qrm_community_data = {}
        qrm_community_data['cname'] = str(sheet.cell(5, 1).value)
        qrm_community_data['universalTime'] = str(int(sheet.cell(6, 1).value))
        qrm_community_data['desc'] = str(sheet.cell(7, 1).value)
        qrm_community_data['type'] = str(int(sheet.cell(8, 1).value))
        qrm_community_data['addr'] = str(sheet.cell(9, 1).value)
        qrm_community_data['cont'] = str(sheet.cell(10, 1).value)
        qrm_community_data['phone'] = str(int(sheet.cell(11, 1).value))
        qrm_community_data['areaCode'] = str(int(sheet.cell(12, 1).value))
        return qrm_community_data
    def get_mz_data(self):
        sheet = DataClass.get_sheet(self)
        mz_hotel_data = {}
        mz_hotel_data['hotel'] = str(sheet.cell(5, 3).value)
        mz_hotel_data['city'] = str(int(sheet.cell(6, 3).value))
        mz_hotel_data['district'] = str(int(sheet.cell(7, 3).value))
        mz_hotel_data['universalTime'] = str(int(sheet.cell(8, 3).value))
        return mz_hotel_data
    def get_mz_room_data(self):
        sheet = DataClass.get_sheet(self)
        mz_room_data = {}
        room = ''
        for i in range(int(sheet.cell(5, 5).value)):
            room = room + str(i+1)+','
        mz_room_data['room'] = room[:room.__len__()-1:]
        mz_room_data['name'] = str(sheet.cell(6, 5).value)
        mz_room_data['price'] = str(int(sheet.cell(7, 5).value))
        return mz_room_data
if __name__ == '__main__':
    m = DataClass()
    print(m.get_mz_room_data())

