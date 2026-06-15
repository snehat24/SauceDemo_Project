from playwright.sync_api import expect

from pages.sort_page import Sorting
from utils.logger import logger


def test_sort(login_page):

    logger.info("execution started for test_TC04_sorting")
    page = login_page
    logger.info("assigned login in page and performing sorting")
    st=Sorting(page)
    before=st.get_first_product()
    st.sort_page("za")
    logger.info("clicked dropdown sorting option")
    after=st.get_first_product()
    logger.info("verifying if sort is worked or not")
    assert before!=after
    logger.info("successfully sorted page")


