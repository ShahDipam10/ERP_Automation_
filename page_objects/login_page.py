from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class HubLogin:
    """Class to handle login interactions on the Hub application."""

    def __init__(self, driver, wait):
        """Initialize HubLogin with WebDriver instance and explicit wait."""
        self.driver = driver
        self.wait = wait  # Using global wait from conftest.py

    # Locators for login elements
    textbox_email_xpath = "//*[@id='email']"
    textbox_password_xpath = "//*[@id='password']"
    remember_btn_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[3]/div/label/span"
    login_btn_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[4]/button"
    alert_no_btn = "//button[normalize-space()='No']"
    profile_menu_xpath="//*[@id= 'profile_menu']"
    logout_xpath = "//*[@id='dd_profile_menu']/div/div/div/div/div"
    create_account_link_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[5]/span/a"

    # Locators for error messages
    error_empty_email = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[1]/div"
    error_wrong_email = "//div[contains(@class, 'toast') or contains(text(), 'Your email is invalid')]"
    error_empty_password = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[2]/div"
    error_wrong_password = "//div[contains(@class, 'toast') or contains(text(), 'Your password is invalid')]"

    def set_email(self, email_id):
        """Enter email into the email input field."""
        email_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.textbox_email_xpath))
        )
        email_input.clear()
        email_input.send_keys(email_id)

    def set_password(self, email_password):
        """Enter password into the password input field."""
        password_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.textbox_password_xpath))
        )
        password_input.clear()
        password_input.send_keys(email_password)

    def click_remember(self):
        """Click the 'Remember Me' checkbox."""
        remember_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.remember_btn_xpath))
        )
        remember_button.click()

    def click_login(self):
        """Click the login button."""
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.login_btn_xpath))
        )
        login_button.click()

    def click_alert(self):
        """Click the 'No' button on an alert popup if it appears."""
        alert = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.alert_no_btn))
        )
        alert.click()

    def click_profile_menu(self):
        """Click the profile menu."""
        profile_menu = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.profile_menu_xpath))
        )
        profile_menu.click()

    def click_logout(self):
        """Click the logout button."""
        logout_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.logout_xpath))
        )
        logout_button.click()

    def get_error_empty_email(self):
        """Retrieve error message for empty email field."""
        error_empty_email = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.error_empty_email))
        )
        return error_empty_email.text

    def get_error_wrong_email(self):
        """Retrieve error message for incorrect email."""
        error_wrong_email = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.error_wrong_email))
        )
        return error_wrong_email.text

    def get_error_empty_password(self):
        """Retrieve error message for empty password field."""
        error_empty_password = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.error_empty_password))
        )
        return error_empty_password.text

    def get_error_wrong_password(self):
        """Retrieve error message for incorrect password."""
        error_wrong_password = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.error_wrong_password))
        )
        return error_wrong_password.text

    def get_email_value(self):
        """Retrieve the email input field value."""
        email = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.textbox_email_xpath))
        )
        return email.get_attribute("value")

    def click_create_account_link(self):
        """Click the Create Account link."""
        try:
            create_account_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.create_account_link_xpath))
            )
            create_account_link.click()
        except TimeoutException:
            print("Error: Create Account link not found.")