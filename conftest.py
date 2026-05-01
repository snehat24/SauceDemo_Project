import pytest
import os
from datetime import datetime

from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from config.config import URLS, USERNAME, PASSWORD


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa")


@pytest.fixture
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def browser():
    from playwright.sync_api import sync_playwright

    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)

    yield browser

    browser.close()
    playwright.stop()


@pytest.fixture
def login_page(browser, env):

    if os.path.exists("state.json"):
        context = browser.new_context(storage_state="state.json")
        page = context.new_page()
        page.goto(URLS[env] + "inventory.html")
    else:
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.goto(URLS[env])
        login_page = LoginPage(page)
        login_page.login(USERNAME, PASSWORD)
        page.wait_for_load_state("networkidle")

    yield page
    context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("login_page")

        if page:
            os.makedirs("screenshots/fail", exist_ok=True)
            timestamp = datetime.now().strftime("%H-%M-%S")
            file_name = f"screenshots/fail/{item.name}_{timestamp}.png"
            page.screenshot(path=file_name, full_page=True)
            print(f"\n[DEBUG] Screenshot: {file_name}")

            context = page.context
            os.makedirs("trace", exist_ok=True)
            trace_file = f"trace/{item.name}.zip"
            context.tracing.stop(path=trace_file)
            print(f"[TRACE] Saved: {trace_file}")