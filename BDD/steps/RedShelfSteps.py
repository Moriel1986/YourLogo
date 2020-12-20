from behave import given, when, then
from selenium import webdriver
from base import base_setup


@given(u'Launch FireFox Browser')
def LaunchBrowser(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://redshelf.com/")
    context.driver.maximize_window()
    context.driver.delete_all_cookies()
    context.driver.set_page_load_timeout(10)
    raise NotImplementedError(u'STEP: Given Launch FireFox Browser')


@when(u'User clicks loginBtn')
def Username(context):
    context.driver = webdriver.Firefox()
    context.driver.find_element_by_xpath("//a[@class='rs-navbar-nav-item-link']"
                                         "//span[@class='rs-navbar-nav-item-label'][text()='Log In']").click()


@when(u'User enters Username')
def Username(context):
    context.driver = webdriver.Firefox()
    context.driver.find_element_by_xpath("//input[@id='username']")

    raise NotImplementedError(u'STEP: When User enters Username')


@when(u'User enters Password')
def Password(context):
    context.driver = webdriver.Firefox()
    context.driver.find_element_by_xpath("//input[@id='password']")
    raise NotImplementedError(u'STEP: When User enters Password')


@when(u'User clicks login')
def Password(context):
    context.driver = webdriver.Firefox()
    context.driver.find_element_by_xpath("//button[@class='btn btn-primary form-control'][text()='Log In']")
    raise NotImplementedError(u'STEP: When User enters Password')


@then(u'User should see My Shelf in header one')
def VerifyFullName(context):
    context.driver = webdriver.Firefox()
    context.driver.quit()
    context.driver.title()
    if context.driver.title == "My Library RedShelf":
        print("Test is successful")
    else:
        print("Test Failed")
    raise NotImplementedError(u'STEP: Then User should see full name')


