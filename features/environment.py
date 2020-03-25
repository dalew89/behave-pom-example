from behave import *
from selenium import webdriver
from features.pages.registration_page import RegistrationPage


HOMEPAGE = "http://newtours.demoaut.com/mercurywelcome.php"

SECTIONS = {  # links of the navigation bar
    "Registrations": "REGISTER"
}


def before_feature(context, feature):
    context.driver = webdriver.Chrome()
    context.driver.get(HOMEPAGE)
    context.registration_page = RegistrationPage(context.driver)


@given("the user is on the {section} page")
def navigate_to(context, section):
    context.driver.find_element_by_link_text(SECTIONS[section]).click()


def after_feature(context, feature):
    context.driver.quit()
