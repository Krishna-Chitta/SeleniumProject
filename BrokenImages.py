from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/"
driver.get(url)
driver.find_element(By.XPATH, "//a[normalize-space()='Broken Images']").click()
images = driver.find_elements(By.TAG_NAME,"img")
broken_images = []
for image in images:
    src = image.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print("broken image found")

if broken_images:
    print("list of broken images:")
    for broken_image in broken_images:
        print(broken_image)
else:
    print("No broken images found!")

driver.quit()
