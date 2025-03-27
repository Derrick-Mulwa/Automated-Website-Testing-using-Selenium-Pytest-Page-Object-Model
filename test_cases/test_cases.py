import pytest
from base_pages.login_page import LoginPage
from base_pages.home_page import HomePage
from base_pages.signup_page import SignupPage
from base_pages.account_created_page import AccountCreatedPage
from base_pages.delete_account_page import DeleteAccountPage
from base_pages.contact_us_page import ContactUsPage
from base_pages.test_cases_page import PageTestCases
from base_pages.all_products_page import AllProductsPage
from base_pages.product_details_page import ProductDetailsPage
from base_pages.view_cart_page import ViewCartPage
from base_pages.checkout_page import CheckoutPage
from base_pages.payments_page import PaymentsPage
from base_pages.payment_done_page import PaymentsDonePage
from base_pages.category_products import CategoryProductsPage
from base_pages.brands_page import BrandsPage

from utilities.verify_download import VerifyDownload
from utilities.read_properties import ReadConfig
import time

class TestCaseOne:
    BASEURL = ReadConfig.get_base_url()
    gender = ReadConfig.get_gender()
    name = ReadConfig.get_name()
    password = ReadConfig.get_password()
    email = ReadConfig.get_email()
    dob_day = ReadConfig.get_dob_day()
    dob_month = ReadConfig.get_dob_month()
    dob_year = ReadConfig.get_dob_year()
    first_name = ReadConfig.get_first_name()
    last_name = ReadConfig.get_last_name()
    company = ReadConfig.get_company()
    address = ReadConfig.get_address1()
    address_2 = ReadConfig.get_address2()
    country = ReadConfig.get_country()
    state = ReadConfig.get_state()
    city = ReadConfig.get_city()
    zip_code = ReadConfig.get_zipcode()
    mobile_number = ReadConfig.get_mobile_number()

    correct_email = ReadConfig.get_correct_email()
    correct_password = ReadConfig.get_correct_password()
    incorrect_email = ReadConfig.get_incorrect_email()
    incorrect_password = ReadConfig.get_incorrect_password()

    contact_subject = ReadConfig.get_contact_subject()
    contact_message = ReadConfig.get_contact_message()
    contact_upload_filepath = ReadConfig.get_contact_us_filepath()

    search_text = ReadConfig.get_search_text()

    first_two_products_data = ReadConfig.get_first_two_product_data()

    card_number = ReadConfig.get_card_number()
    card_cvc = ReadConfig.get_cvc()
    card_expiry_month = ReadConfig.get_expiration_month()
    card_expiration_year = ReadConfig.get_expiration_year()




    def test_case_one(self, setup):
        #1
        self.driver = setup

        #2
        homepage = HomePage(self.driver).navigate_to(self.BASEURL)

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE' #3

        homepage.click_signup_login() #4

        login_page = LoginPage(self.driver)

        assert login_page.new_user_signup_is_visible(), 'NEW USER SIGNUP NOT VISIBLE' #5

        login_page.enter_signup_details(self.name, self.email) #6

        login_page.click_signup_button()#7

        signup = SignupPage(self.driver)

        assert signup.enter_account_information_is_visible(), 'ENTER ACCOUNT INFORMATION NOT VISIBLE' #8

        #9
        signup.select_title(self.gender)
        signup.enter_name(self.name)
        signup.enter_password(self.password)
        signup.enter_date_of_birth(self.dob_day, self.dob_month, self.dob_year)

        signup.check_checkbox_sign_up_for_our_newsletter()#10
        signup.check_checkbox_receive_special_offers()#11

        #12
        signup.enter_first_name(self.first_name)
        signup.enter_last_name(self.last_name)
        signup.enter_company(self.company)
        signup.enter_address(self.address)
        signup.enter_address2(self.address_2)
        signup.enter_country(self.country)
        signup.enter_state(self.state)
        signup.enter_city(self.city)
        signup.enter_zipcode(self.zip_code)
        signup.enter_mobile_number(self.mobile_number)

        signup.click_create_account_button()    #13

        account_created_page = AccountCreatedPage(self.driver)
        assert account_created_page.account_created_is_visible()#14
        account_created_page.click_continue_button()#15

        homepage = HomePage(self.driver)
        homepage.logged_in_as_username_is_visible()#16
        homepage.click_delete_account_button() #17

        delete_account_page = DeleteAccountPage(self.driver)
        delete_account_page.account_deleted_is_visible()
        delete_account_page.click_continue()

    def test_case_two(self, setup):
        # 1
        self.driver = setup

        # 2
        homepage = HomePage(self.driver).navigate_to(self.BASEURL)

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3

        homepage.click_signup_login()  # 4

        login_page = LoginPage(self.driver)

        assert login_page.log_in_to_your_account_is_visible(), 'LOGIN TO YOUR ACCOUNT NOT VISIBLE'  # 5

        login_page.enter_login_details(self.correct_email, self.correct_password) #6

        login_page.click_login_button()#7

        homepage = HomePage(self.driver)

        homepage.logged_in_as_username_is_visible()#8

    def test_case_three(self, setup):
        # 1
        self.driver = setup

        # 2
        homepage = HomePage(self.driver).navigate_to(self.BASEURL)

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3

        homepage.click_signup_login()  # 4

        login_page = LoginPage(self.driver)

        assert login_page.log_in_to_your_account_is_visible(), 'LOGIN TO YOUR ACCOUNT NOT VISIBLE'  # 5

        login_page.enter_login_details(self.incorrect_email, self.incorrect_password)  # 6

        login_page.click_login_button()  # 7

        assert login_page.your_email_or_password_is_incorrect_is_visible()

    def test_case_four(self, setup):
        # 1
        self.driver = setup

        # 2
        homepage = HomePage(self.driver).navigate_to(self.BASEURL)

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3

        homepage.click_signup_login()  # 4

        login_page = LoginPage(self.driver)

        assert login_page.log_in_to_your_account_is_visible(), 'LOGIN TO YOUR ACCOUNT NOT VISIBLE'  # 5

        login_page.enter_login_details(self.correct_email, self.correct_password)  # 6

        login_page.click_login_button()  # 7

        homepage = HomePage(self.driver)

        homepage.logged_in_as_username_is_visible()  # 8

        homepage.click_logout_button() #9

        login_page = LoginPage(self.driver)

        assert login_page.log_in_to_your_account_is_visible()#10


    def test_case_five(self, setup):
        #1
        self.driver = setup

        #2
        homepage = HomePage(self.driver).navigate_to(self.BASEURL)

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE' #3

        homepage.click_signup_login() #4

        login_page = LoginPage(self.driver)

        assert login_page.new_user_signup_is_visible(), 'NEW USER SIGNUP NOT VISIBLE' #5

        login_page.enter_signup_details(self.name, self.correct_email) #6

        login_page.click_signup_button()#7

        assert login_page.email_address_already_exists_is_visible()#8

    def test_case_six(self, setup):
        self.driver = setup # 1
        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2
        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3
        homepage.click_contact_us_button()#4

        contact_us = ContactUsPage(self.driver)

        assert contact_us.get_in_touch_is_visible() #5

        #6
        contact_us.enter_name(self.first_name)
        contact_us.enter_email(self.correct_email)
        contact_us.enter_subject(self.contact_subject)
        contact_us.enter_message(self.contact_message)

        contact_us.upload_file(self.contact_upload_filepath)#7

        contact_us.click_submit_button()#8

        contact_us.click_ok_alert()#9

        assert contact_us.success_your_details_submitted_is_visible()#10

        #11
        contact_us.click_home_button()
        homepage = HomePage(self.driver)
        homepage.homepage_is_visible()

    def test_case_seven(self, setup):
        self.driver = setup # 1
        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2
        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3
        homepage.click_test_cases_button()#4

        test_case = PageTestCases(self.driver)
        assert test_case.test_cases_page_is_visible()#5

    def test_case_eight(self, setup):
        self.driver = setup # 1
        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2
        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3
        homepage.click_products_button()#4

        all_products_page = AllProductsPage(self.driver)
        assert all_products_page.navigated_to_all_products_page_successfully()#5

        assert all_products_page.product_list_is_visible()#6

        all_products_page.click_view_product_button()#7

        product_details_page = ProductDetailsPage(self.driver)
        assert product_details_page.navigated_to_product_details_page_successfully()#8

        assert product_details_page.product_details_is_visible()#9

    def test_case_nine(self, setup):
        self.driver = setup # 1

        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3

        homepage.click_products_button()#4

        all_products_page = AllProductsPage(self.driver)
        assert all_products_page.navigated_to_all_products_page_successfully()#5

        all_products_page.enter_search_text(self.search_text)
        all_products_page.click_search_button()#6

        assert all_products_page.searched_products_text_is_visible()#7

        assert all_products_page.searched_products_list_is_visible()#8

    def test_case_ten(self, setup):
        self.driver = setup # 1

        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3

        homepage.scroll_to_footer()#4

        homepage.subscriptions_is_visible()#5

        #6
        homepage.enter_subscription_email_button(self.correct_email)
        homepage.click_subscribe_button()

        assert homepage.you_have_been_successfully_sub_is_visible()#7

    def test_case_eleven(self, setup):
        self.driver = setup # 1

        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3

        homepage.click_cart_button()

        cart_page = ViewCartPage(self.driver)
        cart_page.scroll_to_footer()#4

        cart_page.subscriptions_is_visible()#5

        #6
        cart_page.enter_subscription_email_button(self.correct_email)
        cart_page.click_subscribe_button()

        assert cart_page.you_have_been_successfully_sub_is_visible()#7

    def test_case_twelve(self, setup):
        self.driver = setup # 1

        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3

        homepage.click_products_button()#4

        all_products_page = AllProductsPage(self.driver)
        all_products_page.hover_add_to_cart_and_continue_shopping(1)#5 & 6
        all_products_page.hover_and_add_to_cart_and_view_cart(2)#7&8

        cart_page = ViewCartPage(self.driver)
        assert cart_page.get_number_of_cart_items() == 2 #9

        assert cart_page.get_cart_data() == self.first_two_products_data #10

    def test_case_13(self, setup):
        self.driver = setup # 1

        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3

        homepage.click_view_product_from_homepage(2)#4

        product_details_page = ProductDetailsPage(self.driver)

        product_details_page.product_details_is_visible()#5

        product_details_page.enter_quantity(4)#6

        product_details_page.click_add_to_cart_button()#7

        product_details_page.click_view_cart_button_popup()#8

        view_cart_page = ViewCartPage(self.driver)
        data = view_cart_page.get_cart_data()
        assert data[0]['Quantity'] == '4'

    def test_case_14(self, setup):
        self.driver = setup # 1

        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3

        #4
        homepage.hover_add_to_cart_and_continue_shopping(1)
        homepage.hover_add_to_cart_and_continue_shopping(2)

        homepage.click_cart_button()#5

        cart_page = ViewCartPage(self.driver)
        cart_page.cart_info_table_is_visible()#6
        cart_page.click_proceed_to_checkout_button()#7
        cart_page.click_register_login_popup_btn()#8

        #9
        login_page = LoginPage(self.driver)

        login_page.enter_signup_details(self.name, self.email)

        login_page.click_signup_button()

        signup = SignupPage(self.driver)

        assert signup.enter_account_information_is_visible(), 'ENTER ACCOUNT INFORMATION NOT VISIBLE'


        signup.select_title(self.gender)
        signup.enter_name(self.name)
        signup.enter_password(self.password)
        signup.enter_date_of_birth(self.dob_day, self.dob_month, self.dob_year)

        signup.check_checkbox_sign_up_for_our_newsletter()
        signup.check_checkbox_receive_special_offers()

        # 12
        signup.enter_first_name(self.first_name)
        signup.enter_last_name(self.last_name)
        signup.enter_company(self.company)
        signup.enter_address(self.address)
        signup.enter_address2(self.address_2)
        signup.enter_country(self.country)
        signup.enter_state(self.state)
        signup.enter_city(self.city)
        signup.enter_zipcode(self.zip_code)
        signup.enter_mobile_number(self.mobile_number)

        signup.click_create_account_button()

        account_created_page = AccountCreatedPage(self.driver)
        #10
        assert account_created_page.account_created_is_visible()
        account_created_page.click_continue_button()

        homepage = HomePage(self.driver)
        assert homepage.logged_in_as_username_is_visible() #11

        homepage.click_cart_button()#12

        view_cart_page = ViewCartPage(self.driver)
        view_cart_page.click_proceed_to_checkout_button() #13

        checkout_page = CheckoutPage(self.driver)
        address = [f'{self.company}\n{self.address}\n{self.address_2}', self.country, self.mobile_number, f'{self.city} {self.state} {self.zip_code}']

        assert checkout_page.verify_address(address)
        assert checkout_page.review_your_order() #14

        checkout_page.enter_description_and_click_place_order('Nice_order')#15

        payment_page = PaymentsPage(self.driver)

        payment_page.enter_payment_details_and_click_pay_button(self.name, self.card_number, self.card_cvc, self.card_expiry_month, self.card_expiration_year)#16 & 17

        payment_done = PaymentsDonePage(self.driver)
        assert payment_done.congratulations_your_order_is_visible() #18

        payment_done.click_delete_account_button() #19

        account_deleted = DeleteAccountPage(self.driver)
        account_deleted.account_deleted_is_visible() #20
        account_deleted.click_continue()

    def test_case_15(self, setup):
        #1
        self.driver = setup

        #2
        homepage = HomePage(self.driver).navigate_to(self.BASEURL)

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE' #3

        homepage.click_signup_login() #4

        # 5
        login_page = LoginPage(self.driver)

        assert login_page.new_user_signup_is_visible(), 'NEW USER SIGNUP NOT VISIBLE'

        login_page.enter_signup_details(self.name, self.email)

        login_page.click_signup_button()

        signup = SignupPage(self.driver)

        assert signup.enter_account_information_is_visible(), 'ENTER ACCOUNT INFORMATION NOT VISIBLE'

        signup.select_title(self.gender)
        signup.enter_name(self.name)
        signup.enter_password(self.password)
        signup.enter_date_of_birth(self.dob_day, self.dob_month, self.dob_year)

        signup.check_checkbox_sign_up_for_our_newsletter()
        signup.check_checkbox_receive_special_offers()


        signup.enter_first_name(self.first_name)
        signup.enter_last_name(self.last_name)
        signup.enter_company(self.company)
        signup.enter_address(self.address)
        signup.enter_address2(self.address_2)
        signup.enter_country(self.country)
        signup.enter_state(self.state)
        signup.enter_city(self.city)
        signup.enter_zipcode(self.zip_code)
        signup.enter_mobile_number(self.mobile_number)

        signup.click_create_account_button()

        # 6
        account_created_page = AccountCreatedPage(self.driver)
        assert account_created_page.account_created_is_visible()
        account_created_page.click_continue_button()

        #7
        homepage = HomePage(self.driver)
        homepage.logged_in_as_username_is_visible()

        #8
        homepage.hover_add_to_cart_and_continue_shopping(1)
        homepage.hover_add_to_cart_and_continue_shopping(2)

        homepage.click_cart_button() #9

        cart_page = ViewCartPage(self.driver)
        assert cart_page.cart_info_table_is_visible()  # 10

        cart_page.click_proceed_to_checkout_button() #11

        checkout_page = CheckoutPage(self.driver)
        address = [f'{self.company}\n{self.address}\n{self.address_2}', self.country, self.mobile_number,
                   f'{self.city} {self.state} {self.zip_code}']

        assert checkout_page.verify_address(address)
        assert checkout_page.review_your_order()  # 12

        checkout_page.enter_description_and_click_place_order('Nice_order')  # 13

        payment_page = PaymentsPage(self.driver)

        payment_page.enter_payment_details_and_click_pay_button(self.name, self.card_number, self.card_cvc,
                                                                self.card_expiry_month,
                                                                self.card_expiration_year) #14 & 15

        payment_done = PaymentsDonePage(self.driver)
        assert payment_done.congratulations_your_order_is_visible()  # 16

        payment_done.click_delete_account_button()  # 17

        account_deleted = DeleteAccountPage(self.driver)
        account_deleted.account_deleted_is_visible()  # 18
        account_deleted.click_continue()


    def test_case_16(self, setup):
        #1
        self.driver = setup

        #2
        homepage = HomePage(self.driver).navigate_to(self.BASEURL)

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE' #3

        homepage.click_signup_login() #4

        # 5
        login_page = LoginPage(self.driver)
        login_page.enter_login_details(self.correct_email, self.correct_password)
        login_page.click_login_button()

        #6
        homepage = HomePage(self.driver)
        homepage.logged_in_as_username_is_visible()

        #7
        homepage.hover_add_to_cart_and_continue_shopping(2)
        homepage.hover_add_to_cart_and_continue_shopping(3)

        homepage.click_cart_button() #8

        cart_page = ViewCartPage(self.driver)
        assert cart_page.cart_info_table_is_visible() #9

        cart_page.click_proceed_to_checkout_button()#10

        checkout_page = CheckoutPage(self.driver)
        address = [f'X\nABC\nDEF', 'Israel', '912129929292', f'Sity Stato 00100']

        assert checkout_page.verify_address(address)
        assert checkout_page.review_your_order() #11

        checkout_page.enter_description_and_click_place_order('Placing login order') #12

        payment_page = PaymentsPage(self.driver)

        payment_page.enter_payment_details_and_click_pay_button(self.name, self.card_number, self.card_cvc,
                                                                self.card_expiry_month,
                                                                self.card_expiration_year) #13& 14

        payment_done = PaymentsDonePage(self.driver)
        assert payment_done.congratulations_your_order_is_visible() #15

    def test_case_17(self, setup):
        self.driver = setup # 1

        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3

        #4
        homepage.hover_add_to_cart_and_continue_shopping(3)
        homepage.hover_add_to_cart_and_continue_shopping(1)

        homepage.click_cart_button()#5

        cart_page = ViewCartPage(self.driver)
        assert cart_page.cart_info_table_is_visible()#6

        cart_page.delete_item_from_order(1) #7

        assert cart_page.get_number_of_cart_items() == 2-1 #8


    def test_case_18(self, setup):
        self.driver = setup # 1

        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2

        assert homepage.left_category_is_visible(), 'LEFT CATEGORY NOT VISIBLE'  # 3

        homepage.click_women_subcategory(3)#4

        homepage.click_women_subcategory(3)#5

        category_products_page = CategoryProductsPage(self.driver)
        assert category_products_page.category_text_is_visible()#6

        category_products_page.click_men_subcategory(2)#7

        assert category_products_page.category_text_is_visible()#8


    def test_case_19(self, setup):
        self.driver = setup # 1

        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2

        homepage.click_products_button()#3

        all_products_page = AllProductsPage(self.driver)
        assert all_products_page.verify_brands_are_visible()#4

        all_products_page.click_brand(2) #5

        brand_page = BrandsPage(self.driver)
        assert brand_page.brand_products_are_visible()#6

        brand_page.click_brand(4)#7

        assert brand_page.brand_products_are_visible()#8


    def test_case_20(self, setup):
        self.driver = setup # 1

        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2

        homepage.click_products_button()#3

        all_products_page = AllProductsPage(self.driver)
        assert all_products_page.all_products_text_is_visible()  # 4

        all_products_page.enter_search_text(self.search_text)#5
        all_products_page.click_search_button()

        assert all_products_page.searched_products_text_is_visible()#6

        assert all_products_page.searched_products_list_is_visible()#7

        all_products_page.add_all_searched_products_to_cart()#8

        all_products_page.click_cart_button()

        cart_page = ViewCartPage(self.driver)
        assert cart_page.cart_info_table_is_visible()#9

        cart_page.click_signup_login_button()
        login_page = LoginPage(self.driver)

        login_page.enter_login_details(self.correct_email, self.correct_password)
        login_page.click_login_button()#10

        homepage = HomePage(self.driver)
        homepage.click_cart_button()#11

        cart_page = ViewCartPage(self.driver)
        assert cart_page.cart_info_table_is_visible()#12

        cart_page.delete_all_items_from_order()#13

        assert cart_page.cart_is_empty_text_is_visible()#14


    def test_case_21(self, setup):
        self.driver = setup # 1

        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2

        homepage.click_products_button()#3

        all_products_page = AllProductsPage(self.driver)
        assert all_products_page.all_products_text_is_visible()  # 4

        all_products_page.click_view_product_button()#5

        product_details_page = ProductDetailsPage(self.driver)
        assert product_details_page.write_your_review_is_visible()#6

        product_details_page.enter_name_email_and_review(self.name, self.email, 'I like this cloth')#7
        product_details_page.click_submit_review_button()#8

        assert product_details_page.thank_you_for_your_review_is_visible()#9

    def test_case_22(self, setup):
        self.driver = setup # 1

        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2

        homepage.scroll_to_bottom()#3
        assert homepage.recommended_items_is_visible()#4

        homepage.click_to_cart_on_recommended_button()#5
        homepage.click_view_cart_button_popup()#6

        view_cart_page = ViewCartPage(self.driver)
        assert view_cart_page.get_number_of_cart_items() == 1 #7

    def test_case_23(self, setup):
        #1
        self.driver = setup

        #2
        homepage = HomePage(self.driver).navigate_to(self.BASEURL)

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE' #3

        homepage.click_signup_login() #4

        # 5
        login_page = LoginPage(self.driver)

        assert login_page.new_user_signup_is_visible(), 'NEW USER SIGNUP NOT VISIBLE'

        login_page.enter_signup_details(self.name, self.email)

        login_page.click_signup_button()

        signup = SignupPage(self.driver)

        assert signup.enter_account_information_is_visible(), 'ENTER ACCOUNT INFORMATION NOT VISIBLE'

        signup.select_title(self.gender)
        signup.enter_name(self.name)
        signup.enter_password(self.password)
        signup.enter_date_of_birth(self.dob_day, self.dob_month, self.dob_year)
        signup.check_checkbox_sign_up_for_our_newsletter()
        signup.check_checkbox_receive_special_offers()
        signup.enter_first_name(self.first_name)
        signup.enter_last_name(self.last_name)
        signup.enter_company(self.company)
        signup.enter_address(self.address)
        signup.enter_address2(self.address_2)
        signup.enter_country(self.country)
        signup.enter_state(self.state)
        signup.enter_city(self.city)
        signup.enter_zipcode(self.zip_code)
        signup.enter_mobile_number(self.mobile_number)

        signup.click_create_account_button()

        # 6
        account_created_page = AccountCreatedPage(self.driver)
        assert account_created_page.account_created_is_visible()
        account_created_page.click_continue_button()

        #7
        homepage = HomePage(self.driver)
        homepage.logged_in_as_username_is_visible()

        #8
        homepage.hover_add_to_cart_and_continue_shopping(1)
        homepage.hover_add_to_cart_and_continue_shopping(2)

        homepage.click_cart_button() #9

        cart_page = ViewCartPage(self.driver)
        assert cart_page.cart_info_table_is_visible()  # 10

        cart_page.click_proceed_to_checkout_button() #11

        checkout_page = CheckoutPage(self.driver)
        address = [f'{self.company}\n{self.address}\n{self.address_2}', self.country, self.mobile_number,
                   f'{self.city} {self.state} {self.zip_code}']

        assert checkout_page.verify_address(address)
        assert checkout_page.verify_billing_address(address)# 12

        checkout_page.click_delete_account_button()  # 13

        account_deleted = DeleteAccountPage(self.driver)
        account_deleted.account_deleted_is_visible()
        account_deleted.click_continue() #14


    def test_case_24(self, setup):
        self.driver = setup # 1

        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3

        #4
        homepage.hover_add_to_cart_and_continue_shopping(3)
        homepage.hover_add_to_cart_and_continue_shopping(5)

        homepage.click_cart_button()#5

        cart_page = ViewCartPage(self.driver)
        cart_page.cart_info_table_is_visible()#6

        cart_page.click_proceed_to_checkout_button()#7
        cart_page.click_register_login_popup_btn()#8

        #9
        login_page = LoginPage(self.driver)

        login_page.enter_signup_details(self.name, self.email)

        login_page.click_signup_button()

        signup = SignupPage(self.driver)

        assert signup.enter_account_information_is_visible(), 'ENTER ACCOUNT INFORMATION NOT VISIBLE'


        signup.select_title(self.gender)
        signup.enter_name(self.name)
        signup.enter_password(self.password)
        signup.enter_date_of_birth(self.dob_day, self.dob_month, self.dob_year)

        signup.check_checkbox_sign_up_for_our_newsletter()
        signup.check_checkbox_receive_special_offers()


        signup.enter_first_name(self.first_name)
        signup.enter_last_name(self.last_name)
        signup.enter_company(self.company)
        signup.enter_address(self.address)
        signup.enter_address2(self.address_2)
        signup.enter_country(self.country)
        signup.enter_state(self.state)
        signup.enter_city(self.city)
        signup.enter_zipcode(self.zip_code)
        signup.enter_mobile_number(self.mobile_number)

        signup.click_create_account_button()

        account_created_page = AccountCreatedPage(self.driver)

        #10
        assert account_created_page.account_created_is_visible()
        account_created_page.click_continue_button()

        homepage = HomePage(self.driver)
        assert homepage.logged_in_as_username_is_visible() #11

        homepage.click_cart_button()#12

        view_cart_page = ViewCartPage(self.driver)
        view_cart_page.click_proceed_to_checkout_button() #13

        checkout_page = CheckoutPage(self.driver)
        address = [f'{self.company}\n{self.address}\n{self.address_2}', self.country, self.mobile_number, f'{self.city} {self.state} {self.zip_code}']

        assert checkout_page.verify_address(address)
        assert checkout_page.review_your_order() #14

        checkout_page.enter_description_and_click_place_order('Nice_order')#15

        payment_page = PaymentsPage(self.driver)

        payment_page.enter_payment_details_and_click_pay_button(self.name, self.card_number, self.card_cvc, self.card_expiry_month, self.card_expiration_year)#16 & 17

        payment_done = PaymentsDonePage(self.driver)
        assert payment_done.congratulations_your_order_is_visible() #18

        #19
        payment_done.click_download_invoice_button()
        verify_download = VerifyDownload()
        assert verify_download.verify_invoice_download()

        payment_done.click_continue_button()#20

        homepage = HomePage(self.driver)
        homepage.click_delete_account_button()#21

        account_deleted = DeleteAccountPage(self.driver)
        assert account_deleted.account_deleted_is_visible()
        account_deleted.click_continue()

    def test_case_25(self, setup):
        self.driver = setup # 1

        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3

        homepage.scroll_to_bottom()#4

        assert homepage.subscriptions_is_visible()#5

        homepage.click_scroll_up_button()#6

        assert homepage.full_fledged_practice_is_visible()#7

    def test_case_26(self, setup):
        self.driver = setup # 1

        homepage = HomePage(self.driver).navigate_to(self.BASEURL) # 2

        assert homepage.homepage_is_visible(), 'HOMEPAGE NOT VISIBLE'  # 3

        homepage.scroll_to_bottom()#4

        assert homepage.subscriptions_is_visible()#5

        homepage.scroll_to_top()#6

        assert homepage.full_fledged_practice_is_visible()#7