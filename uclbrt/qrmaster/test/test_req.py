#encoding=utf-8
import requests
host_client = 'http://115.29.142.212:8020'
params ={
    'no':'dddd',
    'return':'/userCenter.html'
}
req_url = host_client+'/Home/CommunityPage/entry.html'
requests.get(req_url,params=params)