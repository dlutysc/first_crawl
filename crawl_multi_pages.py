# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 15:24:08 2018

@author: Administrator
"""

#导入第三方包和模块
import requests
from bs4 import BeautifulSoup
import os

#在本地新建一个文件夹，命名为test_img，用以保存下载的图片
folder = 'test_img'
if not os.path.exists(folder):
    os.makedirs(folder)

#定义一个函数，用以下载图片
def download(url):
    response = requests.get(url)
    name = url.split('/')[-1]
    f = open(folder + '/mlti_pages/' + name, 'wb')
    f.write(response.content)
    f.close()

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

#网页可以翻19次，相当于改变url，循环19次；然后对每一个页面都执行‘获取src’和‘下载图片’的操作
for i in range(1,20):
    url_i = 'https://tieba.baidu.com/p/4064957036?pn=' + str(i)
    response_i = requests.get(url_i, headers = header)
    print(url_i)

    #获取第i个页面的url、response类、html、soup，以及该页面所有图片对应的src
    html_i = response_i.text
    soup_i = BeautifulSoup(html_i, 'html.parser')
    imgs_i = soup_i.find_all('img', attrs = {'class':'BDE_Image'})

    for img in imgs_i:
        img_src = img.get('src')
        print(img_src)
        download(img_src)  
print('OK')
