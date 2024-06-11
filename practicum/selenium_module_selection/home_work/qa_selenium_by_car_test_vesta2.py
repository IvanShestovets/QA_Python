import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/QA_autotest_16/')

    el = WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#price1'), '550'))
        
    btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'buyButton1'))).click()

    message = driver.find_element(By.ID, 'message1')
    assert 'Вы успешно купили автомобиль!' in message.text
    print('Все ОК!')

finally:
    time.sleep(2)
    driver.quit()
