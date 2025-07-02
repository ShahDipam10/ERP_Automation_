from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class SetupCompany:

    def __init__(self, driver, wait):
        """Initialize SetupCompany with WebDriver instance and explicit wait."""
        self.driver = driver
        self.wait = wait  # Using global wait from conftest.py

    # Setup your company page locators
    company_name_xpath = "//*[@id='refCompanyName']"
    country_name_field_xpath = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/form/div[3]/input"
    country_name_xpath = "//*[@id='item100']"
    state_name_field_xpath = "//*[@id='refState']"
    state_name_xpath = "//*[@id='item10']"
    city_name_field_xpath = "//*[@id='refCity']"
    city_name_xpath = "//*[@id='item10']//span[contains(text(), 'Anand')]"
    mo_no_xpath = "//*[@id='inputId']"
    create_company_btn_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[5]/button"
    back_login_link_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[7]"
    company_created_notif_xpath = "(//div[@class='v-toast v-toast--top'])[1]"
    company_name_dashboard_xpath = "//*[@id='company_dropdown_driver']/div"

    # Error message locators
    company_name_error_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[1]/div"
    country_name_error_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[2]/div"
    state_name_error_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[3]/div[1]/div/div"
    city_name_error_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[3]/div[2]/div/div"
    mo_no_empty_error_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[4]/div[2]"
    mo_no_error_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[4]/div[3]"

    # Methods for company setup page interaction

    def set_company_name(self, company_name):
        """Enter the company name."""
        try:
            input_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.company_name_xpath)))
            input_field.clear()
            input_field.send_keys(company_name)
        except TimeoutException:
            print("Error: Company name input field not found.")

    def click_country_field(self):
        """Click on the country input field to activate dropdown."""
        try:
            country_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.country_name_field_xpath)))
            country_field.click()
        except TimeoutException:
            print("Error: Country input field not clickable.")

    def select_country_name(self):
        """Select a country from the dropdown after typing."""
        try:
            country_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.country_name_xpath)))
            country_option.click()
        except TimeoutException:
            print("Error: Country dropdown option not clickable.")

    def click_state_field(self):
        """Click on the state input field to activate dropdown."""
        try:
            state_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.state_name_field_xpath)))
            state_field.click()
        except TimeoutException:
            print("Error: State input field not clickable.")

    def select_state_name(self):
        """Select a state from the dropdown after typing."""
        try:
            state_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.state_name_xpath)))
            state_option.click()
        except TimeoutException:
            print("Error: State dropdown option not clickable.")

    def click_city_field(self):
        """Click on the city input field to activate dropdown."""
        try:
            city_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.city_name_field_xpath)))
            city_field.click()
        except TimeoutException:
            print("Error: City selection field not clickable.")

    def select_city_name(self):
        """Select a city from the dropdown."""
        try:
            city_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.city_name_xpath)))
            city_option.click()
        except TimeoutException:
            print("Error: City option not clickable.")

    def set_mobile_number(self, mobile_no):
        """Enter the mobile number."""
        try:
            mobile_input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.mo_no_xpath)))
            mobile_input.clear()
            mobile_input.send_keys(mobile_no)
        except TimeoutException:
            print("Error: Mobile number input field not found.")

    def click_create_company(self):
        """Click on the Create Company button."""
        try:
            create_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.create_company_btn_xpath)))
            create_btn.click()
        except TimeoutException:
            print("Error: Create Company button not clickable.")

    def click_back_to_login(self):
        """Click the Back to Login link."""
        try:
            back_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.back_login_link_xpath)))
            back_link.click()
        except TimeoutException:
            print("Error: Back to Login link not clickable.")

    def get_company_created_notification(self):
        """Wait for and return the toast notification text after creating company."""
        try:
            notif = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.company_created_notif_xpath)))
            text = self.driver.execute_script("return arguments[0].innerText;", notif).strip()
            if text:
                return text
            else:
                print("Error: Notification element found but text is empty.")
                return None
        except TimeoutException:
            print("Error: Company creation notification not found (Timeout).")
            return None
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            return None

    def get_company_name(self):
        """Get the value entered in the company name field."""
        try:
            company_name = self.wait.until(EC.presence_of_element_located((By.XPATH, self.company_name_xpath)))
            return company_name.get_attribute("value").strip()
        except (NoSuchElementException, TimeoutException):
            print("Error: Company name input field not found.")
            return None

    def get_city_name(self):
        """Get the value entered in the city field."""
        try:
            city_name = self.wait.until(EC.presence_of_element_located((By.XPATH, self.city_name_xpath)))
            return city_name.get_attribute("value").strip()
        except (NoSuchElementException, TimeoutException):
            print("Error: City input field not found.")
            return None

    def get_mobile_number(self):
        """Get the value entered in the mobile number field."""
        try:
            mobile_input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.mo_no_xpath)))
            return mobile_input.get_attribute("value").strip()
        except (NoSuchElementException, TimeoutException):
            print("Error: Mobile number input field not found.")
            return None

    # Methods to get error messages for validations
    def get_company_name_error(self):
        try:
            error = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.company_name_error_xpath)))
            return error.text.strip()
        except (NoSuchElementException, TimeoutException):
            return None

    def get_country_name_error(self):
        try:
            error = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.country_name_error_xpath)))
            return error.text.strip()
        except (NoSuchElementException, TimeoutException):
            return None

    def get_state_name_error(self):
        try:
            error = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.state_name_error_xpath)))
            return error.text.strip()
        except (NoSuchElementException, TimeoutException):
            return None

    def get_city_name_error(self):
        try:
            error = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.city_name_error_xpath)))
            return error.text.strip()
        except (NoSuchElementException, TimeoutException):
            return None

    def get_mobile_empty_error(self):
        try:
            error = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.mo_no_empty_error_xpath)))
            return error.text.strip()
        except (NoSuchElementException, TimeoutException):
            return None

    def get_mobile_invalid_error(self):
        try:
            error = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.mo_no_error_xpath)))
            return error.text.strip()
        except (NoSuchElementException, TimeoutException):
            return None

    def get_company_name_dashboard(self):
        """Get the company name shown in the dashboard dropdown."""
        try:
            company_name = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.company_name_dashboard_xpath)))
            return company_name.text.strip()
        except (NoSuchElementException, TimeoutException):
            return None
