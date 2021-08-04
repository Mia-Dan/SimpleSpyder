import requests as rq
from bs4 import BeautifulSoup as bs
import re
import os

def filename2dir(filename):
    code_dir = os.path.dirname(__file__)
    file_path = os.path.join(code_dir, filename)   
    return file_path

# 获得某页面的html内容
def get_html_from_url(rooturl, encoding="utf-8"):
    # 默认解码方式utf-8
    response = rq.get(rooturl)
    response.encoding = encoding
    html = response.text
    return html  # 返回链接的html内容。str格式吧%%%

# 获得某页面的html内容
def get_html_from_local(filename):
    file_path = filename2dir(filename)
    with open(file_path,'r') as f:
        data_read = f.read()
    return data_read

# 获得某html下的所有超链接
def get_href(html):
    # 使用BeautifulSoup函数解析传入的html
    soup = bs(html, features="lxml")
    allnode_of_a = soup.find_all("a")
    result = [_.get("href") for _ in allnode_of_a]
    return result

# 筛除结果中非链接的元素
def filterurl(result):
    # result参数：get到的所有a标签内href的内容
    # 对列表中每个元素进行筛选
    urlptn = r"http://(.+)"  # 匹配模式: 所有http://开头的链接
    urls = [re.match(urlptn, str(_)) for _ in result]  # 正则筛选
    while None in urls:
        urls.remove(None)  # 移除表中空元素
    urls = [_.group() for _ in urls]  # group方法获得re.match()返回值中的字符
    return urls

# 提取页面标题
def fetch_page_title(html):
    soup = bs(html, features="lxml")
    title = soup.title.string
    return title

# WO: 由url list
# def create_contents(filename, urls):
#     file_path = filename2dir(filename)
#     with open(file_path,'w') as f:
#         i = 0
#         for url in urls: 
#             title = fetch_page_title(html)
#             f.write(i + ' ' + title + '\n')
#             i = i+1

# 为已经下载的页面生成目录。
## 更好的方法是，获取页面（以变量形式存在）后直接soup解析出它的title，再保存。
def create_contents(urls):
    filename = '0 content'
    file_path = filename2dir(filename)
    with open(file_path,'w') as f:
        i = 0
        for url in urls: 
            html = get_html_from_local(str(i)+'.txt') # 假定所有页面以 1.txt 样式命名
            title = fetch_page_title(html)
            f.write(str(i) + ' ' + title + '\n')
            i = i+1


# main程序段 --------------------------------
if __name__ == '__main__':
    # 1. 提取网页的所有链接
    # html = get_html_from_url("https://computationaltales.blogspot.com/p/stories-by-level.html")  
    html = get_html_from_local("Computational Fairy Tales Stories by Level.html") 

    result = get_href(html)
    urls = filterurl(result) # filter urls
    # print(urls)

    # # 2. 下载所有链接页面
    # i=0
    # for url in urls:
    #     tmphtml = get_html_from_url(url)
    #     filewriter = open(str(i)+'.html','w')
    #     filewriter.write(tmphtml +'\n')
    #     filewriter.close()
    #     # 显示进度
    #     i=i+1
    #     print(i)

    # # 3. 生成下载页面的目录
    # create_contents(urls)


    soup = bs(html, features="lxml")

    # filename = 'prettifed.html'
    # file_path = filename2dir(filename)
    # with open(file_path,'w') as f:
    #     f.write(soup.prettify())
    # node = <a href="http://computationaltales.blogspot.com/2011/03/loops-and-making-horseshoe.html">Loops and Making Horseshoes</a>

    text1 = "Loops and Making Horseshoes"

    x1 = soup.find_all(recursive = True, text = text1)
    print(x1)
    print(type(x1))
    # y1 = x1[0].find_parents()
    # print(y1)


    # 其他尝试
    # soup.get_text() 对于本页面的效果不太好，太多导航栏内容混进去了

    print('done')




