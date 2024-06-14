import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Функция для получения данных из таблицы
def get_table_data(driver, table_id):
    table = driver.find_element(By.ID, table_id)
    return [[cell.text for cell in row.find_elements(By.TAG_NAME, "td")] for row in table.find_elements(By.TAG_NAME, "tr")]

# Функция для проверки сортировки
def check_sorting(driver, table_id, column_index, expected_message):
    driver.find_element(By.CSS_SELECTOR, f"#{table_id} th:nth-child({column_index + 1})").click()
    sorted_data = get_table_data(driver, table_id)
    # Здесь должна быть логика проверки корректности сортировки
    sort_message = driver.find_element(By.ID, "sort-message").text
    assert sort_message == expected_message

# Тест с использованием Pytest
def test_sorting():
    browser = webdriver.Chrome()
    browser.get("https://erikdark.github.io/zachet_selenium_01/")

    table_link = browser.find_element(By.CSS_SELECTOR,"[href='table.html']")
    table_link.click()

    original_data = get_table_data(browser, "data-table")
    # Проверка сортировки для каждой колонки
    for index in range(3):
        check_sorting(browser, "data-table", index, f"Таблица отсортирована по столбцу {index + 1}")
    browser.quit()

if __name__ == "__main__":
    pytest.main()

