import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://erikdark.github.io/QA_autotest_16/')
driver.implicitly_wait(5)

try:
    while True:
        price = driver.find_element(By.ID, 'price1')
        price_text = price.text
        if '550' in price_text:
            btn = driver.find_element(By.ID, 'buyButton1')
            if btn.is_enabled():
                btn.click()
                break
        time.sleep(1)

    message = driver.find_element(By.ID, 'message1')
    assert 'Вы успешно купили автомобиль!' in message.text

finally:
    time.sleep(5)
    driver.quit()
