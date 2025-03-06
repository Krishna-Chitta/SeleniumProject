from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

userName = "standard_user"
password = "secret_sauce"
loginURL = "https://www.saucedemo.com/v1/"
driver.get(loginURL)
driver.maximize_window()
username_field = driver.find_element(By.XPATH,"//input[@id='user-name']")
password_field = driver.find_element(By.ID,"password")
login_button = driver.find_element(By.ID,"login-button")

username_field.send_keys(userName)
password_field.send_keys(password)
assert not login_button.get_attribute("disabled")
login_button.click()

pass_case = driver.find_element(By.XPATH,"//div[@class='product_label']")
print(pass_case.text)
assert pass_case.text == "Products"



driver.quit()
