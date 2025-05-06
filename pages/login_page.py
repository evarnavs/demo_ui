import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators as Loc


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Click 'Login with Email' button")
    def click_login_with_email_button(self):
        self.wait.until(EC.element_to_be_clickable(Loc.LOGIN_WITH_EMAIL_BTN)).click()

    @allure.step("Enter email")
    def enter_email(self, email):
        email_field = self.wait.until(EC.presence_of_element_located(Loc.EMAIL_INPUT))
        email_field.send_keys(email)

    @allure.step("Enter password")
    def enter_password(self, password):
        password_field = self.wait.until(EC.presence_of_element_located(Loc.PASSWORD_INPUT))
        password_field.send_keys(password)

    @allure.step("Click 'Login' button ")
    def submit(self):
        self.wait.until(EC.element_to_be_clickable(Loc.LOGIN_BTN)).click()

    @allure.step("Check if user redirected to dashboard")
    def is_logged_in(self):
        self.wait.until(EC.url_contains("/dashboard"))
        return "/dashboard" in self.driver.current_url
