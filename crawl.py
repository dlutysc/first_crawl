# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:52:36 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:04:01 2018

@author: Administrator
"""
 
import requests
import os
from bs4 import BeautifulSoup#导入BeautifulSoup模块
 
# 在本地新建一个文件夹，保存下载的图片
folder = 'test_img'
if not os.path.exists(folder):
    os.makedirs(folder)
 
# 爬取对象是百度贴吧，爬取本网页中，能年玲奈的33张图片
img_url = 'http://tieba.baidu.com/p/2708004726'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
          (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
 
# 定义下载图片的函数
def download(url):
    response = requests.get(url, headers = header)
    name = url.split('/')[-1]
    f = open(folder + '/tieba/' + name , 'wb')
    f.write(response.content)
    f.close()
    return True
 
# 获取网页的response类、html
img_response = requests.get(img_url, headers = header)
img_html = img_response.text
 
# 获取网页的soup类；
img_soup = BeautifulSoup(img_html, 'html.parser')
 
# 本次实例的重点：bs4包中的find_all函数，变量是html的标签tag和属性attrs，依此两个量来定位src所在位置，返回的是bs4类
img = img_soup.find_all('img', attrs = {'class':'BDE_Image'})
 
# 循环函数，用bs4的get函数，直接获取src的属性值，即是图片对应的网址
for img_src in img:
    img_src = img_src.get('src')
    print(img_src)
    download(img_src)
 
print('OK')
 


