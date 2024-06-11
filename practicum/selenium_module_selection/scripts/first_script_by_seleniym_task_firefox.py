import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#иницилизирую драйвер браузера
driver = webdriver.Firefox()

# через get мы говорим браузеру что обращаемся к странице
try:
    driver.get('https://erikdark.github.io/Qa_autotest_02/')
    input = driver.find_elements(By.CSS_SELECTOR,'input')
    for i in input:
        i.send_keys('Text')

    time.sleep(3)

finally:
    driver.quit()