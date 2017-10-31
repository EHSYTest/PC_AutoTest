from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.ehsy.com")
driver.implicitly_wait(30)
driver.maximize_window()