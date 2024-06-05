import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.ui import Select

#иницилизирую драйвер браузера
driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/QA_autotests_09/')
    time.sleep(2)
    challenge_element = driver.find_element(By.ID, "challenge")
    challenge_text = challenge_element.text
    print(challenge_text)

    # Используем регулярное выражение для нахождения чисел в тексте
    numbers = [int(num) for num in re.findall(r'\d+', challenge_text)]
    # Сложение чисел
    result = sum(numbers)

    select_element = Select(driver.find_element(By.ID, "answerSelect"))

    # Задаем строковое значение числа
    target_number = str(result)

    # Выбор числа в элементе select по его значению
    select_element.select_by_value(target_number)
    # Нажимаем кнопку
    btn = driver.find_element(By.CSS_SELECTOR, '#submitBtn')
    btn.click()
    time.sleep(3)

    text = driver.find_element(By.CSS_SELECTOR,'#message').text
    assert 'You guessed it! Well done!' == text
    print("Текст совпадает!")

finally:
    driver.quit()