import time

from selenium import webdriver
from selenium.webdriver.common.by import By

screen_sizes = [(720,1080), (1080,720), (375,667),(912,1368)]
for height,width in screen_sizes:
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")
    driver.set_window_size(width,height)
    driver.find_element(By.XPATH,"//a[normalize-space()='Broken Images']" ).click()
    time.sleep(2)
    driver.quit()


