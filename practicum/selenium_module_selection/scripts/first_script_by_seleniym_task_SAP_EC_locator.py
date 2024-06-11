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
    driver.get('https://erikdark.github.io/QA_autotest_stop_list/')

    inputfield = driver.find_element(By.CSS_SELECTOR,'#inputField')
    btn = driver.find_element(By.CSS_SELECTOR,'#submitButton')
    result = driver.find_element(By.CSS_SELECTOR,'#result')

    inputText = 'Erik'
    inputfield.send_keys(inputText)
    btn.click()

    condition = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#result'),f'Введенный текст: {inputText}'))

    assert condition == True

finally:
    time.sleep(3)
    driver.quit()
