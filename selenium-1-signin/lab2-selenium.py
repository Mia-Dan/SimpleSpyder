from selenium import webdriver

''' 通过Chrome浏览器，在Bing中搜索“这是一段搜索关键字”
'''

driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 以防因页面元素未加载全，后续可能会出现ElementNotInteractableException

driver.get("https://cn.bing.com")
# element = driver.find_element_by_id("sb_form") # ElementNotInteractableException
element = driver.find_element_by_id("sb_form_q")
element.send_keys("这是一段搜索关键字")
ele = driver.find_element_by_id("sb_form_go")
ele.click()

a = input('enter to continue') # 效果类似断点，无特殊意义
driver.close()
driver.quit()


