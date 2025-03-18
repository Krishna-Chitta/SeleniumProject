from selenium.webdriver.common.by import By
from selenium import webdriver
import time

browser = webdriver.Chrome()
url1 = "https://www.selenium.dev/"
url2 = "https://playwright.dev/python/"
browser.get(url1)
browser.maximize_window()
