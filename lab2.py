from dl1 import filename2dir, get_html_from_local, save_to_local
from bs4 import BeautifulSoup as bs
import bs4
import os

'''
本段代码为prototype。
想解决的问题：
	0805版本基础上，更自动&精确地从页面提取内容部分，而保留格式（分段，粗体等）
观察：
	所有文字内容都在叶子结点上，<span>标签下
思路：
	循环自动输出，用好find_all(),children()
'''

def save_strlist_to_local(list1, filename):
	str1 = ''
	for l_temp in list1:
		print(type(l_temp.prettify()))
		str1 = str1 + '\n' + l_temp.prettify()
	save_to_local(str1, filename)

# # show string (str) is under which node
# def where_is_string(str):
# 	pass

# Get all tag leaves of HTML tree... 
# NOT WORKING WELL, most returns are just <br/>, and <span> is not seen
def get_leaf(tag):
	global type1

	print('aaa')
	leaf = []
	# l1 = tag.contents
	# if not(isinstance(l1, type1)): 
	if not(isinstance(tag, type1)): 
		print('bbb') 
		pass
	elif tag.contents == []:
		leaf = [tag]
	else:
		for tag1 in tag.contents:
			leaf = leaf + get_leaf(tag1)
	return leaf


# a random chosen soup for test
# html = get_html_from_local("Computational Fairy Tales Stories by Level.html") 
html = get_html_from_local("10.html")
soup = bs(html, features="lxml")

# # Show data type
# print(type(soup)) # <class 'bs4.BeautifulSoup'>
# print(type(soup.body)) # <class 'bs4.element.Tag'>
# print(type(soup.children)) # <class 'list_iterator'>
# print(soup.children) # <list_iterator object at 0x107f505e0>
# # a = (soup.children[1]); print(type(a)) # TypeError: 'list_iterator' object is not subscriptable

# # Get all tag leaves of HTML tree... 
# type1 = type(soup.body)
# print(type1)
# # l1 = get_leaf(soup) # AttributeError: type object 'BeautifulSoup' has no attribute 'element'
# l1 = get_leaf(soup.body)
# # type1 = type(soup.body) # class 'bs4.element.Tag'
# # type1 = type(soup.contents) # class 'list' 
# # type1 = type(soup.contents[0]) # class 'bs4.element.Tag'
# # print(type1)
# print(l1)
# i=0
# for tag1 in l1:
# 	# os.system("clear")
# 	print(tag1)
# 	for par1 in tag1.parents:
# 		print(par1.name)
# 	# print(tag1.parents.name)
# 	i = i+1
# 	print(i)
# 	answer = input("continue? - type enter / stop? - type s+enter")
# 	if answer == "s":
# 		break

span_list = soup.find_all(class_ = 'post-body entry-content') 

# Traverse <span>
# 
# span_list = soup.find_all(name = 'span')
# print(span_list) # too long
i = 0
ylist = []
for span in span_list:
	os.system("clear")
	print(span)
	print(type(span))
	i = i+1
	print('No. '+str(i))
	answer = input('''
Continue? - type enter /n
Record this one? - type 'r'+enter/n
Quit? - type ‘q’+enter
''')
	if answer == "r":
		ylist.append(span)
	if answer == "q":
		break
print(ylist)
save_strlist_to_local(ylist,'10_test.html')

print("done")