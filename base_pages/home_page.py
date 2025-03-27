from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base_pages.base_page import BasePage
from utilities.read_properties import ReadConfig


class HomePage(BasePage):
    SIGNUP_LOGIN_BUTTON = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    LOGGED_IN_AS = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')
    DELETE_ACCOUNT = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
    SLIDER_CAROUSEL = (By.ID, "slider")
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    CONTACT_US_BUTTON = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[8]/a')
    TEST_CASES_BUTTON = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
    PRODUCTS_BUTTON = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a')
    FOOTER = (By.ID,'footer')
    SUBSCRIPTION = (By.XPATH, '//*[@id="footer"]/div[1]/div/div/div[2]/div/h2')
    SUBSCRIPTION_EMAIL = (By.ID, 'susbscribe_email')
    SUBSCRIBE_BUTTON = (By.ID, 'subscribe')
    SUCCESS_SUBSCRIBE = (By.ID, "success-subscribe")
    CART_BUTTON = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a')

    VIEW_PRODUCT_PRE_XPATH = '/html/body/section[2]/div[1]/div/div[2]/div[1]/div'
    VIEW_PRODUCT_POST_XPATH = '/div/div[2]/ul/li/a'

    PRODUCT_XPATH_PRE = '/html/body/section[2]/div[1]/div/div[2]/div[1]/div'
    PRODUCT_XPATH_POST = '/div/div[1]/div[1]'
    ADD_TO_CART_XPATH_POST = '/div/div[1]/div[2]/div/a/i'


    CONTINUE_SHOPPING_BUTTON = (By.XPATH, '//*[@id="cartModal"]/div/div/div[3]/button')
    VIEW_CART_BUTTON = (By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a')


    LEFT_CATEGORY_SIDEBAR = (By.ID, 'accordian')
    WOMEN_ITEMS = (By.XPATH, '//*[@id="accordian"]/div[1]/div[1]/h4/a/span')
    WOMEN_ITEMS_SUBCAT = (By.XPATH, '//*[@id="Women"]/div/ul')

    RECOMMENDED_ITEMS_TEXT = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div[2]/h2')
    ADD_TO_CART_RECCOMMENDED = (By.XPATH, '//*[@id="recommended-item-carousel"]/div/div[1]/div[1]/div/div/div/a/i')


    FULL_FLEDGED_PRACTICE_TEXT = (By.XPATH, '//*[@id="slider-carousel"]/div/div[1]/div[1]/h2')
    SCROLLUP_BUTTON = (By.ID, 'scrollUp')

    TIMEOUT = ReadConfig.get_timeout_value()


    def click_signup_login(self):
        self.driver.find_element(*self.SIGNUP_LOGIN_BUTTON).click()
        time.sleep(3)
        return self

    def click_scroll_up_button(self):
        self.driver.find_element(*self.SCROLLUP_BUTTON).click()
        time.sleep(3)
        return self

    def homepage_is_visible(self):
        homepage_carousel = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.SLIDER_CAROUSEL))

        return homepage_carousel.is_displayed()

    def full_fledged_practice_is_visible(self):
        full_fledged_text = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.FULL_FLEDGED_PRACTICE_TEXT))

        return full_fledged_text.is_displayed()

    def logged_in_as_username_is_visible(self):
        logged_in_as = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.LOGGED_IN_AS))

        return logged_in_as.is_displayed()

    def click_delete_account_button(self):
        self.driver.find_element(*self.DELETE_ACCOUNT).click()
        time.sleep(3)
        return self

    def click_logout_button(self):
        logout_button = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.LOGOUT_BUTTON))

        logout_button.click()
        time.sleep(3)

        return self

    def click_contact_us_button(self):
        contact_us_button = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.CONTACT_US_BUTTON))

        contact_us_button.click()
        time.sleep(3)

        return self

    def click_test_cases_button(self):
        test_cases_btn = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.TEST_CASES_BUTTON))

        test_cases_btn.click()
        time.sleep(3)

        return self

    def click_products_button(self):
        products_btn = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.PRODUCTS_BUTTON))

        products_btn.click()
        time.sleep(3)

        return self

    def scroll_to_footer(self):
        footer = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.FOOTER))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer)
        time.sleep(1)

        return self

    def subscriptions_is_visible(self):
        subscriptions = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.SUBSCRIPTION))

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

    def click_cart_button(self):
        cart_btn = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.CART_BUTTON))

        cart_btn.click()
        time.sleep(3)

        return self



    def click_view_product_from_homepage(self, product_number):
        product_full_xpath = (By.XPATH, f"{self.VIEW_PRODUCT_PRE_XPATH}[{product_number + 1}]{self.VIEW_PRODUCT_POST_XPATH}")

        view_product_button = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(product_full_xpath))

        view_product_button.click()
        return self

    def hover_and_add_to_cart(self, product_number):
        # product_number is 1 for first, 2 for second, etc, how they appear on the page
        product_full_xpath = f'{self.PRODUCT_XPATH_PRE}[{product_number + 1}]{self.PRODUCT_XPATH_POST}'
        add_to_cart_xpath = f"{self.PRODUCT_XPATH_PRE}[{product_number + 1}]{self.ADD_TO_CART_XPATH_POST}"


        product_element = (By.XPATH, product_full_xpath)
        add_to_cart_element = (By.XPATH, add_to_cart_xpath)

        hover_product = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(product_element))

        self.actions.move_to_element(hover_product).perform()
        time.sleep(2)

        add_to_cart_btn = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(add_to_cart_element))
        add_to_cart_btn.click()
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

    def hover_and_add_to_cart_and_view_cart(self, product_number):
        self.hover_and_add_to_cart(product_number)
        self.click_view_cart_button_popup()
        return self

    def hover_add_to_cart_and_continue_shopping(self, product_number):
        self.hover_and_add_to_cart(product_number)
        self.click_continue_shopping_button_popup()
        return self

    def left_category_is_visible(self):
        left = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.LEFT_CATEGORY_SIDEBAR))

        return left.is_displayed()


    def click_women_items(self):
        women_items = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.WOMEN_ITEMS))

        time.sleep(3)

        women_items.click()

    def click_women_subcategory(self, number):
        items = self.driver.find_element(*self.WOMEN_ITEMS_SUBCAT).find_elements(By.TAG_NAME, 'a')
        item_to_click = items[number - 1]
        if item_to_click.is_displayed():
            item_to_click.click()
        else:
            self.click_women_items()
            time.sleep(2)
            item_to_click.click()


    def recommended_items_is_visible(self):
        recommended_items = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.RECOMMENDED_ITEMS_TEXT))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", recommended_items)
        time.sleep(2)

        return recommended_items.is_displayed()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        return self

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        time.sleep(2)
        return self

    def click_to_cart_on_recommended_button(self):
        cart_btn = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.ADD_TO_CART_RECCOMMENDED))

        cart_btn.click()
        time.sleep(3)

        return self





