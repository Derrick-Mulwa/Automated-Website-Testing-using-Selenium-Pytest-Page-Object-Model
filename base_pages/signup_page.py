from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from base_pages.base_page import BasePage
import time


class SignupPage(BasePage):
    ENTER_ACCOUNT_INFORMATION = (By.XPATH, '//*[@id="form"]/div/div/div/div[1]/h2/b')
    TITLE_MR_RBTN = (By.XPATH, '//*[@id="form"]/div/div/div/div[1]/form/div[1]/div[1]/label')
    TITLE_MRS_RBTN = (By.XPATH, '//*[@id="form"]/div/div/div/div/form/div[1]/div[2]/label')

    NAME = (By.XPATH, '//*[@id="name"]')
    EMAIL = (By.XPATH, '//*[@id="email"]')
    PASSWORD = (By.ID, 'password')

    DOB_DATE = (By.XPATH, '//*[@id="days"]')
    DOB_MONTH = (By.XPATH, '//*[@id="months"]')
    DOB_YEAR = (By.XPATH, '//*[@id="years"]')
    SIGN_UP_FOR_NEWSLETTER = (By.ID, 'newsletter')
    RECEIVE_SPECIAL_OFFERS = (By.ID, 'optin')
    ADDRESS_INFORMATION_ = (By.XPATH, '//*[@id="form"]/div/div/div/div[1]/form/h2/b')
    FIRST_NAME = (By.ID, 'first_name')
    LAST_NAME = (By.ID, 'last_name')
    COMPANY = (By.ID, 'company')
    ADDRESS = (By.ID, 'address1')
    ADDRESS_2 = (By.ID, 'address2')
    COUNTRY = (By.ID, 'country')
    STATE = (By.ID, 'state')
    CITY = (By.ID, 'city')
    ZIPCODE = (By.ID, 'zipcode')
    MOBILE_NUMBER = (By.ID, 'mobile_number')
    CREATE_ACCOUNT = (By.XPATH, '//*[@id="form"]/div/div/div/div[1]/form/button')

    def enter_account_information_is_visible(self):
        enter_account_information = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.ENTER_ACCOUNT_INFORMATION))

        return enter_account_information.is_displayed()


    def select_title(self, gender):
        if gender.lower() == 'male':
            self.driver.find_element(*self.TITLE_MR_RBTN).click()
        else:
            self.driver.find_element(*self.TITLE_MRS_RBTN).click()

        return self

    def enter_name(self, name):
        self.driver.find_element(*self.NAME).clear()
        self.driver.find_element(*self.NAME).send_keys(name)
        return self

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        return self

    def enter_date_of_birth(self, dob_day, dob_month, dob_year):
        month_mapping = {
            "January": 1, "February": 2, "March": 3, "April": 4,
            "May": 5, "June": 6, "July": 7, "August": 8,
            "September": 9, "October": 10, "November": 11, "December": 12,
            "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "Jun": 6, "Jul": 7, "Aug": 8,
            "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
        }

        day = self.driver.find_element(*self.DOB_DATE)
        month = self.driver.find_element(*self.DOB_MONTH)
        year = self.driver.find_element(*self.DOB_YEAR)

        Select(day).select_by_index(dob_day)
        Select(month).select_by_value(str(month_mapping.get(dob_month)))
        Select(year).select_by_value(dob_year)

        return self

    def check_checkbox_sign_up_for_our_newsletter(self):
        if not self.driver.find_element(*self.SIGN_UP_FOR_NEWSLETTER).is_selected():
            self.driver.find_element(*self.SIGN_UP_FOR_NEWSLETTER).click()
            return self

    def uncheck_checkbox_sign_up_for_our_newsletter(self):
        if self.driver.find_element(*self.SIGN_UP_FOR_NEWSLETTER).is_selected():
            self.driver.find_element(*self.SIGN_UP_FOR_NEWSLETTER).click()
            return self

    def check_checkbox_receive_special_offers(self):
        if not self.driver.find_element(*self.RECEIVE_SPECIAL_OFFERS).is_selected():
            self.driver.find_element(*self.RECEIVE_SPECIAL_OFFERS).click()
            return self

    def uncheck_checkbox_receive_special_offers(self):
        if self.driver.find_element(*self.RECEIVE_SPECIAL_OFFERS).is_selected():
            self.driver.find_element(*self.RECEIVE_SPECIAL_OFFERS).click()
            return self

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        return self

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        return self

    def enter_company(self, company):
        self.driver.find_element(*self.COMPANY).send_keys(company)
        return self

    def enter_address(self, address):
        self.driver.find_element(*self.ADDRESS).send_keys(address)
        return self

    def enter_address2(self, address2):
        self.driver.find_element(*self.ADDRESS_2).send_keys(address2)
        return self

    def enter_country(self, user_country):
        country = self.driver.find_element(*self.COUNTRY)

        Select(country).select_by_value(user_country)

        return self

    def enter_state(self, state):
        self.driver.find_element(*self.STATE).send_keys(state)
        return self

    def enter_city(self, city):
        self.driver.find_element(*self.CITY).send_keys(city)
        return self

    def enter_zipcode(self, zipcode):
        self.driver.find_element(*self.ZIPCODE).send_keys(zipcode)
        return self

    def enter_mobile_number(self, number):
        self.driver.find_element(*self.MOBILE_NUMBER).send_keys(number)
        return self

    def enter_all_user_data(self, user_data):
        # Select title (you can choose the appropriate title based on user_data)
        if user_data['gender'].lower() == 'male':
            self.select_male_title()
        else:
            self.select_female_title()

        # Enter name
        self.enter_name(user_data['name'])

        # Enter password
        self.enter_password(user_data['password'])

        # Enter date of birth
        self.enter_date_of_birth(user_data['dob_day'], user_data['dob_month'], user_data['dob_year'])

        # Subscribe to newsletter and special offers
        self.check_checkbox_sign_up_for_our_newsletter()
        self.check_checkbox_receive_special_offers()

        # Enter address details
        self.enter_first_name(user_data['first_name'])
        self.enter_last_name(user_data['last_name'])
        self.enter_company(user_data['company'])
        self.enter_address(user_data['address1'])
        self.enter_address2(user_data['address2'])
        self.enter_country(user_data['country'])
        self.enter_state(user_data['state'])
        self.enter_city(user_data['city'])
        self.enter_zipcode(user_data['zipcode'])
        self.enter_mobile_number(user_data['mobile_number'])

        return self

    def click_create_account_button(self):
        self.driver.find_element(*self.CREATE_ACCOUNT).click()
        time.sleep(4)
        return self