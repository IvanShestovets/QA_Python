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
driver.implicitly_wait(1)

try:
    driver.get('https://erikdark.github.io/QA_autotest_16/')
    btn = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'verify'))).click()
    message = driver.find_element(By.ID,'verify_message')
    assert 'Verification successful!' in message.text


finally:
    time.sleep(3)
    driver.quit()
