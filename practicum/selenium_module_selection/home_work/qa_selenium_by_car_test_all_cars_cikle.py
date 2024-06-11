import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get('https://erikdark.github.io/Qa_autotests_17/')

    cars = [
    {'selector':'#price1', 'price':'550', 'button_id':'buyButton1', 'message_id':'message1'},
    {'selector':'#price2', 'price':'800', 'button_id':'buyButton2', 'message_id':'message2'},
    {'selector':'#price3', 'price':'19000', 'button_id':'buyButton3', 'message_id':'message3'}
]

    for car in cars:
        element = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, car['selector']), car['price']))
        
        buy_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, car['button_id'])))
        buy_button.click()
        
        message = driver.find_element(By.ID, car['message_id'])
        assert 'Вы успешно купили автомобиль!' in message.text
        print('Машина: Все ОК!')

finally:
    time.sleep(3)
    driver.quit()
