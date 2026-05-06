from playwright.sync_api import expect
from src.pages.home.HomePage import Home

def test_login_url(setup):
    page = setup
    home = Home(page)
    login_p = home.click_signup_login()
    expect(page).to_have_url("https://automationexercise.com/login")