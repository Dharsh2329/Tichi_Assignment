from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    email_field = (By.ID, "email")
    password_field = (By.ID, "password")
    continue_btn = (By.XPATH, "/html/body/div[1]/div[2]/div/form/button")
    logout_btn = (By.XPATH, "/html/body/header/div/div[3]/div[3]/div/button")

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def login(self, email, password):
        self.enter_email(email)
        self.click_continue()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_field))
        self.enter_password(password)
        self.click_continue()

    def get_error(self):
        try:
            return self.driver.find_element(*self.error_msg).text
        except:
            return None

    def is_password_masked(self):
        field = self.driver.find_element(*self.password_field)
        return field.get_attribute("type") == "password"
