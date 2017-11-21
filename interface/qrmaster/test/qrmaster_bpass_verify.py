# encoding=utf-8
import requests
from bs4 import BeautifulSoup
import re
#md5加密,返回二进制
host = "http://115.29.142.212:8021"
login_url = host+'/Bpass/Public/doLogin'
link = host+'/Bpass/Public/login.html'
data = {
    "username": "changlian",
    "password": "49dec5fb8af4eeef7c95e7f5c66c8ae6"
}
def login(req):
    html_doc =req.get(link).text
    soup = BeautifulSoup(html_doc)
    #print(soup.prettify())
    img = soup.find("img",{"id":"imgcode"})
    img_path = host+img["src"]
    #req.get()得到一个response对象，对象存服务器返回的信息，
    #返回的页面会存在.content和.text对象。
    #.content返回的是字节码
    #.text存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串。
    while True:
        image = req.get(img_path,stream=True).content
        with open('demo.jpg','wb') as fd:
            fd.write(image)
        vcode = input("请输入验证码")
        data['vcode'] = vcode
        r = req.post(login_url, data=data).json()
        print(r)
        if r['status']==200:
            break
def pass_group_verity(req):
    query_verify_url = host + '/Bpass/ComAuthority/company.html'
    group_data = {
        'type':'',
        'status':'',
        'name':'瑞士-客栈-有为测试',
        'no':''
    }
    query_group = req.get(query_verify_url,params=group_data)
    with open('./query_verify_url.txt', 'wb') as fd:
        fd.write(query_group.content)
    soup = BeautifulSoup(query_group.text)
    s_table = soup.find('table', id='questionTalbe')
    a_list = s_table.find_all('a')
    a_href = a_list[-1]['href']
    reObj1 = re.compile('[0-9]+')
    id = reObj1.findall(a_href)[0]
    page_id = reObj1.findall(a_href)[1]
    print(id,page_id)
    #通过审核
    verify_page_url = host + '/Bpass/ComAuthority/companyStatus/id/' + id + '/userloginID/' + page_id + '.html'
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
    v = req.post(verify_page_url, files=verify_data)
    print(v.text)
def pass_verity(req):
    #请求企业认证页面，获取最后一页的链接
    company_verify_url = host+'/Bpass/ComAuthority/company.html'
    response = req.get(company_verify_url)
    with open('./company_verify_page.txt','wb') as fd:
        fd.write(response.content)
    soup = BeautifulSoup(response.text)
    page_list = soup.find_all('a',class_='num')
    #得到最后一页的链接
    page_list_url = page_list[-1]['href']
    #请求最后一页的链接，获取最后一个集群的链接
    res_last_page = req.get(host+page_list_url)
    with open('./res_last_page.txt','wb') as fd:
        fd.write(res_last_page.content)
    soup = BeautifulSoup(res_last_page.text)
    last_community_list = soup.find_all('a',class_='btn btn-primary btn-sm')
    last_community = last_community_list[-1]['href']
    print(last_community)
    reObj1 = re.compile('[0-9]+')
    #得到集群的id
    id = reObj1.findall(last_community)[0]
    page_id = reObj1.findall(last_community)[1]

    #拼接审核页面，通过审核
    #http://115.29.142.212:8021/Bpass/ComAuthority/companyStatus/id/581/userloginID/1623.html
    verify_page_url = host+'/Bpass/ComAuthority/companyStatus/id/'+id+'/userloginID/'+page_id+'.html'
    print(verify_page_url)
    verify_data ={
        "id":(None,id),
        "status":(None,"3"),
        "agencyId":(None,"1"),
        "representative":(None,"33323"),
        "hotelSign":(None,"00000"),
        "brandTypeId":(None,"1"),
        "typeSignId":(None,"1"),
        "authorityNote":(None,"22244"),
    }
    v = req.post(verify_page_url,files=verify_data)
    print(v.text)
if __name__ == "__main__":
    req = requests.session()
    login(req)
    pass_group_verity(req)






