from selenium import webdriver
import requests
import time
import os

def filename2dir(filename):
    code_dir = os.path.dirname(__file__)
    file_path = os.path.join(code_dir, filename)   
    return file_path

referer_page = "https://manhua.dmzj.com/xingsedeyijushi/119351.shtml"
page = 1
im = "https://images.dmzj.com/x/%E5%B9%B8%E8%89%B2%E7%9A%84%E4%B8%80%E5%B1%85%E5%AE%A4/%E7%AC%AC50%E8%AF%9D/pic_001.jpg"
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'referer': referer_page,
    }
image_response = requests.get(im, headers=headers)

if image_response.status_code == 200:
    file_path = filename2dir('img/' + str(page) + '.jpg')
    if not os.path.exists(file_path):
         with open(file_path,"wb") as f:
             f.write(image_response.content)
else:
    print(image_response.status_code)

# chapter_url = "https://manhua.dmzj.com/xingsedeyijushi/119351.shtml"
# image_urls = get_image_from_chapter(chapter_url)
# saveImage(image_urls)