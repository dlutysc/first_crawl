# -*- coding: utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup  # 导入BeautifulSoup模块
"""
Created on Mon Nov 26 10:52:36 2018

@author: Administrator
没有抓取成功，代码有问题，还需修改
"""


# 在本地新建一个文件夹，保存下载的图片
folder = 'jiandan_img'
if not os.path.exists(folder):
    os.makedirs(folder)

# 爬取简单随手拍某页图片
imgs_url = 'http://jandan.net/top-ooxx'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
          (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}


# 定义下载图片的函数
def download(index, url):
    response = requests.get(url, headers=header)
    name = str(index)
    f = open(folder + '/' + name, 'wb')
    f.write(response.content)
    f.close()
    return True


# 获取网页的response类、html
response = requests.get(imgs_url, headers=header)
imgs_html = response.text

# 获取网页的soup类
soup = BeautifulSoup(imgs_html, 'lxml')

# 本次实例的重点：bs4包中的find_all函数，变量是html的标签tag和属性attrs，依此两个量来定位src所在位置，返回的是bs4类
imgs = soup.find_all('img')

# 循环函数，用bs4的get函数，直接获取src的属性值，即是图片对应的网址
for index, img_src in enumerate(imgs, 1):
    img_src = img_src.get('src')
    print(img_src)
    download(index, img_src)

print('OK')



