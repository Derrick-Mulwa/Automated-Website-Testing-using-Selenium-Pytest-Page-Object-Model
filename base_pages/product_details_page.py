from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base_pages.base_page import BasePage
from utilities.read_properties import ReadConfig


class ProductDetailsPage(BasePage):
    PRODUCT_DETAILS = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]')
    QUANTITY_INPUT = (By.ID, 'quantity')
    ADD_TO_CART_BUTTON = (By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button')
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, '//*[@id="cartModal"]/div/div/div[3]/button')
    VIEW_CART_BUTTON = (By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a')
    WRITE_YOUR_REVIEW = (By.XPATH, '/html/body/section/div/div/div[2]/div[3]/div[1]/ul/li/a')
    NAME_INPUT = (By.ID, 'name')
    EMAIL_INPUT = (By.ID, 'email')
    ADD_REVIEW_INPUT = (By.ID, 'review')
    SUBMIT_REVIEW_BUTTON = (By.ID, 'button-review')
    THANK_YOU_FOR_REVIEW = (By.ID, 'review-section')

    TIMEOUT = ReadConfig.get_timeout_value()

    def navigated_to_product_details_page_successfully(self):
        return 'Product Details' in self.driver.title

    def product_details_is_visible(self):
        product_details = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.PRODUCT_DETAILS))

        return product_details.is_displayed()

    def enter_quantity(self, number_of_items):
        view_product_button = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.QUANTITY_INPUT))

        view_product_button.clear()
        view_product_button.send_keys(number_of_items)

        return self

    def click_add_to_cart_button(self):
        add_to_cart_button = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        time.sleep(1)
        return self

    def click_continue_shopping_button_popup(self):
        continue_shopping_button = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.CONTINUE_SHOPPING_BUTTON))
        continue_shopping_button.click()
        time.sleep(1)
        return self

    def click_view_cart_button_popup(self):
        view_cart_button = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.VIEW_CART_BUTTON))
        view_cart_button.click()
        time.sleep(1)
        return self

    def add_to_cart_and_continue_shopping(self):
        self.click_add_to_cart_button()
        self.click_continue_shopping_button_popup()

    def add_to_cart_and_view_cart(self):
        self.click_add_to_cart_button()
        self.click_view_cart_button_popup()

    def write_your_review_is_visible(self):
        write = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.WRITE_YOUR_REVIEW))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", write)

        return write.is_displayed()


    def enter_name(self, name):
        name_input = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.NAME_INPUT))

        name_input.clear()
        name_input.send_keys(name)

        return self

    def enter_email(self, email):
        email_input = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.EMAIL_INPUT))

        email_input.clear()
        email_input.send_keys(email)

        return self

    def enter_review(self, review):
        review_input = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.ADD_REVIEW_INPUT))

        review_input.clear()
        review_input.send_keys(review)

        return self

    def enter_name_email_and_review(self, name, email, review):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_review(review)
        time.sleep(1)

        return self

    def click_submit_review_button(self):
        button = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.SUBMIT_REVIEW_BUTTON))

        button.click()
        time.sleep(1)
        return self

    def thank_you_for_your_review_is_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: "hide" not in d.find_element(*self.THANK_YOU_FOR_REVIEW).get_attribute("class")
            )
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located(self.THANK_YOU_FOR_REVIEW)
            )
            return True
        except:
            return False
