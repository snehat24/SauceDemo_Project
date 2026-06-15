from playwright.sync_api import expect

from pages import login_page, checkout_page
from pages.add_to_cart import AddToCart
from pages.checkout_page import CheckoutPage
from utils.logger import logger


def test_remove_from_cart(login_page):
    logger.info("Execution started for test_TC08_Remove_from_cart")
    page=login_page
    logger.info("assigned login in page and performing remove process")
    cart=AddToCart(page)
    cart.add_to_cart()
    expect(page.get_by_role("button", name="Remove")).to_be_visible()
    logger.info("after added to cart we continue to remove it from cart")
    check=CheckoutPage(page)
    check.remove()
    logger.info("successfully removed from cart")