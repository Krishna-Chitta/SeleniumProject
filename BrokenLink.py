import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")


driver.close()
