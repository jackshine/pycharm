# encoding=utf-8
import requests
import hashlib
from bs4 import BeautifulSoup
import json
import re


class QrmasterClass:
    # 切换集群
    qrm_client = ''
    qrm_bpass = ''

    def __init__(self, qrm_client, qrm_bpass):
        self.qrm_client = qrm_client
        self.qrm_bpass = qrm_bpass

    def change_commuity(self, s, qrm_community_data):
        info = s.get(self.qrm_client + '/userCenter.html')
        main_info = BeautifulSoup(info.text, "html.parser")
        com_list = main_info.find('ul', id='communitySwitch')
        no_a = com_list.find('ul', class_='dropdown-menu')
        a_list = no_a.find_all('a')
        group_no = 0
        for i in a_list:
            if qrm_community_data['cname'] in i.string:
                group_no = i['data-value']
        # 获取no，发送请求
        group_data = {
            'no': group_no,
            'return': '/userCenter.html'
        }
        s.get(self.qrm_client + '/Home/CommunityPage/entry.html', params=group_data)
        s.get(self.qrm_client + '/userCenter.html')
        return s


    # 申请审核
    def qrm_apply_verity(self, s):
        img_url = self.up_image(s)
        apply_data = {
            "isforeign": "0",
            "companyname": "畅联",
            "address": "guangdong",
            "representative": "555",
            "telephone": "13480251015",
            "fax": "",
            "business": "444",
            "bpath": img_url,
            "areaCode": "86"
        }
        response = s.post(self.qrm_client + '/Home/CommunityCenter/postAuthenticationCompany', data=apply_data).json()


    # 上传图片
    def up_image(self, s):
        img_file = {
            'config': (None, 'comVerify'),
            'file': open(r'./verify.png', 'rb')}
        response = s.post(self.qrm_client + '/Home/File/upload', files=img_file).json()
        file_url = response['data']['filename']
        return file_url


    # 同步美住客栈
    def syn_community(self, s):
        s = self.syn_login_meizhu(s)
        resp_data = s.post(self.qrm_client + '/Home/Sync/getHotel').json()
        com_data = resp_data['data'][-1]
        # 此时得到的com_data 中的communityid是为0
        params = {
            "hotelid": com_data["hotelentity_id"],
            "hotelname": com_data["name"],
            "communityid": com_data["communityid"],
            "universaltime_id": com_data["universaltime_id"],
            "communityname": com_data["name"]
        }
        data = {
            "hotels": '[' + json.dumps(params, ensure_ascii=False) + ']'
        }
        syn_url = self.qrm_client + '/Home/Sync/syncCommunity'
        s.post(syn_url, data=data)
        # 重复请求getHotel 得到community_no
        resp_data = s.post(self.qrm_client + '/Home/Sync/getHotel').json()
        com_data = resp_data['data'][-1]
        com_data['communityid'] = com_data['communityid']

        # 同步房间
        hotel_data = {
            'hotelId': com_data["hotelentity_id"],
            'communityId': com_data["communityid"],
        }
        res = s.post(self.qrm_client + '/Home/Sync/getRoom', data=hotel_data).json()
        print(res)
        room_dict = {}
        room_list = []
        room_str = ''
        for room in res['data'][0]['room']:
            room_dict['id'] = room['id']
            room_dict['name'] = room['name']
            room_list.append(room_dict)
            room_str = room_str + json.dumps(room_dict) + ','
        add_room_data = {
            'hotelId': com_data["hotelentity_id"],
            'communityId': com_data["communityid"],
            'builderName': '楼栋1',
            'builderNum': '1',
            'floorName': '楼层1',
            'floorNum': '1',
            'roomsAdd': '[' + room_str[0:room_str.__len__() - 1] + ']',
        }
        s.post(self.qrm_client + '/Home/Sync/syncRoomAdd', data=add_room_data)


    #修改锁的类型为二维码
    def update_room_type(self, s):
        req_url = self.qrm_client + '/Home/Room/saveRoom'
        room_data = self.get_all_room_info(s)
        for i in range(room_data.__len__()):
            for single_room in room_data:
                single_room['locktype'] = '1'
                s.post(req_url, data=single_room)

    #得到锁掌柜所有的房间信息
    def get_all_room_info(self, s):
        # 得到每个房间页面的请求链接
        req_index_url = self.qrm_client + '/room.html'
        room_html = s.get(req_index_url)
        soup = BeautifulSoup(room_html.text, "html.parser")
        div_tag = soup.find('div', id='doc-center-page')
        # print(table.tbody.tr.next_sibling.next_sibling)
        page_url = div_tag.find_all('a')
        page_url = page_url[:-page_url.__len__():-1]
        page_url_list = []
        for i in page_url:
            page_url_list.append(i['href'])
        page_url_list.append('room_1.html')
        list_data = []
        for url in page_url_list:
            # 房间id:'room' 房间名：'name'房间号:'no' 锁编号：'num' 锁类型'locktype'
            req_url = self.qrm_client + '/' + url
            data = s.get(req_url)
            soup = BeautifulSoup(data.text, "html.parser")
            table_soup = soup.find('table', id='roomTable')
            tr_list = table_soup.tbody.find_all('tr')
            # 计算tr的数量，得到有多少个房间
            num = 0
            for i in tr_list:
                num += 1
            tr_soup = table_soup.tbody.tr
            td_soup = tr_soup.td
            count = 0
            while True:
                data = {}
                for i in range(16):
                    td_soup = td_soup.next_sibling
                data_room = {}
                data_room['room'] = td_soup['data-value']
                data_room['name'] = td_soup['data-name']
                data_room['no'] = td_soup['data-no']
                data_room['num'] = td_soup['data-num']
                data_room['locktype'] = td_soup['data-locktype']
                list_data.append(data_room)
                count += 1
                if count == num:
                    break
                tr_soup = tr_soup.next_sibling
                td_soup = tr_soup.td
        return list_data

    # 在锁掌柜登陆美住账号
    def syn_login_meizhu(self, s):
        sync_switch_url = self.qrm_client + '/Home/Sync/switchAccount'
        data = {
            'meizhu': '13326528030',
            'password': '111111b',
            'areaCode': '86'
        }
        s.post(sync_switch_url, data=data)
        return s


    # 锁掌柜bpass
    def qrm_bpass_login(self, s, qrm_bpass_data):
        html_doc = s.get(self.qrm_bpass+'/Bpass/Public/login.html').text
        soup = BeautifulSoup(html_doc, 'html.parser')
        img = soup.find("img", {"id": "imgcode"})
        print(img)
        img_path = self.qrm_bpass + img["src"]
        # req.get()得到一个response对象，对象存服务器返回的信息，
        # 返回的页面会存在.content和.text对象。
        # .content返回的是字节码
        # .text存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串。
        while True:
            image = s.get(img_path, stream=True).content
            with open('./qrm_vcode.jpg', 'wb') as fd:
                fd.write(image)
            vcode = input("请输入验证码")
            qrm_bpass_data['vcode'] = vcode
            r = s.post(self.qrm_bpass +'/Bpass/Public/doLogin', data=qrm_bpass_data).json()
            if r['status'] == 200:
                break


    #锁掌柜通过认证
    def pass_group_verity(self, req, qrm_community_data):
                query_verify_url = self.qrm_bpass + '/Bpass/ComAuthority/company.html'
                group_data = {
                    'type': '',
                    'status': '',
                    'name': qrm_community_data['cname'],
                    'no': ''
                }
                print(group_data)
                query_group = req.get(query_verify_url, params=group_data)
                soup = BeautifulSoup(query_group.text, 'html.parser')
                s_table = soup.find('table', id='questionTalbe')
                a_list = s_table.find_all('a')
                a_href = a_list[-1]['href']
                reObj1 = re.compile('[0-9]+')
                id = reObj1.findall(a_href)[0]
                page_id = reObj1.findall(a_href)[1]
                # 通过审核
                verify_page_url = self.qrm_bpass + '/Bpass/ComAuthority/companyStatus/id/' + id + '/userloginID/' + page_id + '.html'
                verify_data = {
                    "id": (None, id),
                    "status": (None, "3"),
                    "agencyId": (None, "1"),
                    "representative": (None, "33323"),
                    "hotelSign": (None, "00000"),
                    "brandTypeId": (None, "1"),
                    "typeSignId": (None, "1"),
                    "authorityNote": (None, "22244"),
                }
                req.post(verify_page_url, files=verify_data)

    # 新建美住客栈，通过审核，新建房间，在锁掌柜同步集群，同步房间，修改房间为二维码房间，
