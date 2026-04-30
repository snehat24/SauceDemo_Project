from unittest import result

import pytest

from utils.data_loader import load_test_data
from utils.logger import logger
from pages.login_page import LoginPage
from playwright.sync_api import expect

data = load_test_data("test_data/login_data.json")
@pytest.mark.parametrize("username,password,result", data)
def test_login_datadriven(page,username,password,result):

    logger.info("this is TC02_login_datadriven")
    page.goto("https://www.saucedemo.com/")
    page.wait_for_load_state("networkidle")
    logger.info("after launching website , performing login")
    login = LoginPage(page)
    login.login(username, password)

    logger.info("Verifying login success")
    if result=="Pass":
        expect(page.get_by_text("Products")).to_be_visible()
    else:
        expect(page.get_by_text("Epic sadface")).to_be_visible()

    logger.info("Test completed successfully")
