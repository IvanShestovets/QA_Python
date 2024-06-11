import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/Qa_autotests_17/')

    el_1 = WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#price1'), '550'))
      
    btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'buyButton1')))
    btn.click()

    message = driver.find_element(By.ID, 'message1')
    assert 'Вы успешно купили автомобиль!' in message.text
    print('Машина 1: Все ОК!')

    el_2 = WebDriverWait(driver, 20).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#price2'), '800'))
      
    btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'buyButton2')))
    btn.click()

    message = driver.find_element(By.ID, 'message2')
    assert 'Вы успешно купили автомобиль!' in message.text
    print('Машина 2: Все ОК!')

    el_3 = WebDriverWait(driver, 120).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#price3'), '19000'))
      
    btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'buyButton3')))
    btn.click()

    message = driver.find_element(By.ID, 'message3')
    assert 'Вы успешно купили автомобиль!' in message.text
    print('Машина 3: Все ОК!')

finally:
    time.sleep(3)
    driver.quit()

