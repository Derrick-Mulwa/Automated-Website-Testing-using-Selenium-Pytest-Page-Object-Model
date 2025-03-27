from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from base_pages.base_page import BasePage
from utilities.read_properties import ReadConfig
import time


class ContactUsPage(BasePage):
    GET_IN_TOUCH = (By.XPATH, '//*[@id="contact-page"]/div[2]/div[1]/div/h2')
    NAME_INPUT = (By.XPATH, '//*[@id="contact-us-form"]/div[1]/input')
    EMAIL_INPUT = (By.XPATH, '//*[@id="contact-us-form"]/div[2]/input')
    SUBJECT_INPUT = (By.XPATH, '//*[@id="contact-us-form"]/div[3]/input')
    MESSAGE_INPUT = (By.ID, 'message')
    UPLOAD_FILE_INPUT = (By.XPATH, '//*[@id="contact-us-form"]/div[5]/input')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="contact-us-form"]/div[6]/input')
    SUCCESS_YOUR_DETAILS = (By.XPATH, '//*[@id="contact-page"]/div[2]/div[1]/div/div[2]')
    HOME_BUTTON = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[1]/a')

    TIMEOUT = ReadConfig.get_timeout_value()

    def get_in_touch_is_visible(self):
        get_in_touch = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.GET_IN_TOUCH))

        return get_in_touch.is_displayed()


    def enter_name(self, name):
        self.driver.find_element(*self.NAME_INPUT).clear()
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        return self

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        return self

    def enter_subject(self, subject):
        self.driver.find_element(*self.SUBJECT_INPUT).clear()
        self.driver.find_element(*self.SUBJECT_INPUT).send_keys(subject)
        return self

    def enter_message(self, message):
        self.driver.find_element(*self.MESSAGE_INPUT).clear()
        self.driver.find_element(*self.MESSAGE_INPUT).send_keys(message)
        return self

    def upload_file(self, filepath):
        file_input = self.driver.find_element(*self.UPLOAD_FILE_INPUT)
        file_input.send_keys(filepath)
        return self

    def click_submit_button(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(2)
        return self

    def click_ok_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        return self

    def success_your_details_submitted_is_visible(self):
        success_your_details = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.SUCCESS_YOUR_DETAILS))

        return success_your_details.is_displayed()

    def click_home_button(self):
        self.driver.find_element(*self.HOME_BUTTON).click()
        time.sleep(2)
        return self




