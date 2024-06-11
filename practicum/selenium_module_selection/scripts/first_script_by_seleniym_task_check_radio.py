import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

#иницилизирую драйвер браузера
driver = webdriver.Chrome()

# через get мы говорим браузеру что обращаемся к странице
try:
    driver.get('https://erikdark.github.io/Qa_autotests_05/')
     
    challenge_element = driver.find_element(By.ID, "challenge")
    challenge_text = challenge_element.text

    # Разбор текста для нахождения чисел и операции
    numbers = re.findall(r'\d+', challenge_text)

    # Преобразование чисел из строкового формата в целые числа и их сложение
    sum_numbers = sum([int(num) for num in numbers])
    # print("Сумма чисел:", sum_numbers)

# Ввод значения в поле инпут
    sum_inputs = driver.find_element(By.ID,'answer')
    sum_inputs.send_keys(sum_numbers) 

# Клик по чекбоксу
    checkbox = driver.find_element(By.ID, 'notRobot')
    checkbox.click()
    
# Клик по radio    
    radio = driver.find_element(By.ID, 'cool')
    radio.click()

    time.sleep(1)

# Клик по кнопке
    btn = driver.find_element(By.CSS_SELECTOR, 'button')
    btn.click()

    time.sleep(3)

# Проверка сообщения
    text = driver.find_element(By.CSS_SELECTOR,'#message').text
    assert 'Поздравляю, Elon Musk!' == text
    print("Текст совпадает!")

finally:
    driver.quit()
