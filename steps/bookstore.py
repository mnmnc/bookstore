__author__ = 'Dawid'

from behave import *
import user
import book


# Scenario: rent successful
user1 = user.User("Jan Kowalsky")
book1 = book.Book("Pan Tadeusz", "Mickiewicz")

@given('user1 rent counter is equal 0')
def step_impl(context):
    user1.rent_counter = 0
@given('user1 BookStore Card is valid')
def step_impl(context):
    user1.card_valid = True
@given('the selected book1 is available')
def step_impl(context):
    book1.available = True

@when('user1 wants to rent the selected book1')
def step_impl(context):
    assert True is not False

@then('the selected book1 is rent to the user1')
def step_impl(context):
    user1.rent_book(book1)
@then('the book1 is added to the users1 rent list')
def step_impl(context):
    assert book1 in user1.book_list
@then('user1 rent counter is incremented')
def step_impl(context):
    assert user1.rent_counter == 1
@then('book1 return date is set to 14 days')
def step_impl(context):
    assert book1.return_date == 14


# Scenario: rent failed - rent limit exceeded
user2 = user.User("Anna Nowak")
book2 = book.Book("Balladyna", "Slowacki")

@given('user2 rent counter is equal 5')
def step_impl(context):
    user2.rent_counter = 5
@given('user2 BookStore Card is valid')
def step_impl(context):
    user2.card_valid = True
@given('the selected book2 is available')
def step_impl(context):
    book2.available = True

@when('user2 wants to rent the selected book2')
def step_impl(context):
    assert True is not False

@then('the selected book2 is NOT rent to the user2')
def step_impl(context):
    user2.rent_book(book2)
@then('the book2 is NOT added to the users2 rent list')
def step_impl(context):
    assert book2 not in user2.book_list
@then('alert info is displayed to user2')
def step_impl(context):
    pass
@then('user2 rent counter is NOT incremented')
def step_impl(context):
    assert user2.rent_counter == 5


# Scenario: rent failed - invalid BookStore Card
user3 = user.User("Piotr Stonoga")
book3 = book.Book("Thinking in Java", "Eckel")

@given('user3 rent counter is equal 0')
def step_impl(context):
    user3.rent_counter = 0
@given('user3 BookStore Card is NOT valid')
def step_impl(context):
    user3.card_valid = False
@given('the selected book3 is available')
def step_impl(context):
    book3.available = True

@when('user3 wants to rent the selected book3')
def step_impl(context):
    assert True is not False

@then('the selected book3 is NOT rent to the user3')
def step_impl(context):
    user3.rent_book(book3)
@then('the book3 is NOT added to the users3 rent list')
def step_impl(context):
    assert book3 not in user3.book_list
@then('alert info is displayed to user3')
def step_impl(context):
    pass
@then('user3 rent counter is NOT incremented')
def step_impl(context):
    assert user3.rent_counter == 0
