import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

cookie = {"name": "receive-cookie-deprecation", "value": "1"}

# Найти все книги по названию

def test_search_content_by_title():
    try:
# Инициализация браузера
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get('https://www.chitai-gorod.ru/')  # Необходимо перейти на сайт перед поиском
        browser.implicitly_wait(4)
        browser.add_cookie(cookie)
# Поиск по запросу
        search_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[class="header-search__input"]')))
        search_input.send_keys('Вино из одуванчиков')
        search_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="header-search__button"]'))).click()
# Ожидание загрузки результатов поиска
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[class="product-card"]')))

# Сбор всех названий книг
        books = browser.find_elements(By.CSS_SELECTOR, '[class="product-card__title"]')
        print("Найденные книги:")
        for book in books:
            print(book.text)

    assert

    except TimeoutException as e:
        print(f"Error in test_api: {e}")
    finally:
        browser.quit()
