from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base_pages.base_page import BasePage
from utilities.read_properties import ReadConfig


class CheckoutPage(BasePage):
    ADDRESS_DETAILS_TEXT = (By.XPATH, '//*[@id="cart_items"]/div/div[2]/h2')
    DELIVERY_ADDRESS = (By.ID, 'address_delivery')
    BILLING_ADDRESS = (By.ID, 'address_invoice')

    REVIEW_YOUR_ORDER = (By.XPATH, '//*[@id="cart_items"]/div/div[4]/h2')
    COMMENT_TEXT_AREA = (By.XPATH, '//*[@id="ordermsg"]/textarea')
    PLACE_ORDER = (By.XPATH, '//*[@id="cart_items"]/div/div[7]/a')
    DELETE_ACCOUNT = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')


    TIMEOUT = ReadConfig.get_timeout_value()

    def verify_address(self, address):
        delivery_address = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.DELIVERY_ADDRESS))

        # Extract data from individual list items
        address_data = [
            "\n".join([
                li.text for li in delivery_address.find_elements(By.CLASS_NAME, "address_address1")
            ]),  # Address
            delivery_address.find_element(By.CLASS_NAME, "address_country_name").text,  # Country
            delivery_address.find_element(By.CLASS_NAME, "address_phone").text,  # Phone
            delivery_address.find_element(By.CLASS_NAME, "address_city").text,  # City_State_Postcode
        ]

        return True if address_data == address else False


    def verify_billing_address(self, address):
        billing_address = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.BILLING_ADDRESS))

        # Extract data from individual list items
        address_data = [
            "\n".join([
                li.text for li in billing_address.find_elements(By.CLASS_NAME, "address_address1")
            ]),  # Address
            billing_address.find_element(By.CLASS_NAME, "address_country_name").text,  # Country
            billing_address.find_element(By.CLASS_NAME, "address_phone").text,  # Phone
            billing_address.find_element(By.CLASS_NAME, "address_city").text,  # City_State_Postcode
        ]

        return True if address_data == address else False


    def review_your_order(self):
        review = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.REVIEW_YOUR_ORDER))

        return review.is_displayed()

    def enter_description_in_comment_text_area(self, description):
        text_area = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.COMMENT_TEXT_AREA))

        text_area.clear()
        text_area.send_keys(description)

        return self

    def click_place_order_button(self):
        place_order_button = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.PLACE_ORDER))
        place_order_button.click()
        time.sleep(1)
        return self

    def enter_description_and_click_place_order(self, description):
        self.enter_description_in_comment_text_area(description)
        time.sleep(2)
        self.click_place_order_button()

        return self

    def click_delete_account_button(self):
        self.driver.find_element(*self.DELETE_ACCOUNT).click()
        time.sleep(3)
        return self




