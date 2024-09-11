import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import configparser


url = 'https://www.chitai-gorod.ru/'
url_1 = 'https://web-gate.chitai-gorod.ru/api/v1'
url_2 = 'https://web-gate.chitai-gorod.ru/api/v2'
token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjYyMzMxMjgsImlhdCI6MTcyNjA2NTEyOCwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImRiMDY1MzJjNmZlYmYyN2Q1NWY3N2NmNWQ2ZWYwMDE1NWFiNTdlNjdiNDhhNzdlYzhmZWZiOWIyOGM5ZGY5NmIiLCJ0eXBlIjoxMH0.18aVikDAihHkfXcSsfAOwRY4WjXVS-lWGr-N6gAQBK4'
HEADRS = {
  'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjYyMzMxMjgsImlhdCI6MTcyNjA2NTEyOCwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImRiMDY1MzJjNmZlYmYyN2Q1NWY3N2NmNWQ2ZWYwMDE1NWFiNTdlNjdiNDhhNzdlYzhmZWZiOWIyOGM5ZGY5NmIiLCJ0eXBlIjoxMH0.18aVikDAihHkfXcSsfAOwRY4WjXVS-lWGr-N6gAQBK4',
  'Cookie': '__ddg1_=h83ZuzjeFslq59sCFBU5'
}


@pytest.fixture
def browser():
    browser = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    browser.implicitly_wait(3)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def config():
    config = configparser.ConfigParser()
    config.read("confi.ini")
    return config
