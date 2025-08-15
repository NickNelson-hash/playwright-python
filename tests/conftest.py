import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def login_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.yetiforce.com/index.php?module=Users&view=Login")
        yield page
        browser.close()

