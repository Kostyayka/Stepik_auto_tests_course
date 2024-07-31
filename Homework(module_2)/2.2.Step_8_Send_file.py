from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Nery")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Princ")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("ggggggg@gmail.com")

    send_file = browser.find_element(By.ID, "file")
    send_file.send_keys("C:/Users/Настя/PycharmProjects/pythonProject/Pest.txt")

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)

    browser.quit()
