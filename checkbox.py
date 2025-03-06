import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.XPATH,"//a[normalize-space()='Checkboxes']").click()
time.sleep(2)
checkboxes = driver.find_elements(By.XPATH,"//input[@type = 'checkbox']")
checkedboxes_count = 0
uncheckedboxes_count = 0
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
    else:
        pass
time.sleep(1)
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkedboxes_count += 1
    if checkbox.is_selected() != True:
        uncheckedboxes_count += 1

print("\ntotal checkboxes checked are:", checkedboxes_count, "\ntotal checkboxes unchecked are:", uncheckedboxes_count)
driver.close()
