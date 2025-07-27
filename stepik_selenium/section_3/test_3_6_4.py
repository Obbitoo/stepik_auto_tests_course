import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link1 = 'https://stepik.org/lesson/236895/step/1'
incorrect_list = []

@pytest.fixture(scope='function')
def browser():
    print('\nStart browser Rasya')
    browser = webdriver.Chrome()
    yield browser
    print('\nEnded browser Rasya')
    browser.quit()
    print(''.join(incorrect_list))

class TestStepikAuthoeization():

    @pytest.mark.parametrize('links', ['https://stepik.org/lesson/236895/step/1',
                                       'https://stepik.org/lesson/236896/step/1',
                                       'https://stepik.org/lesson/236897/step/1',
                                       'https://stepik.org/lesson/236898/step/1',
                                       'https://stepik.org/lesson/236899/step/1',
                                       'https://stepik.org/lesson/236903/step/1',
                                       'https://stepik.org/lesson/236904/step/1',
                                       'https://stepik.org/lesson/236905/step/1'])
    def test_stepik(self, browser, links):
        # Открыть браузер по ссылке
        browser.get(links)
        browser.implicitly_wait(30)

        # Найти кнопку входа
        browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()
        # Ввести данные авторизации
        browser.find_element(By.CSS_SELECTOR, '[name="login"]').send_keys('stub')
        browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys('stub')
        # Нажать кнопку авторизации
        browser.find_element(By.CSS_SELECTOR, '.button_with-loader').click()
        # Отправляем ответы по линкам

        time.sleep(10)
        browser.find_element(By.CSS_SELECTOR, '.ember-text-area').send_keys(str(math.log(int(time.time()))))

        browser.find_element(By.CSS_SELECTOR, '.submit-submission[type="button"]').click()

        our_answer_value = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text

        assert our_answer_value == 'Correct!', f'Некорректное значение {incorrect_list.append(our_answer_value)}'
