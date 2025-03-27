from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from base_pages.base_page import BasePage
from utilities.read_properties import ReadConfig


import time


class LoginPage(BasePage):
    NEW_USER_SIGNUP = (By.XPATH, '//*[@id="form"]/div/div/div[3]/div/h2')
    LOGIN_TO_YOUR_ACCOUNT = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/h2')
    SIGNUP_NAME_INPUT = (By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]')
    SIGNUP_EMAIL_INPUT = (By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]')
    SIGNUP_BUTTON = (By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button')
    LOGIN_EMAIL = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]')
    LOGIN_PASSWORD = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[3]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/button')
    YOUR_EMAIL_OR_PASS_IS_INCORRECT = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/p')
    EMAIL_ADDRESS_ALREADY_EXISTS = (By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/p')

    TIMEOUT = ReadConfig.get_timeout_value()



    def new_user_signup_is_visible(self):
        new_user_signup = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.NEW_USER_SIGNUP))

        return new_user_signup.is_displayed()

    def your_email_or_password_is_incorrect_is_visible(self):
        your_email = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.YOUR_EMAIL_OR_PASS_IS_INCORRECT))

        return your_email.is_displayed()


    def log_in_to_your_account_is_visible(self):
        login_to_acc = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.LOGIN_TO_YOUR_ACCOUNT))

        return login_to_acc.is_displayed()


    def enter_signup_details(self, name, email):
        self.driver.find_element(*self.SIGNUP_NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.SIGNUP_EMAIL_INPUT).send_keys(email)
        return self

    def enter_login_details(self, email, password):
        self.driver.find_element(*self.LOGIN_EMAIL).send_keys(email)
        self.driver.find_element(*self.LOGIN_PASSWORD).send_keys(password)

        return self

    def click_signup_button(self):
        self.driver.find_element(*self.SIGNUP_BUTTON).click()
        time.sleep(2)
        return self

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(2)
        return self

    def email_address_already_exists_is_visible(self):
        email_exists = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.EMAIL_ADDRESS_ALREADY_EXISTS))

        return email_exists.is_displayed()




