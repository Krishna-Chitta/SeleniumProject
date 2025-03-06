import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")
linktoclick = driver.find_element(By.LINK_TEXT,"File Download")
driver.maximize_window()
linktoclick.click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.minimize_window()
driver.maximize_window()

driver.quit()
