# encoding=utf-8
from bs4 import BeautifulSoup
import re
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<table>123</table>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'html.parser')
# print(soup.p.attrs['name'])
# print(soup.p['class'])
# print(soup.p.get('class'))
# print(soup.p.get('class'))
# print(type(soup.p.string))
# print(soup.a.string)
# print(soup.p.children)
# for child in soup.body.children:
#     print(child)
# print(soup.body.contents[1])
# for child in soup.descendants:
#     print(child)
# print(soup.strings)
# for i  in soup.strings:
#     print(i)
# print(soup.strings)
# for i  in soup.stripped_strings:
#     print(i)
# content = soup.head.title.string
# for parent in content.parents:
#     print(parent.name)
# print(soup.p.next_sibling.next_sibling)
# print(soup.p.prev_sibling)
# print(soup.head.next_element)#next_element部分层次
# for element in soup.head.next_elements:
#     print(element)
# print(soup.find_all('b')[0])
# for tag in soup.find_all(re.compile('^b')):
#     print(tag.name)
# print(soup.find_all(['a','b']))
# print(soup.find_all(href=re.compile('lacie')))
# print(soup.find_all('a',class_='sister'))
# data_soup = BeautifulSoup('<div data-foo="value">foo!</div>','html.parser')
# print(data_soup.find_all(attrs={"data-foo": "value"}))
print(soup.find_all(text="Elsie"))
# print(soup.find_all(text=re.compile("Dormouse")))
