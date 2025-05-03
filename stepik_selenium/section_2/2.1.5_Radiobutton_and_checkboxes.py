from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html')
    sleep(2)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value')
    print(type(x_element))
    x = x_element.text
    y = calc(x)
    print(type(x))
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

    browser.find_element(By.CSS_SELECTOR, '.form-check-label').click()
    sleep(1)
    browser.find_element(By.CSS_SELECTOR, '.form-check-label[for="robotsRule"]').click()
    sleep(1)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()


finally:
    sleep(10)
    browser.quit()

