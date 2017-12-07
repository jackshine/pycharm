# encoding=utf-8
import requests
import qrmaster
import meizhu
import qrm_login_hash
import DataClass
# 锁掌柜
qrm_client = 'http://115.29.142.212:8020'

# 锁掌柜bpass
qrm_bpass = "http://115.29.142.212:8021"

# 美住
mz_client = 'http://115.29.142.212:8010'

#美住bpass
mz_bpass = 'http://115.29.142.212:8012'


# 新建美住客栈，通过审核，新建房间，在锁掌柜同步集群，同步房间，修改房间为二维码房间，
if __name__ == "__main__":

    # 1、美住：登陆美住客栈
    mz_client_s = requests.session()
    mz_client_s.get(mz_client + '/Home/BookPage/index.html')
    data = DataClass.DataClass()
    mz_login_account =data.get_mz_login_data()[0]
    mz_client_s.post( mz_client + '/Home/Public/login', data=mz_login_account)

    #  2、美住：创建美住客栈
    mz = meizhu.MeizhuClass(mz_client, mz_bpass)
    # mz.mz_add_hotel(mz_client_s, data.get_mz_data())
    #
    #   3、登陆bpass
    # mz_bpass_s = requests.session()
    # # 得到bpass_login_data
    # bpass_login_data = data.get_mz_login_data()[1]
    # mz_bpass_s = mz.mz_login_bpass(mz_bpass_s, bpass_login_data)
    # #
    # #  4、美住客栈通过审核
    # mz.mz_bpass_pass_hotel(mz_bpass_s, data.get_mz_data()['hotel'])
    #
    #  5、美住新建房间

    # mz.mz_add_room(mz_client_s,data.get_mz_room_data())
    # #
    # #
    # # # 6、登陆锁掌柜
    qrm_client_s = requests.session()
    qrm_community_data = data.get_qrm_data()
    print(qrm_community_data)
    html_doc = qrm_client_s.get(qrm_client + '/login.html').text
    s = qrm_login_hash.HashClass()
    hash = s.get_hash_value(html_doc)
    qrm_client_data = s.handle_hash(data.get_qrm_login_data()[0], hash)
    qrm_client_s.post(qrm_client + '/Home/Public/login', data=qrm_client_data)
    # #
    # # # 7、进入锁掌柜同步中心，登陆美住账号,同步集群,同步房间
    qrm = qrmaster.QrmasterClass(qrm_client,qrm_bpass)
    qrm.syn_community(qrm_client_s)
    # #
    # # # 8、切换到同步集群,修改房间类型为二维码房间
    qrm_client_s = qrm.change_commuity(qrm_client_s, qrm_community_data)
    qrm.update_room_type(qrm_client_s)
    # #
    # # #9、锁掌柜申请认证
    qrm.qrm_apply_verity(qrm_client_s)
    # #
    # # #10 登陆锁掌柜bpass，通过认证
    qrm_bpass_s = requests.session()
    qrm.qrm_bpass_login(qrm_bpass_s, data.get_qrm_login_data()[1])
    qrm.pass_group_verity(qrm_bpass_s, qrm_community_data)




