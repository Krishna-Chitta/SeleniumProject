import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.XPATH,"//a[normalize-space()='Dropdown']").click()
dropdown_element = driver.find_element(By.ID,"dropdown")
select = Select(dropdown_element)
select.select_by_visible_text("Option 2")
time.sleep(1)

driver.close()