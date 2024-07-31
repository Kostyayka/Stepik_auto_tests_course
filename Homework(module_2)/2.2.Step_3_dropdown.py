from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    def suma(a, b):
        return a + b

    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)
    y_element = browser.find_element(By.ID, "num2")
    y = int(y_element.text)

    suma_elements = suma(x, y)

    selectik = Select(browser.find_element(By.TAG_NAME, "select"))
    selectik.select_by_value(str(suma_elements))

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
finally:
    time.sleep(10)
    browser.quit()

