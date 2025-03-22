import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Aim is to find a target value in a row.

url = "https://the-internet.herokuapp.com/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.execute_script("window.scrollTo(0,700)")
driver.find_element(By.XPATH, "//a[normalize-space()='Sortable Data Tables']").click()
table = driver.find_element(By.ID,"table1")
rows = table.find_elements(By.TAG_NAME, "tr")
row_count = len(rows) - 1
print(row_count)
target_value = "Jason"
found = False #this var is important because this will allow us to create a condition to break the first nested loop.
# Without this the loop runs for all rows as well after all the cells/ columns in a row get validated.
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        if target_value in cell.text:
            print(f"found value: {target_value}")
            found = True
            break
    if found:
        break
if not found:
    print("Not found")

time.sleep(2)
driver.close()
