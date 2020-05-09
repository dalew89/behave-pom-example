from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from faker import Faker


class RegistrationPage(BasePage):
    """ Methods and elements on the new Reg Page as seen here: http://newtours.demoaut.com/mercuryregister.php)"""

    def __init__(self, driver):
        super().__init__(driver)
        self.fake = Faker(["en_GB"])  # Localised to UK addresses and numbers 

    # Contact Information
    first_name_field = (By.NAME, "firstName")
    last_name_field = (By.NAME, "lastName")
    phone_field = (By.NAME, "phone")
    email_field = (By.NAME, "userName")

    # Mailing Information
    address_field = (By.NAME, "address1")
    city_field = (By.NAME, "city")
    state_province_field = (By.NAME, "state")
    postcode_field = (By.NAME, "postalCode")
    country_dropdown = (By.NAME, "country")

    # User Information
    username_field = (By.ID, "email")
    password_field = (By.NAME, "password")
    confirm_password_field = (By.NAME, "confirmPassword")

    submit_button = (By.NAME, "register")

    countries = {  # a few of the countries in the dropdown on the registration page, with their dropdown values.
        "UK": "214",
        "France": "65",
        "Germany": "242",
    }

    def set_first_name(self):
        self.driver.find_element(*RegistrationPage.first_name_field).send_keys(self.fake.first_name())

    def set_last_name(self):
        self.driver.find_element(*RegistrationPage.last_name_field).send_keys(self.fake.last_name())

    def set_phone_num(self):
        self.driver.find_element(*RegistrationPage.phone_field).send_keys(self.fake.phone_number())

    def set_email_address(self):
        self.driver.find_element(*RegistrationPage.email_field).send_keys(self.fake.email())

    def set_address_line_1(self):
        self.driver.find_element(*RegistrationPage.address_field) \
            .send_keys(f"{self.fake.building_number()} {self.fake.street_name()}")

    def set_city(self):
        self.driver.find_element(*RegistrationPage.city_field).send_keys(self.fake.city())

    def set_postcode(self):
        self.driver.find_element(*RegistrationPage.postcode_field).send_keys(self.fake.postcode())

    def set_country(self, country):
        country_dropdown = Select(self.driver.find_element(*RegistrationPage.country_dropdown))
        country_dropdown.select_by_value(RegistrationPage.countries[country])

    def set_username(self, username):
        self.driver.find_element(*RegistrationPage.username_field).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*RegistrationPage.password_field).send_keys(password)

    def confirm_password(self, confirm_password):
        self.driver.find_element(*RegistrationPage.confirm_password_field).send_keys(confirm_password)

    def click_submit(self):
        self.driver.find_element(*RegistrationPage.submit_button).click()

    def confirm_account_creation(self):
        assert self.driver.current_url == "http://newtours.demoaut.com/create_account_success.php"
