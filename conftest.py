from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    yield driver
    driver.quit()