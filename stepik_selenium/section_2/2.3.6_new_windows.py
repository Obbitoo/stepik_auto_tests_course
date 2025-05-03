from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import *

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/redirect_accept.html')
    browser.find_element(By.CSS_SELECTOR, '.trollface.btn').click()
    browser.switch_to.window(browser.window_handles[1])
    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(str(log(abs(12 * sin(x)))))
    browser.find_element(By.CLASS_NAME, 'btn').click()
finally:
    sleep(10)
    browser.quit()
