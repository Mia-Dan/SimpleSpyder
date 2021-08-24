'''从dmzj下载某一页的漫画图片'''

import requests
import os

def filename2dir(filename):
    code_dir = os.path.dirname(__file__)
    file_path = os.path.join(code_dir, filename)   
    return file_path

def get_this_image(referer_url, im_url):
    '''给定章节地址referer_url*，以及<img>对应的im_url；获取图片。
    * 这是由于dmzj在访问漫画图片时检查referer的合法性'''
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'referer': referer_url,
        }
    image_response = requests.get(im_url, headers=headers)
    return image_response

def save_this_image(image_response, num):
    '''检查图片是否获取成功（状态码==200），并保存。'''
    if image_response.status_code == 200:
        file_path = filename2dir('img/' + str(num) + '.jpg')
        if not os.path.exists(file_path):
             with open(file_path,"wb") as f:
                 f.write(image_response.content)
                 print("saved")
    else:
        print(image_response.status_code)


referer_url = "https://manhua.dmzj.com/xingsedeyijushi/119351.shtml"
im_url = "https://images.dmzj.com/x/%E5%B9%B8%E8%89%B2%E7%9A%84%E4%B8%80%E5%B1%85%E5%AE%A4/%E7%AC%AC50%E8%AF%9D/pic_001.jpg"
image_response = get_this_image(referer_url, im_url)
save_this_image(image_response, num=1)