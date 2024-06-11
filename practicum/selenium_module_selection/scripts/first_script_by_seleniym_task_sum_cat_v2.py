import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

#иницилизирую драйвер браузера
driver = webdriver.Chrome()

# через get мы говорим браузеру что обращаемся к странице
try:
    driver.get('https://erikdark.github.io/Qa_autotest_07/')

    challenge_element = driver.find_element(By.ID, 'challenge')
    # Извлечение текста из элемента <div>
    challenge_text = challenge_element.text
    # Извлечение числа из текста
    number_a = int(challenge_text.split()[2])

    number_element = driver.find_element(By.ID, "numberImage")
    number_data_b = number_element.get_attribute("data-b")

    # Преобразование значения в число и добавление в переменную
    number_b = int(number_data_b)

    # Сохранение суммы чисел в переменной
    sum = number_a + number_b

    # print("Сумма чисел:", sum_numbers)

    sum_inputs = driver.find_element(By.ID, 'answer')
    sum_inputs.send_keys(sum)
    time.sleep(1)
    # Клик по кнопке
    btn = driver.find_element(By.ID, 'submitBtn')
    btn.click()
    time.sleep(5)

# Проверка сообщения
# text = driver.find_element(By.CSS_SELECTOR,'#answer').text
# assert 'Ты молодец!' == text
# print("Текст совпадает!")

finally:
    driver.quit()
