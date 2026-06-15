from playwright.sync_api import expect

from pages.add_to_cart import AddToCart
from pages.checkout_page import CheckoutPage
from utils.logger import logger


def test_checkout_page(login_page):
    logger.info("Execution started for test_TC06_Checkout")
    page=login_page
    logger.info("assigned login in page and performing checkout process")
    cart = AddToCart(page)
    cart.add_to_cart()
    expect(page.get_by_role("button", name="Remove")).to_be_visible()
    logger.info("item added to cart and continue checkkout process")
    check= CheckoutPage(page)
    check.open_cart()
    check.checkout_page()
    logger.info("filling details for checkout process")
    check.credentials("test","23","2807")
    check.finalContinue()
    check.finish()
    logger.info("verifying if checkout is successful")
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()
    logger.info("successfully checked out")

