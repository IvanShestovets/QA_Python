import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(1)
    driver.quit()

link1 = "https://erikdark.github.io/zachet_selenium_01/"
link2 = "https://erikdark.github.io/SHADOM-DOM-SELENIUM-QA/?name=df&email=EFE%40MAIL.RU"


def test_reg(browser):
    browser.get(link1)
    register_link = browser.find_element(By.CSS_SELECTOR, '[href="register.html"]')
    register_link.click()

    browser.find_element(By.ID, 'name').send_keys('Ivan')
    browser.find_element(By.ID, 'email').send_keys('admin123@qwq.ru')
    browser.find_element(By.ID, 'password').send_keys('password123')

    register_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    register_button.click()

    success_message = browser.find_element(By.ID, 'register-message').text
    assert "Пользователь зарегистрирован" in success_message


def test_login(browser):
    browser.get(link1)
    login_link = browser.find_element(By.CSS_SELECTOR,"[href='login.html']")
    login_link.click()

    browser.find_element(By.ID, 'email').send_keys('admin123@qwq.ru')
    browser.find_element(By.ID, 'password').send_keys('password123')

    login_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    login_button.click()

    success_message = browser.find_element(By.ID, 'login-message').text
    assert "Пользователь вошел в систему" in success_message


def test_logout(browser):
    browser.get(link1)
    profile_link = browser.find_element(By.CSS_SELECTOR, "[href='profile.html']")
    profile_link.click()

    logout_button = browser.find_element(By.ID, 'logout-button')
    logout_button.click()

    success_message = browser.find_element(By.ID, 'logout-message').text
    assert "Пользователь вышел из системы" in success_message


def test_sort_table(browser):    
    browser.get(link1)
    browser.find_element(By.CSS_SELECTOR,'[href="table.html"]').click()
    th_head=browser.find_elements(By.CSS_SELECTOR,'th')

    for i in range(len(th_head)):
        th_head[i].click()
        tr_body=browser.find_elements(By.CSS_SELECTOR,'tbody tr')
        tc=[]
        for tr in tr_body:
            tc.append(tr.text.split()[i])
        tcreverse=sorted(tc)
        tcreverse.reverse()

        assert tc in [sorted(tc),tcreverse],f'Таблица не отсортирована по столбцу {i+1}'


def test_dynamic(browser):
    browser.get(link1)
    dynamic_link = browser.find_element(By.CSS_SELECTOR,"[href='dynamic.html']")
    dynamic_link.click()

    add_button = browser.find_element(By.ID, 'add-element')
    add_button.click()

    success_message = browser.find_element(By.ID, 'content-area').text
    assert "Новый элемент" in success_message

    success_message2 = browser.find_element(By.ID, 'content-area').text
    assert "Элемент добавлен" in success_message2


def test_shadow(browser):
    browser.get(link2)

    shadow_host = browser.find_element(By.ID, "shadow-host")
    shadow_root = browser.execute_script("return arguments[0].shadowRoot", shadow_host)

    shadow_host_two = shadow_root.find_element(By.ID, "shadow-host-two")
    shadow_root_two = browser.execute_script("return arguments[0].shadowRoot", shadow_host_two)

    form = shadow_root_two.find_element(By.ID, "complex-form")

    name_input = form.find_element(By.ID, "name")
    email_input = form.find_element(By.ID, "email")

    name_input.send_keys("Ivan")
    email_input.send_keys("ivan@ex.com")

    submit_button = form.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
