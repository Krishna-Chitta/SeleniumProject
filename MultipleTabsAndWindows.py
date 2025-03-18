from selenium.webdriver.common.by import By
from selenium import webdriver
import time

browser = webdriver.Chrome()
url1 = "https://www.selenium.dev/"
url2 = "https://playwright.dev/python/"
browser.get(url1)
browser.maximize_window()
browser.switch_to.new_window()
browser.get(url2)
NumberOfTabs = len(browser.window_handles)
print(NumberOfTabs)
tabs_value = browser.window_handles
print(tabs_value)
current_tab = browser.current_window_handle
print(current_tab)
browser.find_element(By.CSS_SELECTOR, ".getStarted_Sjon").click()
FirstTab = browser.window_handles[0]
if current_tab != FirstTab:
    browser.switch_to.window(FirstTab)
browser.find_element(By.XPATH, "//span[normalize-space()='Downloads']").click()

browser.quit()
