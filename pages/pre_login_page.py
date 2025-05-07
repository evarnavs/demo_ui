from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.pre_login_locators import PreLoginLocators as Loc
from selenium.common.exceptions import TimeoutException


class PreLoginPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get(self.base_url + "/client")

    def accept_cookies_if_present(self):
        try:
            accept_button = self.driver.find_element(*Loc.ACCEPT_COOKIES_BTN)
            accept_button.click()
        except Exception:
            pass

    def find_element(self, locator):
        """Wait for and return a visible element."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        """Click on an element after ensuring it is visible."""
        element = self.find_element(locator)
        element.click()

    def select_country(self, country_name):
        self.click_element(Loc.SELECT_PLACEHOLDER)
        self.click_element(Loc.COUNTRY_OPTION(country_name))

    def verify_welcome_to_present(self):
        """Return True if the country dropdown is visible, otherwise False."""
        try:
            self.find_element(Loc.WELCOME_TO)
            return True
        except TimeoutException:
            return False

    def select_language(self, language):
        trigger = self.wait.until(EC.element_to_be_clickable(Loc.LANGUAGE_TRIGGER(language)))
        trigger.click()
        option = self.wait.until(EC.visibility_of_element_located(Loc.LANGUAGE_OPTION(language)))
        option.click()

    def continue_to_login(self):
        continue_btn = self.wait.until(EC.element_to_be_clickable(Loc.CONTINUE_BUTTON))
        continue_btn.click()
