import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(4)
    driver.quit()


# проверяем валидацию всех пользователей
def test_login_valid(browser):
    browser.get('https://erikdark.github.io/QA_DIPLOM/')
    browser.find_element(By.XPATH, "//a[contains(@href, 'login.html')]").click()

    users = [{'login': 'user1', 'password': 'Pass1234'},
             {'login': 'user2', 'password': 'Pass1234'},
             {'login': 'user3', 'password': 'Pass1234'},
             {'login': 'user4', 'password': 'Pass1234'},
             {'login': 'user5', 'password': 'Pass1234'}]

    for user in users:
        login_input = browser.find_element(By.ID, 'login')
        login_input.clear()
        login_input.send_keys(user['login'])
        password_input = browser.find_element(By.ID, 'password')
        password_input.clear()
        password_input.send_keys(user['password'])
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        text = browser.find_element(By.ID,'loginMessage').text
        assert 'Вход успешен!' == text


# создаем нового пользователя и проверяем валидацию
def test_creat_new_user(browser):
    browser.get('https://erikdark.github.io/QA_DIPLOM/')
    browser.find_element(By.XPATH, "//a[contains(@href, 'login.html')]").click()

    login_new_input = browser.find_element(By.ID, 'newLogin')
    password_new_input = browser.find_element(By.ID, 'newPassword')
    login_new_input.send_keys('User1234')
    password_new_input.send_keys('Pass1234')

    submit_button = browser.find_element(By.CSS_SELECTOR, "#addUserForm button[type='submit']")
    submit_button.click()
    text = browser.find_element(By.ID,'addUserMessage').text
    assert 'Пользователь добавлен!' == text

    login_input = browser.find_element(By.ID, 'login')
    login_input.send_keys('User1234')
    password_input = browser.find_element(By.ID, 'password')
    password_input.send_keys('Pass1234')
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    text = browser.find_element(By.ID,'loginMessage').text
    assert 'Вход успешен!' == text


# Создаем сразу 3х пользователей и проверяем их валидацию
def test_tree_users(browser):
    browser.get('https://erikdark.github.io/QA_DIPLOM/')
    browser.find_element(By.XPATH, "//a[contains(@href, 'login.html')]").click()
    
    new_users = [{'login': 'user21', 'password': 'Pass1234'},
            {'login': 'user22', 'password': 'Pass1234'},
            {'login': 'user23', 'password': 'Pass1234'}]    

    for user in new_users:
        login_new_input = browser.find_element(By.ID, 'newLogin')
        password_new_input = browser.find_element(By.ID, 'newPassword')
        login_new_input.send_keys(user['login'])
        password_new_input.send_keys(user['password'])
        submit_button = browser.find_element(By.CSS_SELECTOR, "#addUserForm button[type='submit']")
        submit_button.click()
        text = browser.find_element(By.ID,'addUserMessage').text
        assert 'Пользователь добавлен!' == text


    for user in new_users:
        login_input = browser.find_element(By.ID, 'login')
        login_input.clear()
        login_input.send_keys(user['login'])
        password_input = browser.find_element(By.ID, 'password')
        password_input.clear()
        password_input.send_keys(user['password'])
        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        text = browser.find_element(By.ID,'loginMessage').text
        assert 'Вход успешен!' == text
