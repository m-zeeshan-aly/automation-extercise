from src.pages.home.homePage import Home
from src.utils.controlutils.controlUtils import ControlUtils
from src.pages.login.loginPage import Login
from src.utils.constants.constantsUtils import WRONG_PASSWORD,WRONG_EMAIL, PASSWORD, EMAIL

def xtest_login_navigation(setup):
    page = setup
    home = Home(page)
    page = ControlUtils.click_on_element(home.get_button('Signup / Login'))
    login_p = Login(page)
    ControlUtils.validate_element_is_visible(login_p.login_header)


def xtest_login_with_valid_credentials(setup):
    page = setup
    home = Home(page)
    page = ControlUtils.click_on_element(home.get_button('Signup / Login'))
    login_p = Login(page)
    ControlUtils.validate_element_is_visible(login_p.login_header)

    ControlUtils.fill_input_field(login_p.email_locator("login"),EMAIL)
    ControlUtils.validate_input(login_p.email_locator("login"),EMAIL)

    ControlUtils.fill_input_field( login_p.get_input_field("Password"),PASSWORD)
    ControlUtils.validate_input( login_p.get_input_field("Password"),PASSWORD)

    page = ControlUtils.click_on_element(login_p.button_locator("Login"))
    home = Home(page)

    error = login_p.error_message()
    if error.is_visible():
        error_text = error.text_content().strip()
        assert error_text == "Your email or password is incorrect!", f"Unexpected error: {error_text}"
    
    ControlUtils.validate_element_is_visible(home.get_button("Logout"))


def xtest_login_and_logout(setup):
    page = setup
    home = Home(page)
    page = ControlUtils.click_on_element(home.get_button('Signup / Login'))
    login_p = Login(page)
    ControlUtils.validate_element_is_visible(login_p.login_header)

    ControlUtils.fill_input_field(login_p.email_locator("login"),EMAIL)
    ControlUtils.validate_input(login_p.email_locator("login"),EMAIL)

    ControlUtils.fill_input_field( login_p.get_input_field("Password"),PASSWORD)
    ControlUtils.validate_input( login_p.get_input_field("Password"),PASSWORD)

    page = ControlUtils.click_on_element(login_p.button_locator("Login"))
    home = Home(page)

    error = login_p.error_message()
    if error.is_visible():
        error_text = error.text_content().strip()
        assert error_text == "Your email or password is incorrect!", f"Unexpected error: {error_text}"
    
    ControlUtils.validate_element_is_visible(home.get_button("Logout"))
    page = ControlUtils.click_on_element(home.get_button("Logout"))
    home = Home(page)

    ControlUtils.validate_element_is_visible(home.get_button('Signup / Login'))


def xtest_login_with_invalid_credentials(setup):
    page = setup
    home = Home(page)
    page = ControlUtils.click_on_element(home.get_button('Signup / Login'))
    login_p = Login(page)
    ControlUtils.validate_element_is_visible(login_p.login_header)

    ControlUtils.fill_input_field(login_p.email_locator("login"),WRONG_EMAIL)
    ControlUtils.validate_input(login_p.email_locator("login"),WRONG_EMAIL)

    ControlUtils.fill_input_field( login_p.get_input_field("Password"),WRONG_PASSWORD)
    ControlUtils.validate_input( login_p.get_input_field("Password"),WRONG_PASSWORD)

    page = ControlUtils.click_on_element(login_p.button_locator("Login"))
    home = Home(page)

    error = login_p.error_message()
    if error.is_visible():
        error_text = error.text_content().strip()
        assert error_text == "Your email or password is incorrect!", f"Unexpected error: {error_text}"
    
    


