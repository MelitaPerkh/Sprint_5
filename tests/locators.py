from selenium.webdriver.common.by import By

class Locators:
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
    NO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")
    EMAIL_INPUT = (By.NAME,"email")
    PASSWORD_INPUT = (By.NAME,"password")
    PASSWORD_CONFIRM_INPUT = (By.NAME,"submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
    TEXT_USER = (By.XPATH, ".//h3")
    PIC_AVATAR = (By.XPATH, ".//svg")

    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    INVALID_MESSAGE = (By.XPATH, ".//span[@class='input_span__yWPqB']")

    BORDER_EMAIL = (By.XPATH,".//input[@name='email']/parent::div")
    BORDER_PASSWORD = (By.XPATH,".//input[@name='password']/parent::div")
    BORDER_PASWORD_CONFIRM = (By.XPATH,".//input[@name='submitPassword']/parent::div")

    ADVERT_BUTTON = (By.XPATH, ".//button[text()='Разместить объявление']")
    TEXT_ADVERT = (By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']")

    ADVERT_NAME = (By.NAME, "name")
    ADVERT_DESCR = (By.XPATH, ".//textarea[@name='description']")
    ADVERT_PRICE = (By.XPATH, ".//input[@name='price']")
    ADVERT_PRINT = (By.XPATH, ".//button[text()='Опубликовать']")

    ADVERT = (By.XPATH, ".//h2[@class='h2']")