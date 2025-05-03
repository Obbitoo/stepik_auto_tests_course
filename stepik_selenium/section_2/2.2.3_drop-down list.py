from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/selects1.html')
    x = int(browser.find_element(By.CSS_SELECTOR, '#num1').text)
    y = int(browser.find_element(By.CSS_SELECTOR, '#num2').text)
    c = str(x + y)
    print(c)

    d = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    d = d.select_by_visible_text(c)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    sleep(15)
    browser.quit()
