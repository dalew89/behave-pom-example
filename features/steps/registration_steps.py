from behave import *


@when("the user enters their first name")
def step_impl(context):
    context.registration_page.set_first_name()


@when("the user enters their last name")
def step_impl(context):
    context.registration_page.set_last_name()


@when("the user enters their phone number")
def step_impl(context):
    context.registration_page.set_phone_num()


@when("the user enters their email address")
def step_impl(context):
    context.registration_page.set_email_address()


@when("the user enters their contact information")
def step_impl(context):  # combine the contact information steps
    context.execute_steps(u'''
    When the user enters their first name
    And the user enters their last name
    And the user enters their phone number
    And the user enters their email address
    ''')


@when("the user enters the first line of their address")
def step_impl(context):
    context.registration_page.set_address_line_1()


@when("the user enters their city")
def step_impl(context):
    context.registration_page.set_city()


@when("the user enters their state")
def step_impl(context):
    context.registration_page.set_state()


@when("the user enters their postcode")
def step_impl(context):
    context.registration_page.set_postcode()


@when("the user sets {country} as their country of residence")
def step_impl(context, country):
    context.registration_page.set_country(country)


@when("the user living in {country} enters their mailing information")
def step_impl(context, country):  # Combine the mailing information steps
    context.execute_steps(u'''
    When the user enters the first line of their address
    And the user enters their city
    And the user enters their postcode
    And the user sets {country} as their country of residence 
    '''.format(country=country))


@when("the user chooses {username} as their username")
def step_impl(context, username):
    context.registration_page.set_username(username)


@when("the user chooses {password} as their password")
def step_impl(context, password):
    context.registration_page.set_password(password)


@when("the user confirms their password with {confirmed_password}")
def step_impl(context, confirmed_password):
    context.registration_page.confirm_password(confirmed_password)


@when("the user clicks the 'Submit' button")
def step_impl(context):
    context.registration_page.click_submit()


@when("the user submits {username} as their username, with {password} and {confirmed_password}")
def step_impl(context, username, password, confirmed_password):  # Combine the login information steps
    context.execute_steps(u'''
    When the user chooses {username} as their username
    When the user chooses {password} as their password
    When the user confirms their password with {confirmed_password}
    '''.format(username=username, password=password, confirmed_password=confirmed_password))


@then("the account will be created successfully")
def step_impl(context):
    context.registration_page.confirm_account_creation()
