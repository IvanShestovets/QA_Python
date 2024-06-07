
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def test_exection1():
    try:
        driver = webdriver.Chrome()
        driver.get('https://erikdark.github.io/PyTest_01_reg_form/')
        
        driver.find_element(By.ID,'username').send_keys('Ivan')
        driver.find_element(By.ID,'email').send_keys('Kartman@fde.rr')
        driver.find_element(By.ID,'password').send_keys('qwerty')
        driver.find_element(By.CSS_SELECTOR, 'button').click()    

        text = driver.find_element(By.ID,'success-message').text
        assert 'Вы успешно зарегистрированы!' == text
        print("Текст совпадает!")

    finally:
        time.sleep(3)
        driver.quit()


def test_exection2():
    try:
        driver = webdriver.Chrome()
        driver.get('https://erikdark.github.io/PyTest_01_reg_form/')

        driver.find_element(By.ID,'username').send_keys('Ivan')
        driver.find_element(By.ID,'email').send_keys('Kartman')
        driver.find_element(By.ID,'password').send_keys('qwerty')
        driver.find_element(By.CSS_SELECTOR, 'button').click()

        text = driver.find_element(By.ID,'success-message').text
        assert 'Вы успешно зарегистрированы!' == text
        print("Текст совпадает!")
  
    finally:
        time.sleep(3)
        driver.quit() 
