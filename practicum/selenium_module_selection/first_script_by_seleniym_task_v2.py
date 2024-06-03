import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#иницилизирую драйвер браузера
driver = webdriver.Chrome()

# через get мы говорим браузеру что обращаемся к странице
try:
    driver.get('https://erikdark.github.io/Qa_autotest_02/')
    data = ['7821378127','erik@mail.ru','erik','test123']
    inputs = driver.find_elements(By.TAG_NAME,'input')
    for i in range(len(inputs)):
        inputs[i].send_keys(data[i])
    btn = driver.find_element(By.CSS_SELECTOR, '#submitBtn')
    time.sleep(1)
    btn.click()
    time.sleep(3)


finally:
    driver.quit()