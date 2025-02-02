import os

import pytest
driver = None
from selenium import webdriver

#command line option to run on different browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="To run the test on different browser"
    )

#Defined the scope to class level because this setup function has to execute once before the class execute

@pytest.fixture(scope="class")
def setup(request):#request instance is created
    global driver
    browser_name = request.config.getoption("browser_name") #To retrive command line option

    if browser_name == "chrome":
        driver = webdriver.Chrome() #Chrome Browser Innvocation

    elif browser_name == "firefox":
        driver = webdriver.Firefox() #Firefox Browswer Innvocation


    driver.get("https://test.fe.advanced-infrastructure.co.uk/map")
    driver.maximize_window()

    request.cls.driver = driver #Assigning fixture driver to class driver
    yield
    driver.close()

def take_screenshot(driver, name):
    """Helper function to take screenshots."""
    screenshots_dir = "Screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)  # Ensure directory exists
    screenshot_path = os.path.join(screenshots_dir, f"{name}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
