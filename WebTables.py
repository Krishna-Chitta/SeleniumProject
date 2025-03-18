import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://the-internet.herokuapp.com/"
driver = webdriver.Chrome()
driver.get(url)
driver.find_element(By.XPATH, "//a[normalize-space()='Sortable Data Tables']").click()

time.sleep(2)
driver.close()
