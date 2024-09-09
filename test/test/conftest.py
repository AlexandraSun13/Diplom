import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import configparser


url_1 = 'https://web-gate.chitai-gorod.ru/api/v1'
url_2 = 'https://web-gate.chitai-gorod.ru/api/v2'
token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjYwNTA0NzUsImlhdCI6MTcyNTg4MjQ3NSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjE2N2QyMjQ5YjBhZGJmMmJkYWI4ZmMyNjZmZDM0ZWMxOWE1ODIwMTc0MDViNzJmOTFmZTU4MWUzYTI1YTgwY2YiLCJ0eXBlIjoxMH0.BRw1Ns3AnHpU0AwmvRcoB4BjGEyqMTxOgaw1v3tcyJw'
HEADRS = {
  'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjYwNTA0NzUsImlhdCI6MTcyNTg4MjQ3NSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjE2N2QyMjQ5YjBhZGJmMmJkYWI4ZmMyNjZmZDM0ZWMxOWE1ODIwMTc0MDViNzJmOTFmZTU4MWUzYTI1YTgwY2YiLCJ0eXBlIjoxMH0.BRw1Ns3AnHpU0AwmvRcoB4BjGEyqMTxOgaw1v3tcyJw',
  'Cookie': '__ddg1_=h83ZuzjeFslq59sCFBU5'
}


@pytest.fixture
def browser():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.implicitly_wait(3)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def config():
    config = configparser.ConfigParser()
    config.read("confi.ini")
    return config
