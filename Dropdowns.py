import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
login_url = "https://the-internet.herokuapp.com/"
driver.get(login_url)
driver.find_element(By.XPATH,"//a[normalize-space()='Dropdown']").click()
dropdown_element = driver.find_element(By.ID,"dropdown")
select = Select(dropdown_element) #Select class is used to perform operations on dropdowns.
#count of total dropdowns could be obtained by using select.options
options_count = len(select.options)
# 3 different ways to perform actions on dropdowns
#select by visible_text:
select.select_by_visible_text("Option 2")
time.sleep(1)
#select by index:
select.select_by_index(1) #should select 'option 1'
time.sleep(1)
#select by option using value:
select.select_by_value("2") #should select 'option 2'
time.sleep(1)

print(options_count) #count would be 3 because it will also consider "please select an option" as an option

driver.close()