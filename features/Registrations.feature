Feature: New registrations
  Background:
    Given the user is on the Registrations page

  Scenario: A user creates a new account
    When the user enters their contact information
    And the user living in UK enters their mailing information
    And the user chooses test123 as their username
    And the user chooses password123 as their password
    And the user confirms their password with password123
    And the user clicks the 'Submit' button
    Then the account will be created successfully