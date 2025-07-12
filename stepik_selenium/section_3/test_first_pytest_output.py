#import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestFirstUnittest():

    '''Пишем свой первый юнит тест'''

    def test_first_without_error(self):
        link1 = "http://suninjuly.github.io/registration1.html"  # Первая линка с успешной
        link2 = "https://suninjuly.github.io/registration2.html"  # Вторая линка с багом
        browser = webdriver.Chrome()
        browser.get(link1)  # Меняй номер ссылки тут ;)

        # Мой код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR,
                             '.form-control.first:not([placeholder="Input your phone:"])').send_keys('Guts')
        browser.find_element(By.CSS_SELECTOR,
                             '.form-control.second:not([placeholder="Input your address"])').send_keys('Grifitov')
        browser.find_element(By.CSS_SELECTOR, '.form-control.third').send_keys('kaskuotimeli@mail.ru')
        browser.find_element(By.CSS_SELECTOR, '[placeholder = "Input your phone:"]').send_keys('12345562')
        browser.find_element(By.CSS_SELECTOR, '[placeholder = "Input your address:"]').send_keys('Midland 44')
        time.sleep(3)
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert("Congratulations! You have successfully registered!" == welcome_text, 'Ya upal')

        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_second_with_error(self):

        link1 = "http://suninjuly.github.io/registration1.html"  # Первая линка с успешной
        link2 = "https://suninjuly.github.io/registration2.html"  # Вторая линка с багом
        browser = webdriver.Chrome()
        browser.get(link2)  # Меняй номер ссылки тут ;)

        # Мой код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR,
                             '.form-control.first:not([placeholder="Input your phone:"])').send_keys('Guts')
        browser.find_element(By.CSS_SELECTOR,
                             '.form-control.second:not([placeholder="Input your address"])').send_keys('Grifitov')
        browser.find_element(By.CSS_SELECTOR, '.form-control.third').send_keys('kaskuotimeli@mail.ru')
        browser.find_element(By.CSS_SELECTOR, '[placeholder = "Input your phone:"]').send_keys('12345562')
        browser.find_element(By.CSS_SELECTOR, '[placeholder = "Input your address:"]').send_keys('Midland 44')
        time.sleep(3)
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert("Congratulations! You have successfully registered!" == welcome_text, 'Ya upal')

        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    pytest.main()