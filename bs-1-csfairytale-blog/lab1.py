from dl1 import filename2dir, get_html_from_local, save_to_local
from bs4 import BeautifulSoup as bs
import os

'''
本段代码为prototype。
想解决的问题：
	0804版本 下载的html用浏览器打开，页面加载很慢。
探索：
	断开网络后本地页面加载很快；
	访问这些页面对应的网址，速度也很慢（如果不是超时无法打开）。
推测：
	页面某些地方渲染需要网络。
==========
0807更新：
	更加精确的内容定位。
==========
问题再分析：
	部分页面，如29.html，涉及图片；
	然而本地保存的html内未包含图片，需联网载入；
	“断开网络后本地页面加载很快”是因为断网后不再尝试加载图片。
下一步：
要解决的问题：
	下载器应能保存图片。
推测：
	修改get_html_from_url()，使能保存图片。
	推测会进一步涉及request库的使用。
'''

# # 0805 ver: a prototype that works
# # 思路：删减不必要的板块，提高页面打开速度。
# for i in range(87): # 0.txt to 86.txt
# 	filename = str(i)+".txt"
# 	html = get_html_from_local(filename)
# 	soup = bs(html, features="lxml")
# 	target_index = 5
# 	temp_tag = soup.body.contents[target_index]
# 	save_to_local(temp_tag.prettify(), filename)

# 	print(i) # show current progress


# 0807 ver: a prototype that works
# 思路：锁定需要的tag，保存它们。

def save_taglist_to_local(taglist, filename):
	str1 = ''
	for tag1 in taglist:
		print(type(tag1.prettify()))
		str1 = str1 + '\n' + tag1.prettify()
	save_to_local(str1, filename)

# prototype 0807-2
for i in range(87): # 0.txt to 86.txt
	filename = str(i)+".html"
	html = get_html_from_local(filename)
	soup = bs(html, features="lxml")
	# selected content
	#   manually: 通过观察html文件，分析出目标结点的特征（e.g. tag的class）
	#   取出这些结点，保存为列表taglist
	taglist = []
	taglist.extend(soup.find_all(class_ = 'date-header')) 
	taglist.extend(soup.find_all(class_ = 'post-title entry-title')) 
	taglist.extend(soup.find_all(class_ = 'post-body entry-content')) 
	taglist.extend(soup.find_all(class_ = 'comments')) 
	taglist.extend(soup.find_all(class_ = 'post-labels')) 
	save_taglist_to_local(taglist, filename)

	print(i) # show current progress


print("done")