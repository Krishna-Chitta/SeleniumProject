from selenium import webdriver
from selenium.webdriver.common import by

url = "www.sf.com"
driver = webdriver.Chrome()
driver.get(url)

driver.close()
