
"""
login:  testuser
password: password123

Ваша задача написать автотест (pytest)
со следующим набором действий
1 Открыть страницу
2 Авторизоваться под логином и паролем(рабочими)
3 Дождаться того что попап закроется
4 Если логин или пароль отличаются получить сообщение
5 Войти без пароля (получить сообщение)
6 Войти без логина(получить сообщения)
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(browser):
    browser.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')

    open_modal_button = browser.find_element(By.ID, 'openModalButton')
    open_modal_button.click()


    login_modal = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'loginModal')))

    # Авторизация с правильным логином и паролем
    username_input = browser.find_element(By.ID, 'username')
    password_input = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.XPATH, "//form[@id='loginForm']/button")

    username_input.send_keys('testuser')
    password_input.send_keys('password123')
    login_button.click()

    WebDriverWait(browser, 10).until_not(EC.visibility_of_element_located((By.ID, 'loginModal')))

def test_login_invalid(browser):
    browser.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')


    open_modal_button = browser.find_element(By.ID, 'openModalButton')
    open_modal_button.click()

    # Ждем, пока попап откроется
    login_modal = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'loginModal')))

    # Авторизация с неправильным логином и паролем
    username_input = browser.find_element(By.ID, 'username')
    password_input = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.XPATH, "//form[@id='loginForm']/button")

    username_input.send_keys('testuse')
    password_input.send_keys('password12')
    login_button.click()

    WebDriverWait(browser, 10).until_not(EC.visibility_of_element_located((By.ID, 'loginModal')))

def test_login_no_log(browser):
    browser.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')


    open_modal_button = browser.find_element(By.ID, 'openModalButton')
    open_modal_button.click()

    login_modal = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'loginModal')))

    # Авторизация без логина
    username_input = browser.find_element(By.ID, 'username')
    password_input = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.XPATH, "//form[@id='loginForm']/button")

    username_input.send_keys('')
    password_input.send_keys('password123')
    login_button.click()


    WebDriverWait(browser, 10).until_not(EC.visibility_of_element_located((By.ID, 'loginModal')))

def test_login_no_pass(browser):
    browser.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')

    open_modal_button = browser.find_element(By.ID, 'openModalButton')
    open_modal_button.click()

    login_modal = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'loginModal')))

    # Авторизация без пароля
    username_input = browser.find_element(By.ID, 'username')
    password_input = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.XPATH, "//form[@id='loginForm']/button")

    username_input.send_keys('testuser')
    password_input.send_keys('')
    login_button.click()

    WebDriverWait(browser, 10).until_not(EC.visibility_of_element_located((By.ID, 'loginModal')))