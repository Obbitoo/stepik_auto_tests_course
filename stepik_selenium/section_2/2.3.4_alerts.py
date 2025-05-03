from selenium import webdriver
from selenium.webdriver.common.by import By
from math import *
from time import sleep

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/alert_accept.html')
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    sleep(3)
    browser.switch_to.alert.accept()
    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(str(log(abs(12 * sin(x)))))
    browser.find_element(By.CSS_SELECTOR, '.btn').click()

finally:
    sleep(15)
    browser.quit()