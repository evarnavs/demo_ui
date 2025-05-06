import os
import pytest
import allure
from pages.pre_login_page import PreLoginPage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("browser", "base_url")
@allure.title("Full login flow works")
@allure.description("Test checks that user can login after selecting country and language")
def test_full_login_flow(browser, base_url):
    # Load credentials from environment
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    if not email or not password:
        pytest.fail("EMAIL or PASSWORD environment variable is missing.")

    # Pre-login country/language selection
    pre_login = PreLoginPage(browser, base_url)
    pre_login.open()
    pre_login.accept_cookies_if_present()
    pre_login.select_country("Kazakhstan (Қазақстан)")
    pre_login.select_language("English")
    pre_login.continue_to_login()

    # Login
    login_page = LoginPage(browser)
    login_page.click_login_with_email_button()
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.submit()

    # Verification
    assert login_page.is_logged_in(), "Login verification failed."
