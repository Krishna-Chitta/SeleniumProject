from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://the-internet.herokuapp.com/"
driver.get(url)
driver.execute_script("window.scrollTo(0,600)")
driver.find_element(By.CSS_SELECTOR,"a[href='/frames']").click()

driver.close()
