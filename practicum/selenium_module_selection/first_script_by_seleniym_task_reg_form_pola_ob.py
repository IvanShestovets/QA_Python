import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#иницилизирую драйвер браузера
driver = webdriver.Chrome()

# через get мы говорим браузеру что обращаемся к странице
try:
    driver.get('https://erikdark.github.io/Qa_autotest_03/')
    
    input_one = driver.find_element(By.ID,'firstName')
    input_one.send_keys('Ivan')

    input_two = driver.find_element(By.ID,'lastName')
    input_two.send_keys('Sheff')

    input_tree = driver.find_element(By.ID,'email')
    input_tree.send_keys('Kartman@fde.rr')



    # input_two = driver.find_element(By.ID,'phone')
    # input_two.send_keys('Sheff')

    # input_tree = driver.find_element(By.ID,'address')
    # input_tree.send_keys('Kartmande.rr')



    btn = driver.find_element(By.CSS_SELECTOR, 'button')
    btn.click()
    time.sleep(3)

    cong = driver.find_element(By.TAG_NAME, 'h2')
    cong_text = cong.text
    expected_text = "Поздравляю, вы прошли первый уровень."

    assert expected_text == cong_text

    print("Текст совпадает!")

finally:
    driver.quit()
