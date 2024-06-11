import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#иницилизирую драйвер браузера
driver = webdriver.Chrome()

# через get мы говорим браузеру что обращаемся к странице
driver.get('https://erikdark.github.io/QA_autotests_12/')

driver.find_element(By.CSS_SELECTOR,'#startTaskBtn').click()

confirm = driver.switch_to.alert.accept()
# confirm.accept()

prompt = driver.switch_to.alert.send_keys('50')
# prompt.send_keys('50')

confirm = driver.switch_to.alert.accept()
# confirm.accept()

time.sleep(1)

# alert = driver.switch_to.alert
# alert_text = alert.text
# assert 'Правильно! Ответ 50.' in alert_text
# alert.accept()
a = driver.switch_to.alert.text
assert 'Правильно! Ответ 50.' == a

print("Текст совпадает!")

driver.quit()