from behave import *
from selenium import webdriver
from features.pages.registration_page import RegistrationPage


HOMEPAGE = "http://newtours.demoaut.com/mercurywelcome.php"

SECTIONS = {  # links of the navigation bar
    "Registrations": "REGISTER"
}


@fixture
def driver(context):
    context.driver = webdriver.Chrome()
    yield
    context.driver.quit()


def before_all(context):
    use_fixture(driver, context)
    context.registration_page = RegistrationPage(context.driver)


def before_scenario(context, scenario):
    context.driver.get(HOMEPAGE)


def after_scenario(context, scenario):
    context.driver.delete_all_cookies()


# Common steps exist inside of environment.py
@given("the user is on the {section} page")
def navigate_to(context, section):
    context.driver.find_element_by_link_text(SECTIONS[section]).click()
