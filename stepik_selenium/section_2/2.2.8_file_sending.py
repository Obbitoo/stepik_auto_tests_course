from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/file_input.html')
    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Guts')
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Grifitov')
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('rasya@mail.like')
    browser.find_element(By.ID, 'file').send_keys('E:/file1.txt')
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

finally:
    sleep(15)
    browser.quit()