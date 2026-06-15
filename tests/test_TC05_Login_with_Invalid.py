from playwright.sync_api import expect

from pages.login_page import LoginPage
from utils.logger import logger


def test_invalid_login(page):
    logger.info("execution started for test_TC05_Login_with_Invalid")
    page.goto("https://www.saucedemo.com/")
    page.wait_for_load_state("networkidle")
    login = LoginPage(page)
    logger.info("login with invalid credentials")
    login.login("visual_user", "password")
    expect(page.
     get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible()
    logger.info("successfully verified the login with invalid credentials")