# Login User TCs

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from page_objects.login_page import HubLogin
from test_cases.conftest import setup
from test_cases.login_manager import LoginManager

@pytest.mark.usefixtures("setup")
class TestLogin001:
    driver: WebDriver
    wait: WebDriverWait

    logger = LogGen.loggen()  # Logger instance for logging test steps
    baseURL = ReadConfig.get_url()  # Get the login URL from config
    user_password = ReadConfig.get_password()  # Retrieve user password from config
    user_email = ReadConfig.get_user_email()  # Retrieve user email from config
    wrong_user_email = ReadConfig.get_wrong_email()  # Retrieve incorrect email for negative test cases
    wrong_password = ReadConfig.get_wrong_password()  # Retrieve incorrect password for negative test cases

    def test_login(self):
        """Test valid login scenario"""
        login_manager = LoginManager(self.driver, self.wait)  # Initialize LoginManager
        login_manager.login()  # Perform successful login test case

    def test_wrong_email(self, setup):
        """Test login failure due to incorrect email"""
        self.driver = setup
        self.logger.info("***Test_Login_002***")  # Log test case start

        # Step 1: Open the login page
        try:
            self.driver.get(self.baseURL)  # Load login page
        except WebDriverException as e:
            self.logger.error(f"***Failed to load URL: {self.baseURL}. Info: {str(e)}***")
            assert False, "***Test failed: Unable to load login page***"

        try:
            self.hub_login = HubLogin(self.driver, self.wait)  # Initialize login page object

            # Step 2: Click login first without entering anything (to check inline validation)
            self.hub_login.click_login()
            self.logger.info("***Clicked Login Without Email id***")

            error_messages = []

            try:
                email_empty_error = self.hub_login.get_error_empty_email()
                if email_empty_error:
                    error_messages.append(email_empty_error)
            except TimeoutException:
                self.logger.info("***No inline email validation error detected***")

            # Step 3: Enter incorrect email and try again
            self.hub_login.set_email(self.wrong_user_email)  # Enter incorrect email
            self.hub_login.set_password(self.user_password)
            self.logger.info("***Wrong Email Given***")
            self.hub_login.click_login()

            # Step 4: Capture error messages after entering incorrect email
            try:
                wrong_email_error = self.hub_login.get_error_wrong_email()
                if wrong_email_error:
                    error_messages.append(wrong_email_error)
            except TimeoutException:
                self.logger.info("***No toast notification detected***")

            # Step 5: Validate the captured error messages
            expected_messages = {
                "Your email is invalid. Please check and try again",
                "Too many requests. Please try again later",
                "The email field is required"
            }

            if error_messages:
                for msg in error_messages:
                    assert msg in expected_messages, f"Test Failed: Unexpected error message: '{msg}'"
                self.logger.info(f"***Test Passed: Correct error messages displayed -> {error_messages}***")
            else:
                self.logger.error("***Test Failed: No error message appeared***")
                assert False, "***Test Failed: No error message appeared***"

        except Exception as e:
            self.logger.error(f"***Test Execution Failed: {str(e)}***")
            assert False, "***Test Execution Failed***"

    def test_wrong_password(self, setup):
        """Test login failure due to incorrect password"""
        self.driver = setup
        self.logger.info("***Test_Login_003***")  # Log test case start

        # Step 1: Open the login page
        try:
            self.driver.get(self.baseURL)  # Load login page
        except WebDriverException as e:
            self.logger.error(f"***Failed to load URL: {self.baseURL}. Info: {str(e)}***")
            assert False, "***Test failed: Unable to load login page***"

        try:
            self.hub_login = HubLogin(self.driver, self.wait)  # Initialize login page object

            # Step 2: Click login first without entering anything (to check inline validation)
            self.hub_login.click_login()
            self.logger.info("***Clicked Login Without Password***")

            error_messages = []

            try:
                password_empty_error = self.hub_login.get_error_empty_password()
                if password_empty_error:
                    error_messages.append(password_empty_error)
            except TimeoutException:
                self.logger.info("***No inline password validation error detected***")

            # Step 3: Enter incorrect password and try again
            self.hub_login.set_email(self.user_email)  # Enter valid email
            self.hub_login.set_password(self.wrong_password)  # Enter incorrect password
            self.logger.info("***Wrong Password Given***")
            self.hub_login.click_login()

            # Step 4: Capture error messages after entering incorrect password
            try:
                password_wrong_error = self.hub_login.get_error_wrong_password()
                if password_wrong_error:
                    error_messages.append(password_wrong_error)
            except TimeoutException:
                self.logger.info("***No toast notification detected***")

            # Step 5: Validate the captured error messages
            expected_messages = {
                "Your password is invalid. Please check and try again",
                "Too many requests. Please try again later",
                "The password field is required"
            }

            if error_messages:
                for msg in error_messages:
                    assert msg in expected_messages, f"Test Failed: Unexpected error message: '{msg}'"
                self.logger.info(f"***Test Passed: Correct error messages displayed -> {error_messages}***")
            else:
                self.logger.error("***Test Failed: No error message appeared***")
                assert False, "***Test Failed: No error message appeared***"

        except Exception as e:
            self.logger.error(f"***Test Execution Failed: {str(e)}***")
            assert False, "***Test Execution Failed***"

    #Too many times wrong login error check
    def test_wrong_credentials_too_many_attempts(self, setup):
        """Test login failure due to incorrect email and password multiple times until lockout."""
        self.driver = setup
        self.logger.info("***Test_Login_004***")

        try:
            self.driver.get(self.baseURL)  # Assumes baseURL is set elsewhere
        except WebDriverException as e:
            self.logger.error(f"***Failed to load URL: {self.baseURL}. Info: {str(e)}***")
            pytest.fail("***Test failed: Unable to load login page***")

        try:
            self.hub_login = HubLogin(self.driver, self.wait)
            expected_errors = {
                "Your email is invalid. Please check and try again",
                "Too many requests. Please try again later"
            }
            max_attempts = 10
            lockout_detected = False

            for attempt in range(1, max_attempts + 1):
                self.logger.info(f"***Attempt {attempt}: Entering wrong credentials***")
                # self.driver.refresh()

                # Custom interactability check for email field within the function
                try:
                    email_field = self.wait.until(
                        lambda driver: (
                            element := driver.find_element(By.XPATH, self.hub_login.textbox_email_xpath),
                            element.is_displayed() and
                            element.is_enabled() and
                            driver.execute_script("return window.getComputedStyle(arguments[0]).pointerEvents !== 'none';", element) and
                            (element.clear() or True)  # Test clear; 'or True' ensures it doesn't fail the lambda
                        ) and element
                    )
                    email_field.send_keys(self.wrong_user_email)
                except TimeoutException:
                    self.logger.error("***Email field not fully interactable after 10 seconds***")
                    pytest.fail("***Test Failed: Email field not interactable***")

                # Set password and click login using HubLogin methods
                self.hub_login.set_password(self.wrong_password)
                self.hub_login.click_login()

                # Check for error messages
                login_error = None
                try:
                    # Prioritize lockout check first
                    if "Too many requests" in self.driver.page_source:
                        login_error = "Too many requests. Please try again later"
                    else:
                        login_error = self.hub_login.get_error_wrong_email().strip() or self.hub_login.get_error_wrong_password().strip()
                except TimeoutException:
                    pass

                if login_error:
                    self.logger.info(f"***Received Error: {login_error}***")
                    if login_error not in expected_errors:
                        self.logger.error(f"***Unexpected error message: {login_error}***")
                        pytest.fail(f"***Test Failed: Unexpected error message: {login_error}***")
                    if login_error == "Too many requests. Please try again later":
                        self.logger.info("***Too many requests error detected, stopping test early***")
                        lockout_detected = True
                        break
                self.driver.refresh()
            if lockout_detected:
                self.logger.info("***Test Passed: Too many requests error appeared within 10 attempts***")
            else:
                self.logger.error("***Test Failed: Lockout not triggered within 10 attempts***")
                pytest.fail("***Test Failed: Lockout not triggered within 10 attempts***")

        except Exception as e:
            self.logger.error(f"***Test Execution Failed: {str(e)}***")
            pytest.fail("***Test Execution Failed***")

    #All wrong credentials
    def test_wrong_credentials(self, setup):
        """Test login failure due to incorrect email & password"""
        self.driver = setup
        self.logger.info("***Test_Login_005***")  # Log test case start

        # Step 1: Open the login page
        try:
            self.driver.get(self.baseURL)  # Load login page
        except WebDriverException as e:
            self.logger.error(f"***Failed to load URL: {self.baseURL}. Info: {str(e)}***")
            assert False, "***Test failed: Unable to load login page***"

        try:
            self.hub_login = HubLogin(self.driver, self.wait)  # Initialize login page object

            # Step 2: Click login first without entering anything (to check inline validation)
            self.hub_login.click_login()
            self.logger.info("***Clicked Login Without Email id***")

            error_messages = []

            try:
                email_empty_error = self.hub_login.get_error_empty_email()
                if email_empty_error:
                    error_messages.append(email_empty_error)
            except TimeoutException:
                self.logger.info("***No inline email validation error detected***")

            # Step 3: Enter incorrect email and try again
            self.hub_login.set_email(self.wrong_user_email)  # Enter incorrect email
            self.hub_login.set_password(self.wrong_password)  # Enter incorrect password
            self.logger.info("***Wrong Email & Password Given***")
            self.hub_login.click_login()

            # Step 4: Capture error message
            try:
                wrong_email_error = self.hub_login.get_error_wrong_email()
                if wrong_email_error:
                    error_messages.append(wrong_email_error)
            except TimeoutException:
                self.logger.info("***No toast notification detected***")

            # Step 5: Validate the captured error message
            expected_messages = {
                "Your email is invalid. Please check and try again",
                "Too many requests. Please try again later",
                "The email field is required"
            }

            if error_messages:
                for msg in error_messages:
                    assert msg in expected_messages, f"Test Failed: Unexpected error message: '{msg}'"
                self.logger.info(f"***Test Passed: Correct error messages displayed -> {error_messages}***")
            else:
                self.logger.error("***Test Failed: No error message appeared***")
                assert False, "***Test Failed: No error message appeared***"

        except Exception as e:
            self.logger.error(f"***Test Execution Failed: {str(e)}***")
            assert False, "***Test Execution Failed***"

    def test_remember_me(self, setup):
        self.logger.info("***Test_Login_006***")
        self.user_email = ReadConfig.get_user_email()
        """Test Remember Me functionality."""
        self.driver = setup
        self.logger.info("***Test_Remember_Me***")  # Log test case start

        try:
            # Step 1: Initialize login page object
            self.hub_login = HubLogin(self.driver, self.wait)

            # Step 2: Do Login
            login_manager = LoginManager(self.driver, self.wait)  # Initialize LoginManager
            login_manager.login()
            self.logger.info("***Login Successful***")

            # Step 3: Click on profile menu
            self.hub_login.click_profile_menu()
            self.logger.info("***Clicked Profile Menu***")

            # Step 4: Click on logout
            self.hub_login.click_logout()
            self.logger.info("***Clicked Logout***")
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # Step 5: Verify Remember Me functionality
            email_value = self.hub_login.get_email_value()  # Fetch pre-filled email from the login field
            assert email_value == self.user_email, "Test Failed: Remember Me did not retain email"
            self.logger.info("***Test Passed: Remember Me retained email***")

        except Exception as e:
            self.logger.error(f"***Test Execution Failed: {str(e)}***")
            assert False, "***Test Execution Failed***"

    def test_create_account_link(self,setup):
        self.driver = setup
        self.logger.info("***Test_Login_007***")

        try:
            self.driver.get(self.baseURL)
            # main_window = self.driver.current_window_handle
        except WebDriverException as e:
            self.logger.error(f"***Failed to load URL: {self.baseURL}. Info: {str(e)}***")
            pytest.fail("***Test failed: Unable to load login page***")

        try:
            # Step 1: Click on the Create Account link
            self.hub_login = HubLogin(self.driver, self.wait)
            self.hub_login.click_create_account_link()
            self.logger.info("***Clicked Create Account Link***")

            # Step 2: Switch to the newly opened tab
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # Step 3: Validate the Privacy Policy page title
            assert "Alian Hub | Register" in self.driver.title, "Test Failed: Create Account Page title mismatch."
            self.logger.info("***Create Account Page validated successfully.***")

            # Step 4: Switch back to the main window
            self.logger.info("***Switched back to Create Account page.***")

        except Exception as e:
            self.logger.error(f"***Create Account Page validation failed: {e}***")
            assert False, "Test Failed: Create Account Page validation error."