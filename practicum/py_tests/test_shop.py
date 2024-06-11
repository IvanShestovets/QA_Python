import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(3)
    driver.quit()

def test_go_to_offers_page(browser):
    browser.get("http://selenium1py.pythonanywhere.com/ru/")

# Основное меню
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dropdown-menu")))
    dropdown_menu = browser.find_element(By.CLASS_NAME, "dropdown-menu")
# Переход "Предложения" в меню
    offers_link = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Предложения")))
    offers_link.click()
# Книга 1 "Добавить в корзину"
    add_to_cart_form = browser.find_element(By.CSS_SELECTOR, "form[action='/ru/basket/add/209/']")
    add_to_cart_form.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Книга 2 "Добавить в корзину"
    add_to_cart_form = browser.find_element(By.CSS_SELECTOR, "form[action='/ru/basket/add/208/']")
    add_to_cart_form.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Книга 3 "Добавить в корзину"
    add_to_cart_form = browser.find_element(By.CSS_SELECTOR, "form[action='/ru/basket/add/207/']")
    add_to_cart_form.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Книга 4 "Добавить в корзину"
    add_to_cart_form = browser.find_element(By.CSS_SELECTOR, "form[action='/ru/basket/add/206/']")
    add_to_cart_form.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Переходим в корзину
    browser.find_element(By.XPATH, "//a[contains(@href, '/ru/basket/')]").click()
# Переход к оформлению
    browser.find_element(By.XPATH, "//a[contains(@href, '/ru/checkout/')]").click()
# Ищем и заполняем поля логин и пароль 
    username_input = browser.find_element(By.ID, 'id_username')
    password_input = browser.find_element(By.ID, 'id_password')

    username_input.send_keys('testuser@wew.ru')
    password_input.send_keys('password123')
#  Породолжить
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
# форма регистрации
    name_input = browser.find_element(By.ID, 'id_first_name')
    name2_input = browser.find_element(By.ID, 'id_last_name') 
    adres_input = browser.find_element(By.ID, 'id_line1') 
    city_input = browser.find_element(By.ID, 'id_line4')
    post_input = browser.find_element(By.ID, 'id_postcode') 

    name_input.send_keys('Ivan')
    name2_input.send_keys('Sheff')
    adres_input.send_keys('street')
    city_input.send_keys('SPb')
    post_input.send_keys('1001')

#  Породолжить
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#  Породолжить   
    browser.find_element(By.XPATH, "//a[contains(@href, 'ru/checkout/preview/')]").click()








