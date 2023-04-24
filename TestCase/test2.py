#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
__title__=""
__author__="Administrator"
__mtime_="2018/9/12"
Fail until you fail again,this is how you succeed.

"""
import time
import re
import requests
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_vedio_url_list():
    # chrome_options=webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # locator_result=(By.XPATH,'//ul[contains(@class,"video-list")]/li/a')
    # driver=webdriver.Chrome(chrome_options=chrome_options)
    # driver.get(URL)
    # links=driver.find_elements(*locator_result)
    # for link in links:
    # video_url_list.append(link.get_attribute('href'))
    # 	video_title_list.append(link.find_element_by_class_name('title').text)
    # print("获取完视频地址列表")
    # driver.quit()
    response = urllib.urlopen(URL).read()
    list = re.findall(r'<a href="(.*?)" class="play-holder-Video-', response)
    # print response
    for url in list:
        video_url_list.append("http://www.icoolxue.com" + url)
        video_title_list.append(url)
    # video_title_list = re.findall(r'<span class=title>(.*?)</span>', response)


def download_vedio(vedio_url, vedio_title):
    Accept = 'application/json,text/javascript,*/*;q=0.01'
    Accept_Encoing = 'gzip,deflat'
    Accept_Language = 'zh-CN,zh;9=0.9'
    client = 'web'
    content_type = 'application/x-www-form-urlencoded'
    cookie = 'MEIQIA_EXTRA_TRACK_ID=1A0lelvRToHsRH0Y11oJrtbnXFu; Hm_lvt_315805d5d93485b7b39f1f10c5456261=1536571428,1536629072; JSESSIONID=fd1e8f19-e37a-452c-bf14-cc0b27f52502; Hm_lpvt_315805d5d93485b7b39f1f10c5456261=' + str(
        int(time.time())) + '; MEIQIA_VISIT_ID=1A2ohZGIXUWc6mkGpZlS7CTINAD'
    host = 'www.icoolxue.com'
    method = 'ajax'
    user_agent = 'Mozilla/5.0(Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    referer = 'http://www.icoolxue.com/play/4867'
    X_Requested_With = 'XMLHttpRequest'
    headers = {'Accept': Accept, 'Accept-Encoding': Accept_Encoing, 'Accept-Language': Accept_Language,
               'Client': client, 'Content-Type': content_type, 'Cookie': cookie, 'Host': host, 'method': method,
               'User_Agent': user_agent, 'Referer': referer, 'X-Requested-With': X_Requested_With}
    first_request_url = vedio_url.replace('play', 'video/play/url')
    r = requests.get(first_request_url, headers=headers)
    reality_vedio_url = r.json().get('data')
    resp = requests.get(reality_vedio_url)
    data = resp.content
    with open('e:\\vedio\\' + vedio_title + '.mp4', 'wb') as f:
        f.write(data)
    print("当前视频下载完成！")


if __name__ == "__main__":
    URL = "http://www.icoolxue.com/album/show/216"
    video_url_list = []
    video_title_list = []
    get_vedio_url_list()
    if len(video_url_list) != len(video_title_list):
        print (len(video_url_list))
        print (len(video_title_list))
        exit()
    # for i in range(0, len(video_url_list)):
    download_vedio(video_url_list[0], video_title_list[0])
    print("所有视频下载完成！！！")
    # print video_title_list