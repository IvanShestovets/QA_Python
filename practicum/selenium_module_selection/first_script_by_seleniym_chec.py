import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#иницилизирую драйвер браузера
driver = webdriver.Chrome()

# time.sleep(5)
try:
    # через get мы говорим браузеру что обращаемся к странице
    driver.get('https://erikdark.github.io/Qa_autotest_01/')
    time.sleep(2)
    #с помощью команды find_element(и класса By внутри ) мы ишем нужный элемент на странце сайта, в качестве аргумента мы передаем класс поиска By и значение которое ищем.
    input_one = driver.find_element(By.ID,'inputField')

    #с помощью send_keys(мы записываем данные в поле)
    input_one.send_keys('Картман')
    time.sleep(5)

    btn = driver.find_elements(By.CSS_SELECTOR,'.btn')
    print(len(btn))
    if len(btn) == 8:
        print('ок')
    else:
        print('no')

#с помощью click() мы кликаем по кнопке
# btn.click()
    time.sleep(5)
finally:
    driver.quit()