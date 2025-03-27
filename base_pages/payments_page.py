from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base_pages.base_page import BasePage
from utilities.read_properties import ReadConfig


class PaymentsPage(BasePage):
    PAYMENT_TEXT = (By.XPATH, '//*[@id="cart_items"]/div/div[2]/h2')
    PAY_AND_CONFIRM_BUTTON = (By.ID, 'submit')
    NAME_ON_CARD_INPUT = (By.XPATH, '//*[@id="payment-form"]/div[1]/div/input')
    CARD_NUMBER_INPUT = (By.XPATH, '//*[@id="payment-form"]/div[2]/div/input')
    CVC_INPUT = (By.XPATH, '//*[@id="payment-form"]/div[3]/div[1]/input')
    EXPIRATION_MM_INPUT = (By.XPATH, '//*[@id="payment-form"]/div[3]/div[2]/input')
    EXPIRATION_YYYY_INPUT = (By.XPATH, '//*[@id="payment-form"]/div[3]/div[3]/input')


    TIMEOUT = ReadConfig.get_timeout_value()

    def payment_text_is_visible(self):
        payment_txt = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.PAYMENT_TEXT))

        return payment_txt.is_displayed()

    def click_pay_and_confirm_order_button(self):
        pay_button = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.PAY_AND_CONFIRM_BUTTON))

        pay_button.click()
        time.sleep(1)
        return self


    def enter_name(self, name):
        textbox = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.NAME_ON_CARD_INPUT))
        textbox.clear()
        textbox.send_keys(name)
        return self

    def enter_card_number(self, card_number):
        textbox = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.CARD_NUMBER_INPUT))
        textbox.clear()
        textbox.send_keys(card_number)
        return self

    def enter_cvc(self, cvc):
        textbox = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.CVC_INPUT))
        textbox.clear()
        textbox.send_keys(cvc)
        return self

    def enter_expiration_date(self, month, year):
        month_txt = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.EXPIRATION_MM_INPUT))
        month_txt.clear()
        month_txt.send_keys(month)

        year_txt = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.EXPIRATION_YYYY_INPUT))
        year_txt.clear()
        year_txt.send_keys(year)

        return self

    def enter_payments_details(self, name, card_number, cvc, expiration_month, expiration_year):
        self.enter_name(name)
        self.enter_card_number(card_number)
        self.enter_cvc(cvc)
        self.enter_expiration_date(expiration_month, expiration_year)

        return self

    def enter_payment_details_and_click_pay_button(self, name, card_number, cvc, expiration_month, expiration_year):
        self.enter_payments_details(name, card_number, cvc, expiration_month, expiration_year)
        time.sleep(2)
        self.click_pay_and_confirm_order_button()