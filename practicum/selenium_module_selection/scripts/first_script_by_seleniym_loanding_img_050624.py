import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.ui import Select

#иницилизирую драйвер браузера
driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/QA_autotests_11/')
    time.sleep(1)
    
    driver.find_element(By.CSS_SELECTOR, '#imageInput').send_keys(r'C:\Users\AttekPC\Desktop\img1.jpg')
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    time.sleep(1)

finally:
    driver.quit()