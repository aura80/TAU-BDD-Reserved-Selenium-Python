from functools import partial
import time

from pytest_bdd import scenarios, when, then, given, parsers
from utils.util import AddCart

# Scenarios
scenarios('../features/test_util_page.feature')

@given('open the register page')
def open_page(browser):
    util = AddCart(browser)
    util.load_page()

@when('adding sneakers to the cart')
def add_sneakers(browser):
    util = AddCart(browser)
    util.get_sneakers()

@when('finding the next picture')
def find_next(browser):
    util = AddCart(browser)
    util.get_next()

@when('accessing the menu')
def find_next(browser):
    util = AddCart(browser)
    util.get_color()
