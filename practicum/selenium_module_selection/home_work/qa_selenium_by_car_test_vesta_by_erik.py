import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
price = (By.ID, 'price1')
btn = (By.ID, 'buyButton1')
msg = (By.ID, 'message1')

try:
    driver.get('https://erikdark.github.io/QA_autotest_16/')
    wait = WebDriverWait(driver,10)
    price_element = wait.until(EC.presence_of_element_located((price)))

    while True:
        current_price = int(price_element.text)

        if current_price == 550:
            buy_btn = driver.find_element(*btn).click()

            message_element = driver.find_element(*msg)
            if 'Вы успешно купили автомобиль!' in message_element.text:
               print('Успех')
            else:
                print('Не успех')
            break
        time.sleep(1)

finally:
    time.sleep(1)
    driver.quit()
