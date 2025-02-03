# from selenium import webdriver
# import pytest
#
#
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     return driver
#
#
# #
#
# def pytest_addoption(parser):  # it will get the value from CLI ?hooks
#     parser.addoption('--browser')
#
# #
# @pytest.fixture()
# def browser(request):  # this will return the Browser value to setup method
#     return request.config.getoption('--browser')
#
# # it is hook or adding environment info to html reposrt
# def pytest_config(config):
#     config.metadata['Project Name'] = 'Luma Ecommerce'
#     config.metadata['Module Name'] = 'Customer'
#     config.metadata['Tester'] = 'Prem s'

# from selenium import webdriver
import pytest
from selenium import webdriver


# Custom command-line argument to select the browser
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help="Choose browser: chrome or firefox")


# Fixture to return the browser value passed through the CLI
@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


# Setup WebDriver based on browser choice
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


# Adding metadata to the HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Luma Ecommerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Prem S'
