from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
import string
import pytest
from locators import Locators
from helpers import generate_random_email
class TestAutorization:
             
    def test_user_registration(self, driver):

        
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_random_email())
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("Perkhurova_22")
        driver.find_element(*Locators.PASSWORD_CONFIRM_INPUT).send_keys("Perkhurova_22")
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.EXIT_BUTTON)))
        assert driver.find_element(*Locators.TEXT_USER).text == "User." and expected_conditions.visibility_of_element_located((Locators.PIC_AVATAR))


    def test_registration_user_invalid_email(self, driver):
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("Invalid e-mail")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("Perkhurova_22")
        driver.find_element(*Locators.PASSWORD_CONFIRM_INPUT).send_keys("Perkhurova_22")
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((Locators.INVALID_MESSAGE)))
        assert driver.find_element(*Locators.INVALID_MESSAGE).text == "Ошибка" and driver.find_element(*Locators.BORDER_EMAIL).value_of_css_property("border-color")  == "rgb(255, 105, 114)" and driver.find_element(*Locators.BORDER_PASSWORD).value_of_css_property("border-color")  == "rgb(255, 105, 114)" and driver.find_element(*Locators.BORDER_PASWORD_CONFIRM).value_of_css_property("border-color")  == "rgb(255, 105, 114)"

    def test_registration_user_exist(self, driver):

        email = self.generate_random_email()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("Perkhurova_22")
        driver.find_element(*Locators.PASSWORD_CONFIRM_INPUT).send_keys("Perkhurova_22")
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.EXIT_BUTTON)))
        driver.find_element(*Locators.EXIT_BUTTON).click()

        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("Perkhurova_22")
        driver.find_element(*Locators.PASSWORD_CONFIRM_INPUT).send_keys("Perkhurova_22")
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((Locators.INVALID_MESSAGE)))
        assert driver.find_element(*Locators.INVALID_MESSAGE).text == "Ошибка" and driver.find_element(*Locators.BORDER_EMAIL).value_of_css_property("border-color")  == "rgb(255, 105, 114)" and driver.find_element(*Locators.BORDER_PASSWORD).value_of_css_property("border-color")  == "rgb(255, 105, 114)" and driver.find_element(*Locators.BORDER_PASWORD_CONFIRM).value_of_css_property("border-color")  == "rgb(255, 105, 114)"   