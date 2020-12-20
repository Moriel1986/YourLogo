Feature: RedSelf Login
  Scenario: Verify RedShelf Login Credentials
    Given Launch FireFox Browser
    When User clicks loginBtn
    And User enters Username
    And User enters Password
    And User clicks login
    Then User should see My Shelf in header one
