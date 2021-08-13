from selenium import webdriver 
'''
某网课页面登陆
2 TODO's
'''

driver = webdriver.Chrome()
driver.implicitly_wait(10) 
driver.get("http://passport2.chaoxing.com/login?refer=http%3A%2F%2Fmooc1-3.chaoxing.com%2Fvisit%2Finteraction&fid=0&newversion=true&_blank=0")

driver.execute_script(f'document.getElementById("otherlogin").click();')

# TODO: read account info from file
element = driver.find_element_by_id("inputunitname")
element.send_keys("aaaaa") 
element = driver.find_element_by_id("uname")
element.send_keys("aaaaa") 
element = driver.find_element_by_id("password")
element.send_keys("aaaaa") 
# TODO: CAPTCHA auto fill
element = driver.find_element_by_id("vercode")
element.send_keys("aaaaa") 
a = input('pause') 
element = driver.find_element_by_id("loginBtn")
element.click() 

a = input('pause') 
driver.close() # 关闭页面
driver.quit() # 关闭webdriver

