from selenium import webdriver # 导入浏览器驱动

driver = webdriver.Chrome()
driver.implicitly_wait(10) # 若删去这句，后续可能会出现ElementNotInteractableException；因为页面元素还未加载全
driver.get("https://cn.bing.com")
# element = driver.find_element_by_id("sb_form") # ElementNotInteractableException
element = driver.find_element_by_id("sb_form_q")
element.send_keys("如何关闭微软小冰") # 模拟键盘输入 send_keys
ele = driver.find_element_by_id("sb_form_go")
ele.click() # 鼠标左键单击搜索按钮 # 如果每一句都设置一个断点，依次执行，这里会出现ElementNotInteractableException。原因不详。
a = input('aaa') # just for a pause
driver.close() # 关闭页面
driver.quit() # 关闭webdriver



