# Flow: Create Account -> new user credentials -> Verify -> Login [not the invitation method]

import random
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from test_cases.conftest import setup
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from page_objects.gmail_login_verifier_page import GoogleLoginVerifier
from page_objects.login_page import HubLogin
from page_objects.create_account_page import CreateAccount
from page_objects.setup_company_page import SetupCompany
from utilities.mongo_utils import get_latest_user

@pytest.mark.usefixtures("setup")
class TestCreateAccount:
    driver: WebDriver
    wait: WebDriverWait

    logger = LogGen.loggen()  # Logger instance for logging test steps

    baseURL = ReadConfig.get_url()  # Get the login URL from config
    gmail_url = ReadConfig.get_google_url()
    gmail_email = ReadConfig.get_google_email()
    gmail_password = ReadConfig.get_google_pass()
    search_text = ReadConfig.get_search_text()
    first_name = ReadConfig.get_firstname()
    last_name = ReadConfig.get_lastname()

    user_password = ReadConfig.get_password()  # Retrieve user password from config
    user_email = ReadConfig.get_user_email()  # Retrieve user email from config

    company_name = ReadConfig.get_company_name()
    company_phone_no = ReadConfig.get_company_phone_no()

    @staticmethod
    def generate_test_email():
        prefix = ReadConfig.get_email_prefix()
        suffix = random.randint(10000, 99999)
        return f"{prefix}+{suffix}@gmail.com"

    def run_create_account_flow(self, setup):

        self.logger.info("=== Starting Create Account Test ===")
        self.create_account = CreateAccount(self.driver, self.wait)
        self.create_user_email = self.generate_test_email()


        # Step 1: Open the login page
        try:
            self.driver.get(self.baseURL)  # Load login page
        except WebDriverException as e:
            self.logger.error(f"***Failed to load URL: {self.baseURL}. Info: {str(e)}***")
            assert False, "***Test failed: Unable to load login page***"

        # Step 2: Account Creation for Login
        try:
            self.hub_login = HubLogin(self.driver, self.wait)
            self.hub_login.click_create_account_link()
            self.create_account.set_first_name(self.first_name)
            self.create_account.set_last_name(self.last_name)
            self.create_account.set_email(self.create_user_email)
            self.create_account.set_password(self.user_password)
            self.create_account.set_confirm_password(self.user_password)
            self.create_account.click_agree()
            self.create_account.click_register()
            try:
                toast_msg = self.create_account.get_toast_notification()
                assert toast_msg is not None, "No toast message received after company creation."
                expected_msg = "User has been registered successfully, Please verify your email to continue."
                assert expected_msg in toast_msg, f"Unexpected toast message: '{toast_msg}'"
                self.logger.info(f"Toast notification validated successfully: '{toast_msg}'")

            except AssertionError as ae:
                self.logger.error(f"Toast message assertion failed: {ae}")
                raise
            except Exception as e:
                self.logger.error(f"Unexpected error during toast message verification: {e}")
                assert False, f"Test Failed due to unexpected error: {e}"
            self.logger.info("Account created successfully.")

        except (TimeoutException, NoSuchElementException, WebDriverException) as e:
            self.logger.error(f"Account creation failed: {e}")
            assert False, "Test Failed: Account creation error."

        # Step 3:  Verification Process (Direct URL, no Gmail)
        try:
            # Fetch latest user from MongoDB
            user = get_latest_user()
            if not user:
                self.logger.error("No user found in MongoDB for verification.")
                assert False, "Test Failed: No user found in MongoDB."
            verification_url = f"http://localhost:4000/#/verify-email/{user['_id']}/{user.get('verificationToken')}"
            self.logger.info(f"Opening verification URL: {verification_url}")

            # Open verification URL in new tab
            existing_tabs = self.driver.window_handles
            self.driver.execute_script(f"window.open('{verification_url}', '_blank');")
            self.wait.until(lambda d: len(d.window_handles) > len(existing_tabs))
            new_tab_handle = [wh for wh in self.driver.window_handles if wh not in existing_tabs][0]
            self.driver.switch_to.window(new_tab_handle)
            self.logger.info(f"Switched to verification tab: {new_tab_handle}")

            self.wait.until(lambda d: d.title != "")
            self.logger.info(f"New page title: {self.driver.title}")

            # Toast message verification after email verification
            try:
                toast_msg = self.create_account.get_toast_notification()
                assert toast_msg is not None, "No toast message received after company creation."
                expected_msg = "Your email has been verify successfully"
                assert expected_msg in toast_msg, f"Unexpected toast message: '{toast_msg}'"
                self.logger.info(f"Toast notification validated successfully: '{toast_msg}'")
            except AssertionError as ae:
                self.logger.error(f"Toast message assertion failed: {ae}")
                raise
            except Exception as e:
                self.logger.error(f"Unexpected error during toast message verification: {e}")
                assert False, f"Test Failed due to unexpected error: {e}"
            self.logger.info("Account created successfully.")

        except Exception as e:
            self.logger.error(f"Unexpected error during direct verification: {e}")
            assert False, "Test Failed: Unknown error occurred during direct verification."

        # Step 6: Attempt System Login
        try:
            self.hub_login = HubLogin(self.driver, self.wait)
            self.hub_login.set_email(self.create_user_email)
            self.logger.info("Entered email for first login.")
            self.hub_login.set_password(self.user_password)
            self.logger.info("Entered password for first login.")
            self.hub_login.click_login()
            self.logger.info("First login attempt executed.")

            # Page title verification after login
            self.wait.until(lambda d: "Company Information" in d.title)
            assert "Alian Hub | Company Information" in self.driver.title, "Test Failed: Did not reach company info page after login."

        except (TimeoutException, NoSuchElementException, WebDriverException) as e:
            self.logger.error(f"Final login failed: {e}")
            assert False, "Test Failed: Final login error."

    def company_setup(self, setup):

        try:
            self.logger.info("=== Starting Setup Company Flow ===")

            # Step 1: Fill company details and submit
            try:
                self.setup_company = SetupCompany(self.driver, self.wait)
                self.setup_company.set_company_name(self.company_name)
                self.setup_company.set_mobile_number(self.company_phone_no)
                self.setup_company.click_country_field()
                self.setup_company.select_country_name()
                self.logger.info("Country selected")

                self.setup_company.click_state_field()
                self.setup_company.select_state_name()
                self.logger.info("State selected")

                # self.setup_company.click_city_field()
                self.logger.info("City list opened")
                self.setup_company.select_city_name()
                self.logger.info("City selected")
                self.setup_company.click_create_company()
                self.logger.info("Filled all company details and clicked create.")
            except Exception as e:
                self.logger.error(f"Failed to fill and submit company data: {e}")
                assert False, "Test Failed: Error during company info submission."

            # Step 2: Verify toast message
            try:
                toast_msg = self.create_account.get_toast_notification()
                assert toast_msg is not None, "No toast message received after company creation."
                expected_msg = "Company has been created Successfully."
                assert expected_msg in toast_msg, f"Unexpected toast message: '{toast_msg}'"
                self.logger.info(f"Toast notification validated successfully: '{toast_msg}'")

            except AssertionError as ae:
                self.logger.error(f"Toast message assertion failed: {ae}")
                raise
            except Exception as e:
                self.logger.error(f"Unexpected error during toast message verification: {e}")
                assert False, f"Test Failed due to unexpected error: {e}"

            # Step 3: Verify Company Name Displayed on Dashboard
            try:
                self.hub_login.click_alert()
                self.wait.until(lambda d: self.setup_company.get_company_name_dashboard() is not None)
                displayed_company_name = self.setup_company.get_company_name_dashboard()

                if displayed_company_name is None:
                    raise AssertionError("Company name element not found on dashboard.")

                assert displayed_company_name == self.company_name, (
                    f"Displayed company name mismatch: "
                    f"Expected '{self.company_name}', but got '{displayed_company_name}'."
                )

                self.logger.info(
                    f"Company name verified successfully on dashboard: '{displayed_company_name}'."
                )

            except Exception as e:
                self.logger.error(f"Company name verification on dashboard failed: {e}")
                assert False, "Test Failed: Company name not displayed correctly on dashboard."

        except Exception as e:
            self.logger.error(f"Test failed during setup_company flow: {e}")
            assert False, f"Test Failed: Exception in setup_company - {e}"

    def test_create_account(self, setup):
        """
        Master test function that calls each part of the account creation flow.
        """
        try:
            self.run_create_account_flow(setup)  # Step 1: Full registration + Gmail + verification
            self.company_setup(setup)  # Step 2: Setup company & verify dashboard
        except Exception as e:
            self.logger.error(f"Test failed during test_create_account flow: {e}")
            assert False, f"Test Failed: Exception in test_create_account - {e}"