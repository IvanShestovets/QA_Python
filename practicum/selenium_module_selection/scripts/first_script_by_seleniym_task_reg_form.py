import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#иницилизирую драйвер браузера
driver = webdriver.Chrome()

# через get мы говорим браузеру что обращаемся к странице
try:
    driver.get('https://erikdark.github.io/Qa_autotest_03/')
    data = ['Ivan','Sheff','erik@mail.ru','tell','SPb']

    inputs = driver.find_elements(By.TAG_NAME,'input')
    for i in range(len(inputs)):
        inputs[i].send_keys(data[i])
    time.sleep(3)
    btn = driver.find_element(By.CSS_SELECTOR, 'button')
    btn.click()
    time.sleep(3)

    cong = driver.find_element(By.TAG_NAME, 'h2')
    cong_text = cong.text
    expected_text = "Поздравляю, вы прошли первый уровень."

    assert expected_text == cong_text, f"Текст на странице: '{cong_text}', ожидался текст: '{expected_text}'"

    print("Текст совпадает!")

finally:
    driver.quit()
