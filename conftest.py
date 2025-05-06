import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()

def is_ci_environment():
    return os.getenv("CI") == "true" or os.getenv("GITHUB_ACTIONS") == "true"

@pytest.fixture(scope="session")
def browser():
    chrome_options = Options()

    if is_ci_environment():
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")
