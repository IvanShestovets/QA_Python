import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

#иницилизирую драйвер браузера
driver = webdriver.Chrome()

# через get мы говорим браузеру что обращаемся к странице
try:
    driver.get('https://erikdark.github.io/Qa_autotest_07/')
     
    image_element = driver.find_element(By.ID, 'numberImage')

    # Получение значения атрибута data-b
    data_b = image_element.get_attribute('data-b')

    # Извлечение чисел и их суммирование
    numbers = [int(num) for num in data_b.split('?') if num.isdigit()]
    sum_numbers = sum(numbers)

    # print("Сумма чисел:", sum_numbers)

    sum_inputs = driver.find_element(By.ID,'answer')
    sum_inputs.send_keys(sum_numbers) 
    time.sleep(1)   
    # Клик по кнопке
    btn = driver.find_element(By.ID, 'submitBtn')
    btn.click()
    time.sleep(1)

# Проверка сообщения
    # text = driver.find_element(By.CSS_SELECTOR,'#answer').text
    # assert 'Ты молодец!' == text
    # print("Текст совпадает!")

finally:
    driver.quit()
