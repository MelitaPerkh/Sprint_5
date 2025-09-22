from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
import string
from locators import Locators

class TestLogin: 
    
    def test_login(self, driver):
        
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("123@example.com")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123")
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.EXIT_BUTTON)))
        assert driver.find_element(*Locators.TEXT_USER).text == "User."

        


    def test_logout(self, driver):
     
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("123@example.com")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123")
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.EXIT_BUTTON)))
        driver.find_element(Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.REGISTER_BUTTON)))
        assert not driver.find_element(*Locators.TEXT_USER).text == "User." and expected_conditions.visibility_of_element_located((Locators.REGISTER_BUTTON))


      