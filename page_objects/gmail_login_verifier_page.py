from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from utilities.custom_logger import LogGen


class GoogleLoginVerifier:
    """Class to handle Google login and email verification interactions using Selenium."""

    logger = LogGen.loggen()

    def __init__(self, driver, wait):
        """Initialize with WebDriver instance and explicit wait."""
        self.driver = driver
        self.wait = wait  # Using global wait from conftest.py

    # Locators for login elements
    textbox_email_id = "identifierId"  # Email input field ID
    nextBtn_xpath = "//*[@id='identifierNext']/div/button/span"  # Next button after entering email

    textbox_password_xpath = "//*[@id='password']/div[1]/div/div[1]/input[1]"  # Password input field XPATH
    loginBtn_xpath = "//*[@id='passwordNext']/div/button[1]"  # Login button XPATH

    # Locators for email verification elements
    searchbar_xpath = "//*[@id='gs_lc50']/input[1]"  # Search bar for finding emails
    search_btn = "//*[@id='aso_search_form_anchor']/button[4]"  # Search button

    first_email_xpath = "//tr[contains(@class, 'zA')]/td[6]/div/div/div[2]"  # First email in the inbox
    verify_link_xpath = "//a[contains(@href, 'localhost')]"  # Verification link

    def set_email(self, email_id):
        """Enter email into the email input field."""
        email_input = self.wait.until(
            EC.presence_of_element_located((By.ID, self.textbox_email_id))
        )
        email_input.send_keys(email_id)

    def click_next(self):
        """Click the 'Next' button after entering the email."""
        next_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.nextBtn_xpath))
        )
        next_button.click()

    def set_password(self, email_password):
        """Enter password into the password input field."""
        password_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.textbox_password_xpath))
        )
        password_input.send_keys(email_password)

    def click_login(self):
        """Click the 'Login' button after entering the password."""
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.loginBtn_xpath))
        )
        login_button.click()

    def search_email(self, search_txt):
        """Enter the search text into the email search bar."""
        search_email = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.searchbar_xpath))
        )
        search_email.send_keys(search_txt)

    def click_search(self):
        """Click the search button to find the email."""
        search_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.search_btn))
        )
        search_button.click()

    def open_email(self):
        """Open the first email in the inbox after search results load."""
        first_email = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.first_email_xpath))
        )
        first_email.click()

    def verification_link(self):
        """Click the verification link inside the email without using time.sleep()."""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # Always re-fetch the element
                verify_link = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, self.verify_link_xpath))
                )
                verify_link.click()
                self.logger.info("Clicked verification link.")
                return
            except StaleElementReferenceException:
                self.logger.warning(f"[Retry {attempt + 1}] Stale element encountered, re-waiting...")
                continue
            except TimeoutException:
                self.logger.error("Timeout: Verification link not clickable.")
                raise AssertionError("Test Failed: Verification link not clickable within timeout.")
            except Exception as e:
                self.logger.error(f"Unexpected error clicking verification link: {e}")
                raise AssertionError(f"Test Failed: Could not click verification link. Reason: {e}")

        raise AssertionError("Test Failed: Verification link kept going stale after multiple retries.")
