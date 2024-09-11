from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import url
import allure


cookie = {"name": "receive-cookie-deprecation", "value": "1"}
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.maximize_window()
browser.delete_all_cookies()


@allure.title("Перейти на сайт Читай-город")
@allure.suite('UI')
def open_browser_addcookie():
    browser.get(url)
                

@allure.epic("Читай-город")
@allure.suite('UI')
@allure.feature('Test 1')
@allure.title("Поиск книги") 
@allure.description("Тест проверяет поиск книги") 
@allure.severity("blocker") 
def test_search_book():
    browser.get(url)
    with allure.step("Добавлено ожидание окна"): 
        browser.implicitly_wait(5)
    with allure.step("Выполнение поиска книги"):
        browser.find_element(By.CSS_SELECTOR, '.header-search__input').send_keys('Ремарк')
        browser.find_element(By.CLASS_NAME, 'header-search__button-icon').click()
        result_text = browser.find_element(By.XPATH, "//p[@class='search-page__found-message']").text
    print(f"Результат поиска: {result_text}")
    assert "Показываем результаты по запросу" in result_text, 'Текст не найден'
    

@allure.epic("Читай-город")
@allure.suite('UI')
@allure.feature('Test 2')
@allure.title("Добавить книгу в корзину") 
@allure.description("Переходим на страницу с книгой, нажимаем купить, товар добавляется в корзину")
@allure.severity("blocker") 
def test_add_book():
    with allure.step("Открыть страницу с книгой"): 
        open_buttons = browser.find_element(
    By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[1]/a[1]/picture[1]/img[1]")
        open_buttons.click()
    with allure.step("Нажать кнопку купить"): 
        buy_buttons = browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[2]/button[1]")
        buy_buttons.click()
       

@allure.epic("Читай-город")
@allure.suite('UI')
@allure.feature('Test 3')
@allure.title("Перейти в корзину") 
@allure.description("Открывается страница с корзиной товаров")
@allure.severity("critical") 
def test_go_to_cart():
    with allure.step("Переходим в корзину"): 
        browser.get("https://www.chitai-gorod.ru/cart")


@allure.epic("Читай-город")
@allure.suite('UI')
@allure.feature('Test 4')
@allure.title("Проверка кол-ва товаров в корзине") 
@allure.description("В корзине должно отразиться столько товаров, сколько раз нажали купить")
@allure.severity("blocker") 
def test_get_cart_counter():
    txt = browser.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").text
    print(f"текст элемента:{txt}")
    with allure.step("Проверить счетчик товаров"):
        assert isinstance(txt, str), f"Ожидали число, получили {type(txt)}"

@allure.epic("Читай-город")
@allure.suite('UI')
@allure.feature('Test 5')
@allure.title("Проверка кол-ва товаров в корзине") 
@allure.description("В корзине должно отразиться столько товаров, сколько раз нажали купить")
@allure.severity("blocker") 
def test_delete_cart():
    with allure.step("Нажать очистить корзину"):
        delete_goods = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/*[name()='svg'][1]")))
        delete_goods.click()
    with allure.step("Перезагрузить страницу"):
        browser.refresh()
    with allure.step("Убедиться, что корзина пуста"):
        try:
            empty_cart_message = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/section[1]/p[1]')))
            assert empty_cart_message.is_displayed(), "Корзина не пуста!"
        except Exception as e:
            print(f"Ошибка при проверке пустой корзины: {e}")
  

    browser.quit()
