from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from math import *

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    # Нажатие на кнопку "Book"
    book_button = browser.find_element(By.CSS_SELECTOR, "#book")
    book_button.click()


    browser.find_element(By.CSS_SELECTOR, "#book").click()
    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    d = str(log(abs(12 * sin(x))))  
    print(x, type(x))
    print(d, type(d))
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(d)
    browser.find_element(By.CSS_SELECTOR, '#solve').click()

finally:
    sleep(10)
    browser.quit()
