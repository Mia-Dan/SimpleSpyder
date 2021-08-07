from dl1 import filename2dir, get_html_from_local, save_to_local
from bs4 import BeautifulSoup as bs
'''
本段代码为prototype。
想解决的问题：
	0804版本 下载的html用浏览器打开，页面加载很慢。
探索：
	断开网络后本地页面加载很快；
	访问这些页面对应的网址，速度也很慢（如果不是超时无法打开）。
推测：
	页面某些地方渲染需要网络。
'''

# # a prototype that works
# # html = get_html_from_local("Computational Fairy Tales Stories by Level.html") 
# html = get_html_from_local("10.txt")
# soup = bs(html, features="lxml")
# a = soup.body.contents
#
# # print(len(a)) # 13
# i = 5
# # a[1],a[7] is useless at my purpose; 
# # even ones like a[0], a[2], ... are empty; 
# # only a[5] contains target content.
# print(a[i])
# print(a[i].name)
# print(type(a[i])) # <class 'bs4.element.Tag'>
# print(type(a[i].prettify())) # <class 'str'>
# # and a[i].text would throw away all the format, which is bad here.

# save_to_local(a[i].prettify(), "a"+str(i)+"_1.html") # reason: see above.

for i in range(87): # 0.txt to 86.txt
	filename = str(i)+".txt"
	html = get_html_from_local(filename)
	soup = bs(html, features="lxml")
	target_index = 5
	temp_tag = soup.body.contents[target_index]
	save_to_local(temp_tag.prettify(), filename)

	print(i)


print("done")