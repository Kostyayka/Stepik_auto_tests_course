from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    I_want = browser.find_element(By.XPATH, "//button[@type='submit']")
    I_want.click()

    new_wind = browser.window_handles[1]

    browser.switch_to.window(new_wind)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
