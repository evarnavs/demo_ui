from selenium.webdriver.common.by import By


class PreLoginLocators:
    ACCEPT_COOKIES_BTN = (By.XPATH, "//div[@class='btn__content-container' and text()='Save']")
    SELECT_PLACEHOLDER = (By.XPATH, "//p[@class='text placeholder' and text()='Select']")
    COUNTRY_OPTION = lambda country: (By.XPATH, f"//p[@role='link' and contains(@class, 'dropdown-content__single-option') and text()='{country}']")
    LANGUAGE_TRIGGER = lambda language: (By.XPATH, f"//p[contains(@class, 'text') and contains(text(), '{language}')]")
    LANGUAGE_OPTION = lambda language: (By.XPATH, f"//p[@role='link' and contains(@class, 'dropdown-content__single-option') and contains(text(), '{language}')]")
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(., 'Continue')]")
