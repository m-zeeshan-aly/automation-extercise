import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="function")
def setup(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://automationexercise.com/")
    yield page
    context.close()
    browser.close()
