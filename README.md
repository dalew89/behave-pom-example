# Page Object Model with Behave(BDD)
This is a very simple example of implementing the Page Object Model and [Behave](https://pypi.org/project/behave/) with Selenium and Chromedriver

This project operates on the demo site: http://newtours.demoaut.com/create_account_success.php

So far this only includes one page object, with a feature file and associated steps. 

This project uses:
- [Selenium](https://github.com/SeleniumHQ/selenium) for the automation
- [Behave] as the test framework
- [Faker](https://github.com/joke2k/faker) to generate fake user data. Documentation for faker can be found [here.](https://faker.readthedocs.io/en/master/)
 

To install dependencies, type:

```pip install requirements.txt```

into your terminal.

Additional requirements:
 - Chromedriver

To run this test, type:

```behave```

