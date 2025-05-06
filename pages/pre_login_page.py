from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.pre_login_locators import PreLoginLocators as Loc


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

    def select_country(self, country_name):
        self.driver.find_element(*Loc.SELECT_PLACEHOLDER).click()
        country_option = self.wait.until(EC.visibility_of_element_located(Loc.COUNTRY_OPTION(country_name)))
        country_option.click()

    def select_language(self, language):
        trigger = self.wait.until(EC.element_to_be_clickable(Loc.LANGUAGE_TRIGGER(language)))
        trigger.click()
        option = self.wait.until(EC.visibility_of_element_located(Loc.LANGUAGE_OPTION(language)))
        option.click()

    def continue_to_login(self):
        continue_btn = self.wait.until(EC.element_to_be_clickable(Loc.CONTINUE_BUTTON))
        continue_btn.click()
