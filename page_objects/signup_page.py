#After verification sign up page step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Signup:
    firstname_id = "firstName"
    lastname_id = "lastName"
    password_id = "password"
    confirm_password_id = "confirmPassword"
    agree_btn_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[4]/label/span"
    register_btn_xpath = "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[5]/button"

    def __init__(self, driver):
        self.driver = driver
        self.wait = driver.wait

    def set_firstname(self, firstname):
         first_name = self.wait.until(
            EC.presence_of_element_located((By.ID, self.firstname_id))
         )
         first_name.send_keys(firstname)

    def set_lastname(self, lastname):
         last_name = self.wait.until(
            EC.presence_of_element_located((By.ID, self.lastname_id))
         )
         last_name.send_keys(lastname)

    def set_password(self, email_password):
        password_input = self.wait.until(
            EC.presence_of_element_located((By.ID, self.password_id))
        )
        password_input.send_keys(email_password)

    def set_confirm_password(self, email_password):
        conf_password_input = self.wait.until(
            EC.presence_of_element_located((By.ID, self.confirm_password_id))
        )
        conf_password_input.send_keys(email_password)

    def click_agree(self):
        agree_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.agree_btn_xpath))
        )
        agree_button.click()

    def click_register(self):
        register_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.register_btn_xpath))
        )
        register_button.click()