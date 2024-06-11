import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#иницилизирую драйвер браузера
driver = webdriver.Chrome()

# через get мы говорим браузеру что обращаемся к странице
try:
    driver.get('https://erikdark.github.io/Qa_autotest_04/')
    

    name_input = driver.find_element(By.ID, 'firstName')
    name_input.send_keys("A") 

    last_name_input = driver.find_element(By.ID, 'lastName')
    last_name_input.send_keys("*")

    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys("invalid-email@eeer.rr")
    phone_input = driver.find_element(By.ID, 'phone')
    phone_input.send_keys('1234567890') 


    # Проверка значений
    assert len(name_input.get_attribute('value')) >= 1, "Некорректное имя"
    assert len(last_name_input.get_attribute('value')) >= 1, "Некорректная фамилия"
    assert '@' in email_input.get_attribute('value'), "Некорректный email"
    assert phone_input.get_attribute('value') == '+7' + '1234567890', "Некорректный номер телефона"

finally:
    driver.quit()
