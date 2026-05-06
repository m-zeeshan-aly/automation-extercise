from playwright.sync_api import expect
from src.pages.home.homePage import Home

def xtest_login_url(setup):
    page = setup
    home = Home(page)
    login_p = home.click_signup_login()
    expect(page).to_have_url("https://automationexercise.com/login")


def xtest_login_and_logout(setup):
    page = setup
    home_p = Home(page)
    login_p = home_p.click_signup_login()
    expect(page).to_have_url("https://automationexercise.com/login")

    login_p.email_locator("login").fill("dummybaba@gmail.com")
    expect(login_p.email_locator("login")).to_have_value("dummybaba@gmail.com")


    login_p.get_input_field("Password").fill("pakistan123")
    expect(login_p.get_input_field("Password")).to_have_value("pakistan123")

    button = login_p.button_locator("Login")
    home_p = login_p.login(button)
    page.wait_for_timeout(300)

    error = login_p.error_message()
    if error.is_visible():
        error_text = error.text_content().strip()
        assert error_text == "Your email or password is incorrect!", f"Unexpected error: {error_text}"
    
    expect(error).not_to_be_visible()
    logout_button = home_p.get_logout_button
    expect(logout_button).to_be_visible()

    # loggin out 
    home_p = login_p.logout(logout_button)
    logout_button = home_p.get_logout_button
    expect(logout_button).not_to_be_visible()


    page.wait_for_timeout(300)


def xtest_login_suceess(setup):
    page = setup
    home_p = Home(page)
    login_p = home_p.click_signup_login()
    expect(page).to_have_url("https://automationexercise.com/login")

    login_p.email_locator("login").fill("dummybaba@gmail.com")
    expect(login_p.email_locator("login")).to_have_value("dummybaba@gmail.com")


    login_p.get_input_field("Password").fill("pakistan123")
    expect(login_p.get_input_field("Password")).to_have_value("pakistan123")

    login_p.button_locator("Login").click()
    page.wait_for_timeout(300)

    error = login_p.error_message()
    if error.is_visible():
        error_text = error.text_content().strip()
        assert error_text == "Your email or password is incorrect!", f"Unexpected error: {error_text}"
    
    expect(error).not_to_be_visible()
    logout_button = home_p.get_logout_button
    expect(logout_button).to_be_visible()
    page.wait_for_timeout(300)


def xtest_login_with_wrong_email_pass(setup):
    page = setup
    home = Home(page)
    login_p = home.click_signup_login()
    expect(page).to_have_url("https://automationexercise.com/login")

    login_p.email_locator("login").fill("dummybaba@gmail.com")
    expect(login_p.email_locator("login")).to_have_value("dummybaba@gmail.com")


    login_p.get_input_field("Password").fill("pakistan12")
    expect(login_p.get_input_field("Password")).to_have_value("pakistan12")

    login_p.button_locator("Login").click()

    error = login_p.error_message()
    expect(error).to_have_text("Your email or password is incorrect!")
    if error.is_visible():
        error_text = error.text_content().strip()
        assert error_text == "Your email or password is incorrect!", f"Unexpected error: {error_text}"

    page.wait_for_timeout(300)

