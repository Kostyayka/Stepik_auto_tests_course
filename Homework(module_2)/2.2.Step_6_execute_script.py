from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    button_1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_1)
    button_1.click()

    button_2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_2)
    button_2.click()

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()
