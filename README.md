# Diplom
Дипломная работа
## Шаги

1. Склонировать проект 'git clone https://github.com/VailaAs/chitai-gorod_project.git'
2. Установить все зависимости из requirements.txt
3. Скопировать access-token по инструкции ниже.
3. Запустить тесты 'pytest -s -v --alluredir=allure-result' ИЛИ 'python -m pytest -s -v --alluredir=allure-result'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report' ИЛИ 'allure serve allure-result '
5. Открыть отчет 'allure open allure-report'

### Библиотеки (**!**)

- pip install pytest
- pip install selenium
- pip install requests
- pip install allure-pytest
- pip install webdriver-manager
- pip install configparser

## Инструкция по использованию token в проекте

token - основная перменная проекта. Она хранится в файле confi.ini, корневая директория.

### Шаги присвоения access-token

1. Перейти на [сайт](https://www.chitai-gorod.ru/).
2. Авторизироваться.
3. Открыть Панель разработчика.
4. Перейти на вкладку Applicatio и выбрать Cookies.
5. Перезагрузить главную страницу с открытой панелью.
6. Ищем access-token. 
7. Скопировать её значение. 
8. Открыть файл conf.ini и вставить скопированные данные в переменную access-token без кавычек.
 *Ключ протухает, поэтому иногда нужно менять значение в переменной (примерно каждый час). 