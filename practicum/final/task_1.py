import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(4)
    driver.quit()

def test_login_valid(browser):

        browser.get('https://erikdark.github.io/QA_DIPLOM/')

        browser.find_element(By.XPATH, "//a[contains(@href, 'registration.html')]").click()

        name_input = browser.find_element(By.ID, 'name')
        email_input = browser.find_element(By.ID, 'email')
        password_input = browser.find_element(By.ID, 'password')
        conf_password_input = browser.find_element(By.ID, 'confirmPassword')


        login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        name_input.send_keys('testuser')
        email_input.send_keys('password@fg.ru')
        password_input.send_keys('Password!123')
        conf_password_input.send_keys('Password!123')
        login_button.click()

        text = browser.find_element(By.ID,'message').text
        assert 'Регистрация успешна!' == text
        print("Текст совпадает!")

def test_login_invalid_name(browser):

        browser.get('https://erikdark.github.io/QA_DIPLOM/')

        browser.find_element(By.XPATH, "//a[contains(@href, 'registration.html')]").click()

        name_input = browser.find_element(By.ID, 'name')
        email_input = browser.find_element(By.ID, 'email')
        password_input = browser.find_element(By.ID, 'password')
        conf_password_input = browser.find_element(By.ID, 'confirmPassword')


        login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        name_input.send_keys('11')
        email_input.send_keys('password@fg')
        password_input.send_keys('Password!123')
        conf_password_input.send_keys('Password!123')
        login_button.click()

        text = browser.find_element(By.ID,'message').text
        assert 'Имя может содержать только буквы и знак "-"' == text
        print("Текст совпадает!")


def test_login_invalid_mail(browser):

        browser.get('https://erikdark.github.io/QA_DIPLOM/')

        browser.find_element(By.XPATH, "//a[contains(@href, 'registration.html')]").click()

        name_input = browser.find_element(By.ID, 'name')
        email_input = browser.find_element(By.ID, 'email')
        password_input = browser.find_element(By.ID, 'password')
        conf_password_input = browser.find_element(By.ID, 'confirmPassword')


        login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        name_input.send_keys('q')
        email_input.send_keys('password@ww')
        password_input.send_keys('Password!123')
        conf_password_input.send_keys('Password!123')
        login_button.click()

        text = browser.find_element(By.ID,'message').text
        assert 'Введите корректный email' == text
        print("Текст совпадает!")


def test_login_invalid_pass(browser):

        browser.get('https://erikdark.github.io/QA_DIPLOM/')

        browser.find_element(By.XPATH, "//a[contains(@href, 'registration.html')]").click()

        name_input = browser.find_element(By.ID, 'name')
        email_input = browser.find_element(By.ID, 'email')
        password_input = browser.find_element(By.ID, 'password')
        conf_password_input = browser.find_element(By.ID, 'confirmPassword')


        login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        name_input.send_keys('q')
        email_input.send_keys('password@ww')
        password_input.send_keys('assword!123')
        conf_password_input.send_keys('assword!123')
        login_button.click()

        text = browser.find_element(By.ID,'message').text
        assert 'Пароль должен содержать не менее 8 символов, включая 1 заглавную букву, 1 строчную букву и 1 цифру' == text
        print("Текст совпадает!")

def test_login_invalid_pass_not_conf(browser):

        browser.get('https://erikdark.github.io/QA_DIPLOM/')

        browser.find_element(By.XPATH, "//a[contains(@href, 'registration.html')]").click()

        name_input = browser.find_element(By.ID, 'name')
        email_input = browser.find_element(By.ID, 'email')
        password_input = browser.find_element(By.ID, 'password')
        conf_password_input = browser.find_element(By.ID, 'confirmPassword')


        login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

        name_input.send_keys('q')
        email_input.send_keys('password@ww.ru')
        password_input.send_keys('Password!123')
        conf_password_input.send_keys('Password!12')
        login_button.click()

        text = browser.find_element(By.ID,'message').text
        assert 'Пароли не совпадают' == text
        print("Текст совпадает!")
