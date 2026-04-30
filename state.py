from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill("input#user-name","standard_user")
    page.fill("input#password", "secret_sauce")
    page.click("input#login-button")
    page.wait_for_url("**/inventory.html")
    print(page.url)
    context.storage_state(path="state.json")
    browser.close()