from playwright.sync_api import expect

def test_home_navigation(setup):
    page= setup
    expect(page).to_have_url("https://automationexercise.com/")
