import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(1)
    driver.quit()


# Найти все записи с именем Иван
def test_sql_1(browser):
    browser.get('https://erikdark.github.io/QA_DIPLOM/')
    browser.find_element(By.XPATH, "//a[contains(@href, 'database.html')]").click()

    sql_input = browser.find_element(By.ID, 'sqlQuery')
    sql_input.send_keys("SELECT * FROM TABLE WHERE NAME = 'Иван'")

    submit_button = browser.find_element(By.ID, "executeButton")
    submit_button.click()

    text = browser.find_element(By.ID,'sqlMessage').text
    assert 'Найдено 1 записей.' == text


# С помощью команды ORDER BY выполнить сортировку по возрасту и убедится что она успешно прошла
def test_sql_2(browser):
    browser.get('https://erikdark.github.io/QA_DIPLOM/')
    browser.find_element(By.XPATH, "//a[contains(@href, 'database.html')]").click()
    
    sql_input = browser.find_element(By.ID, 'sqlQuery')
    sql_input.send_keys("ORDER BY age")
    submit_button = browser.find_element(By.ID, "executeButton")
    submit_button.click()

    age_cells = browser.find_elements(By.XPATH, "//table[@id='dataTable']/tbody/tr/td[3]")
    ages = [int(cell.text) for cell in age_cells]
    assert ages == sorted(ages)


# Удалить запись с id 1 и убедится что она действительно удалена
def test_sql_3(browser):
    browser.get('https://erikdark.github.io/QA_DIPLOM/')
    browser.find_element(By.XPATH, "//a[contains(@href, 'database.html')]").click()
    sql_input = browser.find_element(By.ID, 'sqlQuery')
    sql_input.send_keys("DELETE FROM TABLE WHERE ID = 1")
    submit_button = browser.find_element(By.ID, "executeButton")
    submit_button.click()    

    table_rows = browser.find_elements(By.CSS_SELECTOR, '#dataTable tbody tr')

    id_1_found = False
    for row in table_rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if cells[0].text == '1':
            id_1_found = True
            break

    assert not id_1_found, "Запись с id 1 присутствует в таблице"
