from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class CreateAccount:
    """Class to handle account creation interactions on the Hub application."""

    def __init__(self, driver, wait):
        """Initialize CreateAccount with WebDriver instance and explicit wait."""
        self.driver = driver
        self.wait = wait  # Using global wait from conftest.py

    # Locators
    first_name_id = "firstName"
    last_name_id = "lastName"
    textbox_email_xpath = "//*[@id='inputId']"
    password_id = "password"
    confirm_password_id = "confirmPassword"
    agree_btn_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[4]/label/span"
    register_btn_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[5]/button"
    terms_link_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[4]/label/span/a[1]"
    privacy_link_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[4]/label/span/a[2]"
    login_link_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[6]/span/a"
    toast_notif_xpath = "(//div[@class='v-toast v-toast--top'])[1]"
    link_expiry_xpath = "(//div[@class='v-toast v-toast--top'])[1]"

    # Error locators
    first_name_error_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[1]/div[1]/div/div"
    last_name_error_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div"
    password_error_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[3]/div[1]/div/div"
    confirm_password_error_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[3]/div[2]/div/div"
    agree_checkbox_error_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[4]/div"

    # Input Methods
    def set_first_name(self, first_name):
        try:
            field = self.wait.until(EC.presence_of_element_located((By.ID, self.first_name_id)))
            field.clear()
            field.send_keys(first_name)
        except TimeoutException:
            print("Error: First name input field not found.")

    def set_last_name(self, last_name):
        try:
            field = self.wait.until(EC.presence_of_element_located((By.ID, self.last_name_id)))
            field.clear()
            field.send_keys(last_name)
        except TimeoutException:
            print("Error: Last name input field not found.")

    def set_email(self, email_id):
        try:
            field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_email_xpath)))
            field.clear()
            field.send_keys(email_id)
        except TimeoutException:
            print("Error: Email input field not found.")

    def set_password(self, password):
        try:
            field = self.wait.until(EC.presence_of_element_located((By.ID, self.password_id)))
            field.clear()
            field.send_keys(password)
        except TimeoutException:
            print("Error: Password input field not found.")

    def set_confirm_password(self, confirm_password):
        try:
            field = self.wait.until(EC.presence_of_element_located((By.ID, self.confirm_password_id)))
            field.clear()
            field.send_keys(confirm_password)
        except TimeoutException:
            print("Error: Confirm password input field not found.")

    def click_agree(self):
        try:
            checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.agree_btn_xpath)))
            checkbox.click()
        except TimeoutException:
            print("Error: 'Agree to Terms' checkbox not clickable.")

    def click_register(self):
        try:
            button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.register_btn_xpath)))
            button.click()
        except TimeoutException:
            print("Error: Register button not clickable.")

    def get_link_expiry_error(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.link_expiry_xpath)))
            if element.is_displayed():
                return element.text.strip()
        except (NoSuchElementException, TimeoutException):
            return None

    # Navigation Link Clicks
    def click_terms_link(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.terms_link_xpath))).click()
        except TimeoutException:
            print("Error: Terms & Conditions link not found.")

    def click_privacy_link(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.privacy_link_xpath))).click()
        except TimeoutException:
            print("Error: Privacy Policy link not found.")

    def click_login_link(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_link_xpath))).click()
        except TimeoutException:
            print("Error: Login link not found.")

    # Error Text Retrieval
    def get_first_name_error(self):
        return self._get_error_text(self.first_name_error_xpath, "First name")

    def get_last_name_error(self):
        return self._get_error_text(self.last_name_error_xpath, "Last name")

    def get_password_error(self):
        return self._get_error_text(self.password_error_xpath, "Password")

    def get_confirm_password_error(self):
        return self._get_error_text(self.confirm_password_error_xpath, "Confirm password")

    def get_agree_checkbox_error(self):
        return self._get_error_text(self.agree_checkbox_error_xpath, "Agree checkbox")

    def _get_error_text(self, xpath, field_name):
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return element.text
        except (NoSuchElementException, TimeoutException):
            print(f"Error: {field_name} error message not found.")
            return None

    # Field Value Retrieval
    def get_first_name(self):
        return self._get_field_value(By.ID, self.first_name_id, "First name")

    def get_last_name(self):
        return self._get_field_value(By.ID, self.last_name_id, "Last name")

    def get_password(self):
        return self._get_field_value(By.ID, self.password_id, "Password")

    def get_confirm_password(self):
        return self._get_field_value(By.ID, self.confirm_password_id, "Confirm password")

    def get_agree_checkbox(self):
        try:
            checkbox = self.wait.until(EC.presence_of_element_located((By.XPATH, self.agree_btn_xpath)))
            return checkbox.is_selected()
        except (NoSuchElementException, TimeoutException):
            print("Error: 'Agree to Terms' checkbox not found.")
            return None

    def _get_field_value(self, by, locator, field_name):
        try:
            field = self.wait.until(EC.presence_of_element_located((by, locator)))
            return field.get_attribute("value")
        except (NoSuchElementException, TimeoutException):
            print(f"Error: {field_name} input field not found.")
            return None

    def get_toast_notification(self):
        """Wait for and return the toast notification text."""
        try:
            toast = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.toast_notif_xpath)))
            self.wait.until(lambda driver: toast.text.strip() != "")
            return toast.text.strip()
        except (TimeoutException, NoSuchElementException):
            print("Toast notification not found or not visible.")
            return None
