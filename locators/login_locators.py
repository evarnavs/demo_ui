from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_WITH_EMAIL_BTN = (By.XPATH, "//div[@class='btn__content-container' and contains(text(), 'Login with Email/Access Token')]")
    EMAIL_INPUT = (By.XPATH, "//input[@type='text' and @placeholder='Enter you email or access token']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @placeholder='Enter your password']")
    LOGIN_BTN = (By.XPATH, "//div[@class='btn__content-container' and text()='Login']")
