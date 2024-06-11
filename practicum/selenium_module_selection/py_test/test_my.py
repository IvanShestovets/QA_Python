import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
"""
login:  testuser
password: password123

Ваша задача написать автотест (pytest)
со следующим набором действий
Открыть страницу
Авторизоваться под логином и паролем(рабочими)
Дождаться того что попап закроется
Если логин или пароль отличаются получить сообщение
Войти без пароля (получить сообщение)
Войти без логина(получить сообщения)
"""

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit

@pytest.fixture
def login_driver(driver):
    driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')





