from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin


try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/execute_script.html')
    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    x = str(log(abs(12*sin(x))))
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(x)
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.CSS_SELECTOR, '#answer'))
    browser.find_element(By.CSS_SELECTOR, '.form-check-label[for="robotCheckbox"]').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()


finally:
    sleep(15)
    browser.quit()