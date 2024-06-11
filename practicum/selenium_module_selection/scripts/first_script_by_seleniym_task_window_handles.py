import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#иницилизирую драйвер браузера
driver = webdriver.Chrome()

# через get мы говорим браузеру что обращаемся к странице
driver.get('https://erikdark.github.io/QA_autotests_13/')
# Нажмите кнопку
driver.find_element(By.CSS_SELECTOR, '#openNewPageBtn').click()
# Переключиться на новую вкладку
driver.switch_to.window(driver.window_handles[1])
# Нажмите кнопку в новой вкладке
driver.find_element(By.CSS_SELECTOR, '#displayTextBtn').click()

time.sleep(2)

display_text = driver.find_element(By.CSS_SELECTOR,'#displayText').text
assert display_text == 'Я СДЕЛАЛ', 'текст не отображается или не верный текст'
print('Test compleate!')

driver.quit()