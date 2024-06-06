import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

#иницилизирую драйвер браузера
driver = webdriver.Chrome()
# driver.implicitly_wait(0.5)

try:
    driver.get('https://erikdark.github.io/QA_autotest_16/')

    price_element = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'price1'), '550'))

    if price_element:
        buy_button = driver.find_element(By.ID, 'buyButton1').click
        message = driver.find_element(By.ID,'message1')
        assert 'Вы успешно купили автомобиль' in message.text
        print('Все ОК!')

finally:
    time.sleep(3)
    driver.quit()
