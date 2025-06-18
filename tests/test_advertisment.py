from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from locators import Locators
import random
import string

class TestAdvertisment:
     def generate_random_email(self):
        letters = string.ascii_lowercase
        rand_email = ''.join(random.sample(letters, 9))+"@example.com"
        return rand_email


     def test_unautor_advertisment(self,driver):
        driver.find_element(*Locators.ADVERT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.TEXT_ADVERT)))
        assert expected_conditions.visibility_of_element_located((Locators.TEXT_ADVERT))


     def test_autor_advertisment(self,driver):        
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(self.generate_random_email())
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("Perkhurova_22")
        driver.find_element(*Locators.PASSWORD_CONFIRM_INPUT).send_keys("Perkhurova_22")
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.EXIT_BUTTON)))
        driver.find_element(*Locators.ADVERT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "name")))
        driver.find_element(By.NAME, "name").send_keys("Продам стол")
        driver.find_element(*Locators.ADVERT_DESCR).send_keys("Очень красивый")
        driver.find_element(*Locators.ADVERT_PRICE).send_keys(99)
        driver.find_element(*Locators.ADVERT_PRINT).click()

        driver.get('https://qa-desk.stand.praktikum-services.ru/profile')
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_all_elements_located)

        assert driver.find_element(*Locators.ADVERT)
