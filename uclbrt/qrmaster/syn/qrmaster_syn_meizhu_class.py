# encoding=utf-8
import requests
import qrmaster
import meizhu
# 锁掌柜
qrm_client = 'http://115.29.142.212:8020'

# 锁掌柜bpass
qrm_bpass = "http://115.29.142.212:8021"
qrm_bpass_login_url = qrm_bpass + '/Bpass/Public/doLogin'

# 美住
mz_client = 'http://115.29.142.212:8010'

#美住bpass
mz_bpass = 'http://115.29.142.212:8012'

# 锁掌柜账号
qrm_bpass_data = {
    "username": "changlian",
    "password": "49dec5fb8af4eeef7c95e7f5c66c8ae6"
}
# 锁掌柜账号
qrm_client_data = {
    "mobile": "13326528030",
    "areaCode": "86",
    "password": "bbc69d27003568a7a94626ce4337bc9d"
}
# 集群信息
qrm_community_data = {
    "universalTime": "5",
    "desc": "333",
    "type": "1",
    "addr": "11",
    "cont": "联系人",
    "phone": '13480251015',
    "areaCode": "1"
}
# 美住客栈信息
mz_hotel_data = {
    'city': '320700',
    'district': '320704',
    'universalTime': '5'
}

# 美住登陆客栈信息：
mz_login_data = {
    'mobile': '13326528030',
    'password': '111111b',
    'areaCode': '86',
}
# 新建美住客栈，通过审核，新建房间，在锁掌柜同步集群，同步房间，修改房间为二维码房间，
if __name__ == "__main__":
    # 1、美住：登陆美住客栈
    h_name = input('输入客栈名称')
    # 河源客栈-有为测试
    mz_hotel_data['hotel'] = h_name.strip()
    mz_client_s = requests.session()
    mz_client_s.get(mz_client + '/Home/BookPage/index.html')
    mz_client_s.post( mz_client + '/Home/Public/login', data=mz_login_data)
    #
    #  2、美住：创建美住客栈
    mz_add_hotel(mz_client_s)
    #
    #  3、登陆bpass
    mz_bpass_s = requests.session()
    mz_bpass_s = mz_login_bpass(mz_bpass_s)
    #
    # 4、美住客栈通过审核
    mz_bpass_pass_hotel(mz_bpass_s, h_name)
    #
    # 5、美住新建房间
    mz_add_room(mz_client_s)


    # 6、登陆锁掌柜
    qrm_client_s = requests.session()
    qrm_community_data['cname'] = h_name
    html_doc = qrm_client_s.get(qrm_client + '/login.html').text
    s = qrm_login_hash.get_Hash()
    hash = s.get_hash_value(html_doc)
    qrm_client_data = s.handle_hash(qrm_client_data, hash)
    qrm_client_s.post(qrm_client + '/Home/Public/login', data=qrm_client_data)

    # 7、进入锁掌柜同步中心，登陆美住账号,同步集群,同步房间
    syn_community(qrm_client_s)

    # 8、切换到同步集群,修改房间类型为二维码房间
    qrm_client_s = change_commuity(qrm_client_s)
    update_room_type(qrm_client_s)

    #9、锁掌柜申请认证
    qrm_apply_verity(qrm_client_s)

    #10 登陆锁掌柜bpass，通过认证
    qrm_bpass_s = requests.session()
    qrm_bpass_login(qrm_bpass_s)
    pass_group_verity(qrm_bpass_s, qrm_community_data)




