Feature: Book rent

Scenario: rent successful
  Given user1 rent counter is equal 0
    And user1 BookStore Card is valid
    And the selected book1 is available
  When  user1 wants to rent the selected book1
  Then  the selected book1 is rent to the user1
    And the book1 is added to the users1 rent list
    And user1 rent counter is incremented
    And book1 return date is set to 14 days

Scenario: rent failed - rent limit exceeded
  Given user2 rent counter is equal 5
    And user2 BookStore Card is valid
    And the selected book2 is available
  When  user2 wants to rent the selected book2
  Then  the selected book2 is NOT rent to the user2
    And the book2 is NOT added to the users2 rent list
    And alert info is displayed to user2
    And user2 rent counter is NOT incremented


Scenario: rent failed - invalid BookStore Card
  Given user3 rent counter is equal 0
    And user3 BookStore Card is NOT valid
    And the selected book3 is available
  When  user3 wants to rent the selected book3
  Then  the selected book3 is NOT rent to the user3
    And the book3 is NOT added to the users3 rent list
    And alert info is displayed to user3
    And user3 rent counter is NOT incremented
