import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def yetiforce_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto("https://demo.yetiforce.com/index.php?module=Users&view=Login")
        yield page
        browser.close()

