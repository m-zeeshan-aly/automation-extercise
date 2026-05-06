import pytest
from playwright.sync_api import Playwright,expect
from src.pages.login.loginPage import Login

@pytest.fixture(scope="function")
def setup(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://automationexercise.com/")
    yield page
    context.close()
    browser.close()



@pytest.fixture(scope="session")
def save_login_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://automationexercise.com/login")

    login_p = Login(page)

    login_p.email_locator("login").fill("dummybaba@gmail.com")
    login_p.get_input_field("Password").fill("pakistan123")
    login_p.button_locator("Login").click()

    context.storage_state(path="auth.json")

    # yield page

    context.close()
    browser.close()


@pytest.fixture(scope="function")
def use_saved_login(playwright: Playwright, save_login_state):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth.json")

    page = context.new_page()
    # page = save_login_state

    page.goto("https://automationexercise.com/")

    yield page

    context.close()
    browser.close()