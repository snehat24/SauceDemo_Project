from playwright.sync_api import expect

from pages.add_to_cart import AddToCart
from pages.checkout_page import CheckoutPage
from utils.logger import logger


def test_checkout_without_address(login_page):
    logger.info("Execution started for test_TC09_Checkout_without_address")
    page=login_page
    logger.info("assigned login in page and performing checkout process")
    cart = AddToCart(page)
    cart.add_to_cart()
    expect(page.get_by_role("button", name="Remove")).to_be_visible()
    logger.info("item added to cart ")
    check= CheckoutPage(page)
    check.open_cart()
    check.checkout_page()
    logger.info("Continue checkkout process without filling address details")
    check.credentials("test","23","")
    check.finalContinue()
    logger.info("verifying if we can checkout without filling address details")
    expect(page.get_by_text("Error: Postal Code is required")).to_be_visible()
    logger.info("test case passed")