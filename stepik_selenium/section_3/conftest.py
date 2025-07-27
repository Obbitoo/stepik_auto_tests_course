import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='function')
def browser():
    print("\nНАЧАЛО РАБОТЫ БРАУЗЕРА")
    browser = webdriver.Chrome()
    yield browser
    print("\nКОНЕЦ РАБОТЫ БРАУЗЕРА")
    browser.quit()
