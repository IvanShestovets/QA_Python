import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#иницилизирую драйвер браузера
driver = webdriver.Chrome()

# через get мы говорим браузеру что обращаемся к странице
driver.get('https://erikdark.github.io/Qa_autotest_02/')

#с помощью команды find_element(и класса By внутри ) мы ишем нужный элемент на странце сайта, в качестве аргумента мы передаем класс поиска By и значение которое ищем.
input_one = driver.find_element(By.ID,'phone')
input_one.send_keys('+79001000000')

input_two = driver.find_element(By.ID,'email')
input_two.send_keys('Kartman@mail.com')

input_tree = driver.find_element(By.ID,'name')
input_tree.send_keys('Kartman')

input_fore = driver.find_element(By.ID,'password')
input_fore.send_keys('Kartman')

btn = driver.find_element(By.ID,'submitBtn')
#с помощью click() мы кликаем по кнопке
time.sleep(2)
btn.click()
time.sleep(5)

driver.quit()