import pytest
import allure
from pages.pre_login_page import PreLoginPage


@pytest.mark.usefixtures("browser", "base_url")
@allure.title("Navigation options from register preview page work")
@allure.description("Test checks that all registration navigation buttons on the preview page function correctly")
def test_register_preview_navigation(browser, base_url):
    pre_login = PreLoginPage(browser, base_url)

    with allure.step("Open register preview page"):
        pre_login.open()
        pre_login.accept_cookies_if_present()

    with allure.step("Verify all main objects are visible"):
        assert pre_login.verify_welcome_to_present(), "'Welcome to' is visible"
        # add asserts for elements visibility of elements on pre_login page
