import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/")
browser.maximize_window()
title = browser.title
print(title)

assert "The Internet" in title

browser.find_element(By.XPATH,"//a[normalize-space()='A/B Testing']").click()

time.sleep(2)
browser.quit()
