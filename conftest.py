import json
import os
from dotenv import load_dotenv

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import Login
from utils.screenshot_utility import take_screenshot

load_dotenv()
def pytest_addoption(parser):
    parser.addoption("--browser_name",action="store",default = "chrome",help="Browser selection at run time")

@pytest.fixture()
def driver(request):
    global driver
    browser = request.config.getoption("--browser_name")
    if browser == "chrome":
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("prefs",{
            "credentials_enable_service":False,
            "profile.password_manager_enabled":False,
            "profile.password_manager_leak_detection":False
        })
        driver = webdriver.Chrome(options=opt)
    elif browser == "firefox":
         firefox_driver_path = Service(r"C:\Users\Lenovo\Selenium_POM_Git\drivers\geckodriver_win64\geckodriver.exe")
         driver = webdriver.Firefox(service=firefox_driver_path)
    elif browser == "edge":
        edge_driver_path = Service(r"C:\Users\Lenovo\Selenium_POM_Git\drivers\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=edge_driver_path)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def baseurl():
    return os.getenv("BASE_URL")

@pytest.fixture()
def credentials():
    return {
        "username": os.getenv("USER_NAME"),
        "password": os.getenv("PASSWORD")
    }

@pytest.fixture
def product_cart(driver,baseurl,credentials):
    login = Login(driver)
    login.site_load(baseurl)
    product_cart = login.login(credentials["username"], credentials["password"])
    yield product_cart

@pytest.fixture()
def your_cart(product_cart,json_dataextraction):
    product_cart.add_product_toCart(json_dataextraction[0]["items"])
    product_cart.product_count_validation()
    your_cart = product_cart.navigate_toCart()
    return your_cart

@pytest.fixture()
def your_info(your_cart,json_dataextraction):
    your_cart.cart_item_validation(json_dataextraction[0]["items"])
    your_info = your_cart.cart_checkout()
    return your_info

@pytest.fixture()
def overview(your_info):
    your_info.fill_yourDetails("Sourav", "Mohanty", "560035")
    overview = your_info.click_Continue()
    return overview

@pytest.fixture()
def json_dataextraction():
    filePath = r"C:\Users\Lenovo\Selenium_POM\data\test_data.json"
    with open(filePath) as file:
        test_data = json.load(file)
        data_list = test_data["data"]
        return data_list

@pytest.fixture()
def user_details():
    return {
              "first_name":os.getenv("FIRST_NAME"),
              "last_name":os.getenv("LAST_NAME"),
              "zip_code":os.getenv("ZIP_CODE")
    }
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            take_screenshot(driver,f"FAILED_{item.name}")

@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    global filepath
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            driver = item.funcargs.get("driver")
            if driver:
                filepath = take_screenshot(driver, f"FAILED_{file_name}")
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra