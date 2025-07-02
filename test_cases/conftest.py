from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture()
def setup(request, browser):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')

    if browser == 'chrome':
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome(options=options)

    driver.maximize_window()

    # Attach driver and explicit wait to the test class (for pytest classes)
    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 60)  # You can adjust wait time as needed

    # Attach a global explicit wait to the driver
    driver.wait = WebDriverWait(driver, 50)

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption('--mybrowser', action='store', default='chrome', help='Browser to run tests')

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
