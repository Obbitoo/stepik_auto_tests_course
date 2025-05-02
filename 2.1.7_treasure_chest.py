import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/get_attribute.html')
    element = browser.find_element(By.CSS_SELECTOR, 'img[src="images/chest.png"]')
    x = element.get_attribute('valuex')
    y = calc(x)

    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
finally:
    sleep(15)
    browser.quit()