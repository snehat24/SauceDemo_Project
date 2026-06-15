from playwright.sync_api import expect

from pages.logout import Logout
from utils.logger import logger


def test_logout(login_page):

    logger.info("Execution started for test_TC07_Logout")
    page = login_page
    logger.info("assigned login in page and performing logout process")
    log=Logout(page)
    log.open_menu()
    log.logout()
    logger.info("verifying if logged out or not")
    expect(page.locator('#login-button')).to_be_visible()
    logger.info("successfully logged out")