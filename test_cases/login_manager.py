#Login Helper file

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.common import WebDriverException, NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from utilities.read_properties import ReadConfig
from page_objects.login_page import HubLogin
from utilities.custom_logger import LogGen

class LoginManager:
    def __init__(self, driver: WebDriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = driver.wait
        """Initialize with WebDriver instance"""
        self.hub_login = None
        self.logger = LogGen.loggen()  # Logger instance for logging test steps
        self.baseURL = ReadConfig.get_url()  # Get the login URL from config
        self.user_password = ReadConfig.get_password()  # Retrieve user password from config
        self.user_email = ReadConfig.get_user_email()  # Retrieve user email from config
        self.wrong_user_email = ReadConfig.get_wrong_email()  # Retrieve incorrect email for negative test cases
        self.wrong_password = ReadConfig.get_wrong_password()  # Retrieve incorrect password for negative test cases

    # Log In
    def login(self):
        self.logger.info("***Test_Login_001***")  # Log test case start

        # Step 1: Load the login page
        try:
            self.driver.get(self.baseURL)  # Open the login page
        except WebDriverException as e:
            self.logger.error(f"***Failed to load URL: {self.baseURL}. Info: {str(e)}***")
            assert False, "***Test failed: Unable to load login page***"  # Fails test if page doesn't load

        try:
            self.hub_login = HubLogin(self.driver, self.wait)  # Initialize login page object
            self.hub_login.set_email(self.user_email)
            self.hub_login.set_password(self.user_password)
            self.hub_login.click_remember()  # Comment if needed
            self.hub_login.click_login()
            self.hub_login.click_alert()

            # Step 2: Wait for the page title to validate successful login
            expected_title = "Alian Hub | Home"
            WebDriverWait(self.driver, 10, poll_frequency=0.2).until(lambda driver: driver.title and driver.title != "")
            actual_title = self.driver.title
            assert actual_title == expected_title, (
                f"Test Failed: Expected title '{expected_title}', but got '{actual_title}'"
            )

            # Verify if login was successful by checking the title
            assert self.driver.title == expected_title, (
                f"Test Failed: Expected title '{expected_title}', but got '{self.driver.title}'"
            )

            self.logger.info("***Test Passed: Successfully signed into Alian Hub***")

        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"***Test Failed: Missing or unresponsive login elements. Info: {str(e)}***")
            assert False, "***Test Failed: Login elements missing or unresponsive***"

        except Exception as e:
            self.logger.error(f"***Unexpected error during login: {str(e)}***")
            assert False, "***Test Failed: Unexpected login issue***"