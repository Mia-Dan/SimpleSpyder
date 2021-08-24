'''从dmzj下载某一章的漫画图片
1. 获取 图片链接 的列表 
2. 下载链接列表中所有图片
'''

from selenium import webdriver
import requests
import time
import os
from random import uniform

from lab1_tri_a_page import filename2dir, get_this_image, save_this_image
# lab1-tri-a-page invalid syntax // 要使用下划线啊 // take notes%%%

''' 1. 获取 图片链接 的列表  '''
chapter_url = "https://manhua.dmzj.com/xingsedeyijushi/119351.shtml"
webdriver = webdriver.Chrome()
webdriver.implicitly_wait(3)
webdriver.get(chapter_url)
# image_urls = webdriver.find_element_by_xpath('//html/body/div[13]/select/option') # full xpath # okay
elements = webdriver.find_elements_by_xpath('//*[@id="page_select"]/option') # xpath # okay
# elements = webdriver.find_elements_by_xpath('//*[@id="page_select"]/option@value') # not a valid XPath expression.
image_urls = [] # whose length should be len(elements)
for ele in elements:
    image_urls.append(ele.get_attribute('value'))

print(image_urls)
webdriver.close()
webdriver.quit()


''' 2. 下载链接列表中所有图片 '''
referer_url = chapter_url
i = 1
for image_url in image_urls:
    t = uniform(0,3)
    print(t)
    time.sleep(t)
    image_url = "https:" + image_url
    image_response = get_this_image(referer_url, image_url)
    save_this_image(image_response, i)
    i = i+1

print("done")






