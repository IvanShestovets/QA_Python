import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(4)
    driver.quit()


# Все 3 товара добавляются в корзину без проблем
def test_shop(browser):
    browser.get('https://erikdark.github.io/QA_DIPLOM/')
    browser.find_element(By.XPATH, "//a[contains(@href, 'shop.html')]").click()

    button1 = browser.find_element(By.CSS_SELECTOR, ".products .product:nth-child(1) button.add-to-cart")
    button1.click()
    browser.switch_to.alert.accept()

    button2 = browser.find_element(By.CSS_SELECTOR, ".products .product:nth-child(2) button.add-to-cart")
    button2.click()
    browser.switch_to.alert.accept()

    button3 = browser.find_element(By.CSS_SELECTOR, ".products .product:nth-child(3) button.add-to-cart")
    button3.click()
    browser.switch_to.alert.accept()

    submit_button = browser.find_element(By.ID, "cartButton")
    submit_button.click()

    text = browser.find_element(By.ID, 'cartItems').text
    assert 'Товар 1 - $100\nТовар 2 - $200\nТовар 3 - $350' == text

    text2 = browser.find_element(By.ID,'cartTotal').text
    assert 'Общая стоимость: $650' == text2


# Убедится что если товар добавлен несколько раз он действительно несколько раз отображается в корзине
def test_shop_2(browser):
    browser.get('https://erikdark.github.io/QA_DIPLOM/')
    browser.find_element(By.XPATH, "//a[contains(@href, 'shop.html')]").click()

    button1 = browser.find_element(By.CSS_SELECTOR, ".products .product:nth-child(1) button.add-to-cart")
    button1.click()
    browser.switch_to.alert.accept()

    button1 = browser.find_element(By.CSS_SELECTOR, ".products .product:nth-child(1) button.add-to-cart")
    button1.click()
    browser.switch_to.alert.accept()

    submit_button = browser.find_element(By.ID, "cartButton")
    submit_button.click()

    text = browser.find_element(By.ID, 'cartItems').text
    assert 'Товар 1 - $100\nТовар 1 - $100' == text

    text2 = browser.find_element(By.ID,'cartTotal').text
    assert 'Общая стоимость: $200' == text2



# Убедится что стоимость товара в магазине и в корзине не отличается.
def test_compare_product_prices(browser):
    browser.get('https://erikdark.github.io/QA_DIPLOM/')
    browser.find_element(By.XPATH, "//a[contains(@href, 'shop.html')]").click()
    product_button = browser.find_element(By.CSS_SELECTOR, ".products .product:nth-child(1) button.add-to-cart")
    product_button.click()
    browser.switch_to.alert.accept()

    product_button = browser.find_element(By.CSS_SELECTOR, ".products .product:nth-child(2) button.add-to-cart")
    product_button.click()
    browser.switch_to.alert.accept()

    product_button = browser.find_element(By.CSS_SELECTOR, ".products .product:nth-child(3) button.add-to-cart")
    product_button.click()
    browser.switch_to.alert.accept()

    submit_button = browser.find_element(By.ID, "cartButton")
    submit_button.click()


    store_prices = browser.find_elements(By.CSS_SELECTOR, '.products .product p')
    store_total = sum([int(re.search(r'\d+', p.text).group()) for p in store_prices])

    # Находим общую стоимость товаров в корзине
    cart_total = browser.find_element(By.ID, 'cartTotal').text
    cart_price = int(re.search(r'\d+', cart_total).group())

    # Проверяем, что стоимость товаров в магазине и в корзине равны
    assert store_total == cart_price, "Стоимость товаров в магазине и в корзине отличается"