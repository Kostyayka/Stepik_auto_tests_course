from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    button_1 = browser.find_element(By.ID, "robotCheckbox")
    button_1.click()

    button_2 = browser.find_element(By.ID, "robotsRule")
    button_2.click()

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
