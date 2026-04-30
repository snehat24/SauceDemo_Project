import pytest

from utils.logger import logger
from playwright.sync_api import expect
from pages.login_page import LoginPage
@pytest.mark.smoke
def test_login(page):
    logger.info("Opening website")
    page.goto("https://www.saucedemo.com/")
    page.wait_for_load_state("networkidle")
    logger.info("Performing login")
    login = LoginPage(page)
    login.login("visual_user", "secret_sauce")

    logger.info("Verifying login success")
    expect(page.get_by_text("Products")).to_be_visible()

    logger.info("Test completed successfully")

