#encoding=utf-8
import requests
import time
import os
import urllib.request
from bs4 import BeautifulSoup
#广州-客栈 13326528030
cookies = {
    "mz_UCLBRTUID" : "0a2c9f6f-61e6-4860-b80b-6565969b6695",
    "mz_UCLBRTUSSID":"ckdGuvD7RCuZi0PU9CQEG4w46BxB1K4j%2FWbBYLyQZORe7QtJXw7C1f4%2FObvLLLWkNsavh4u0rvzTqgsFJ0yj%2FesRvSG7b12VRwpyDae%2FhKTbUCVTBTPao0OlS%2BBlSTB5D59I07%2BlzWsvyqbBHAphFVDz4oJXz0jop3QoG7G6jkEMs7HhCrltoWMYaJq4Hn6NRMQ7Pz1nQkBJSnj88nsGcJd9n2yuvaJ4hxIayJiG1IDuHEZ1exzO8Ctf6X%2FYSf0TRZiKAT9x3B3WlEwyIKCXA7%2BOITkIXkrXhXtRwBXka99PUM9shrehJP6FyWQjz%2F7szipbIcE%2B826FL6gQo0jwiA%3D%3D",
    "mz_UCLBRTUSSPS":"b425a3c2bc4f5045d71b99b6540fcece08abe89b5924e0250bb51737495fd5f62df07ba1ddbe987449f228a9e7cf6699aa2596159210af6b33e5b3097ff313f2",
    "mz_UCLBRTPSTM":"1510414270",
    "mz_think_language":"zh_cn",
    "mz_room_view_style":"1",
    "master_session_id":"1vlvsmllah845sep076qg0g693",
    "qrm_community_identity":"P1D3MQVxdpVJLzdY",
    "monitor_count":"70",
    "qrm_think_language":"zh_cn"}
host = "http://115.29.142.212:8020"
url = "/room.html"
link = host+url
print(link)
#page = urllib.request.urlopen(link)
req = requests.get(link,cookies=cookies)
html_doc = req.text
soup = BeautifulSoup(html_doc)
#print(soup.prettify())

#print(soup.prettify())
#print(soup.find_all('td',attrs={'class':'col-xs-3'}))

