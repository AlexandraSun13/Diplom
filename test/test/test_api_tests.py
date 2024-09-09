import requests
import json
import allure
from conftest import url_1, url_2, token, HEADRS


# Поиск книги по фамилии автора
def test_api():
    base_url = url_2
    headers = {'authorization': token}
    response = requests.get(base_url + '/search/product?customerCityId=213&phrase=%D1%80%D0%B5%D0%BC%D0%B0%D1%80%D0%BA&products%5Bpage%5D=1&products%5Bper-page%5D=48&sortPreset=relevance', headers=headers)
    assert response.status_code == 200
    print(response.status_code, response.text)


# Добавление товара в корзину
def product_in_card():
    url = url_1
    payload = json.dumps({
        "id": 2839320,
        "adData": {'item_list_name': "search", 'product_shelf': ""}}
    )
    headers = {
        'authorization': token,
        'Content-Type': 'application/json',
        'Cookie': '__ddg1_=h83ZuzjeFslq59sCFBU5'
    }
    response = requests.post(
        url+'/cart/product', headers=headers, data=payload)
    assert response.status_code == 200
    print(response.status_code, response.text)


# Поиск книги по названию (невалидный)

@allure.title("Поиск книги по названию (Негативный)")
@allure.description("Выполнение теста на поиск книги с вводом эмоджи")
def test_search_content():
    with allure.step("Указываем GET запроса с вводом эмоджи в строке Поиск"):
        response = requests.get(f"{url_1}/recommend/semantic?phrase=%F0%9F%90%87&perPage=48", headers=HEADRS)
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200


# Найти книгу по ID

def test_search_book_ID():
    base_URL = url_1
    headers = {'authorization': token}
    response = requests.get(
        base_URL + '/products/slug/master-i-margarita-3018590',
        headers=headers)
    assert response.status_code == 200


# Получить список категорий

def test_list_category():
    base_URL = url_2
    headers = {'authorization': token}
    response = requests.get(base_URL + '/categories', headers=headers)
    assert response.status_code == 200
