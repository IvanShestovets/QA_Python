import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re

#иницилизирую драйвер браузера
driver = webdriver.Chrome()
driver.implicitly_wait(1)

x = True

try:
    driver.get('https://erikdark.github.io/Qa_autotest_15/')
    while x == True:
        try:
            btn = driver.find_element(By.ID,'verify').click()
            message = driver.find_element(By.ID,'verify_message')
            if 'Verification successful!' in message.text:
                print('Y')
                x = False
                break
            else:
                continue
        except:
            continue

finally:
    time.sleep(3)
    driver.quit()
