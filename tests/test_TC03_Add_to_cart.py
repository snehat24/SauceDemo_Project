import pytest

from pages.add_to_cart import AddToCart
from utils.logger import logger
from playwright.sync_api import expect

@pytest.mark.regression
def test_add_to_cart(login_page):

    logger.info("execution started for TC03_Add_to_cart")
    page=login_page
    logger.info("assigned login in page and performing add_to_cart")
    cart=AddToCart(page)
    cart.add_to_cart()
    expect(page.get_by_role("button", name="Remove")).to_be_visible()
    logger.info("successfully added to cart")