from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base_pages.base_page import BasePage
from utilities.read_properties import ReadConfig


class ViewCartPage(BasePage):
    SHOPPING_CART_TEXT = (By.XPATH, '//*[@id="cart_items"]/div/div[1]/ol/li[2]')
    FOOTER = (By.ID, 'footer')

    SUBSCRIPTION_TEXT = (By.XPATH, '//*[@id="footer"]/div[1]/div/div/div[2]/div/h2')
    SUBSCRIPTION_EMAIL = (By.ID, 'susbscribe_email')
    SUBSCRIBE_BUTTON = (By.ID, 'subscribe')
    SUCCESS_SUBSCRIBE = (By.ID, "success-subscribe")
    CART_INFO_TABLE = (By.ID, 'cart_info_table')
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, '//*[@id="do_action"]/div[1]/div/div/a')
    REGISTER_LOGIN_POPUP_BUTTON = (By.XPATH, '//*[@id="checkoutModal"]/div/div/div[2]/p[2]/a/u')
    CONTINUE_ON_CART_POPUP_BUTTON = (By.XPATH, '//*[@id="checkoutModal"]/div/div/div[3]/button')

    TABLE_ROWS_ELEMENT = (By.XPATH, '//*[@id="cart_info_table"]/tbody/tr')
    TABLE_ROW = '//*[@id="cart_info_table"]/tbody/tr'

    SIGNUP_LOGIN_BUTTON = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    CART_IS_EMPTY_TEXT = (By.ID, 'empty_cart')
    SOMETHING = (By.XPATH,)
    SOMETHING = (By.XPATH,)



    TIMEOUT = ReadConfig.get_timeout_value()

    def scroll_to_footer(self):
        footer = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.FOOTER))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer)
        time.sleep(1)

        return self

    def subscriptions_is_visible(self):
        subscriptions = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.SUBSCRIPTION_TEXT))

        return subscriptions.is_displayed()

    def enter_subscription_email_button(self, email):
        email_text_input = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.SUBSCRIPTION_EMAIL))

        email_text_input.clear()
        email_text_input.send_keys(email)
        time.sleep(1)

        return self

    def click_subscribe_button(self):
        products_btn = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.SUBSCRIBE_BUTTON))

        products_btn.click()

        return self

    def you_have_been_successfully_sub_is_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: "hide" not in d.find_element(*self.SUCCESS_SUBSCRIBE).get_attribute("class")
            )
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located(self.SUCCESS_SUBSCRIBE)
            )
            return True
        except:
            return False

    def cart_info_table_is_visible(self):
        try:
            table = WebDriverWait(self.driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(self.CART_INFO_TABLE))

            return table.is_displayed()
        except:
            return False

    def get_number_of_cart_items(self):
        try:
            table = WebDriverWait(self.driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(self.CART_INFO_TABLE))
            rows = table.find_elements(By.XPATH, "./tbody/tr")
            number_of_rows = len(rows)
            return  number_of_rows
        except:
            return 0

    def get_cart_data(self):
        try:
            table = WebDriverWait(self.driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(self.CART_INFO_TABLE))
            rows = table.find_elements(By.XPATH, "./tbody/tr")

            table_data = []
            for row in rows:
                # Extract data from each column
                product_name = row.find_element(By.CSS_SELECTOR, ".cart_description h4 a").text
                category = row.find_element(By.CSS_SELECTOR, ".cart_description p").text
                price = row.find_element(By.CSS_SELECTOR, ".cart_price p").text
                quantity = row.find_element(By.CSS_SELECTOR, ".cart_quantity button").text
                total = row.find_element(By.CSS_SELECTOR, ".cart_total_price").text

                # Append the data as a dictionary
                table_data.append({
                    "Product Name": product_name,
                    "Category": category,
                    "Price": price,
                    "Quantity": quantity,
                    "Total": total
                })
            return table_data
        except:
            return None

    def click_proceed_to_checkout_button(self):
        btn = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.PROCEED_TO_CHECKOUT_BUTTON))

        btn.click()

        return self

    def click_register_login_popup_btn(self):
        btn = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.REGISTER_LOGIN_POPUP_BUTTON))

        btn.click()

        return self

    def click_continue_on_cart_popup_btn(self):
        btn = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.CONTINUE_ON_CART_POPUP_BUTTON))

        btn.click()

        return self


    def delete_item_from_order(self, item_number):
        # Locate all rows in the table's body
        rows = self.driver.find_elements(*self.TABLE_ROWS_ELEMENT)
        xpaths = []

        for index in range(1, len(rows) + 1):
            xpath = self.TABLE_ROW + f'[{index}]/td[@class="cart_delete"]/a[@class="cart_quantity_delete"]'
            xpaths.append(xpath)

        item_to_delete = self.driver.find_element(By.XPATH, xpaths[int(item_number) - 1])
        item_to_delete.click()
        time.sleep(3)

        return self


    def delete_all_items_from_order(self):
        # Locate all rows in the table's body
        rows = self.driver.find_elements(*self.TABLE_ROWS_ELEMENT)

        for i in rows:
            btn = i.find_element(By.CLASS_NAME, 'fa-times')
            btn.click()
            time.sleep(0.5)

        return self


    def click_signup_login_button(self):
        btn = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.SIGNUP_LOGIN_BUTTON))

        btn.click()

        return self

    def cart_is_empty_text_is_visible(self):
        empty_cart = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.CART_IS_EMPTY_TEXT))

        return empty_cart.is_displayed()
