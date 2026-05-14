from playwright.sync_api import expect
from src.pages.home.homePage import Home
from src.utils.generatedata.dataUtils import signup_data
from src.utils.controlutils.controlUtils import ControlUtils
from src.pages.login.loginPage import Login
from src.pages.signup.signupPage import Signup
from src.pages.account.accountCreatedPage import AccountCreated
import pytest 

@pytest.mark.parametrize("run", range(1))  # runs 1 time increase number to run multiple time
def test_signup_form(setup,run, data = signup_data()):
    page = setup
    home = Home(page)
    page = ControlUtils.click_on_element(home.get_button('Signup / Login'))
    login_p = Login(page)
    expect(login_p.signup_header).to_have_text("New User Signup!")

    ControlUtils.fill_input_field(login_p.get_input_field("Name"),data.get("full_name"))
    ControlUtils.validate_input(login_p.get_input_field("Name"),data.get("full_name"))
    # ControlUtils.validate_input(ControlUtils.fill_input_field(login_p.get_input_field("Name"),data.get("full_name")),data.get("full_name"))

    ControlUtils.fill_input_field(login_p.email_locator("signup"),data.get("email"))
    ControlUtils.validate_input(login_p.email_locator("signup"),data.get("email"))

    page = ControlUtils.click_on_element(login_p.button_locator("Signup"))
    signup_p = Signup(page)

    error = login_p.error_message()
    if error.is_visible():
        error_text = error.text_content().strip()
        assert error_text == "Email Address already exist!", "User already exist cannot add"

    ControlUtils.validate_element_is_visible(signup_p.signup_header)

    ControlUtils.valodate_element_is_editable(signup_p.get_input_field("name"))
    signup_p.get_input_field("name").fill((data.get("full_name")))

    ControlUtils.fill_input_field(signup_p.get_input_field("name"),data.get("full_name"))
    ControlUtils.validate_input(signup_p.get_input_field("name"),data.get("full_name"))

    expect(signup_p.get_input_field("email")).not_to_be_editable()

    ControlUtils.check_radio_and_checkbox_button(signup_p.get_title_radio_locator(data.get("title")))
    ControlUtils.validate_element_is_checked(signup_p.get_title_radio_locator(data.get("title")))
    
    if data.get("title")=="Mr":
        expect(signup_p.get_title_radio_locator("Mrs")).not_to_be_checked()
    if data.get("title")=="Mrs":
        expect(signup_p.get_title_radio_locator("Mr")).not_to_be_checked()

    ControlUtils.fill_input_field(signup_p.get_input_field("password"),(''.join([data.get("first_name"),data.get("phone")])))
    ControlUtils.validate_input(signup_p.get_input_field("password"),(''.join([data.get("first_name"),data.get("phone")])))

    ControlUtils.select_dropdown_value(signup_p.get_dropdown("days"),data.get("day"))
    ControlUtils.validate_dropdown_value(signup_p.get_dropdown("days"),data.get("day"))

    ControlUtils.select_dropdown_value(signup_p.get_dropdown("months"),data.get("month"))

    # selected_month = signup_p.get_dropdown("months").text_content()
    # assert data.get("month") in selected_month

    ControlUtils.select_dropdown_value(signup_p.get_dropdown("years"),data.get("year"))
    ControlUtils.validate_dropdown_value(signup_p.get_dropdown("years"),data.get("year"))


    for checkbox in data.get("checkboxes"):
        ControlUtils.check_radio_and_checkbox_button(signup_p.get_checkbox_locator(checkbox))

    for checkbox in data.get("checkboxes"):
        ControlUtils.validate_element_is_checked(signup_p.get_checkbox_locator(checkbox))

    ControlUtils.fill_input_field(signup_p.get_input_field("first_name"),data.get("first_name"))
    ControlUtils.validate_input(signup_p.get_input_field("first_name"),data.get("first_name"))

    ControlUtils.fill_input_field(signup_p.get_input_field("last_name"),data.get("last_name"))
    ControlUtils.validate_input(signup_p.get_input_field("last_name"),data.get("last_name"))

    ControlUtils.fill_input_field(signup_p.get_input_field("company"),data.get("company"))
    ControlUtils.validate_input(signup_p.get_input_field("company"),data.get("company"))

    ControlUtils.fill_input_field(signup_p.get_input_field("address1"),data.get("address"))
    ControlUtils.validate_input(signup_p.get_input_field("address1"),data.get("address"))

    ControlUtils.fill_input_field(signup_p.get_input_field("address2"),data.get("address"))
    ControlUtils.validate_input(signup_p.get_input_field("address2"),data.get("address"))

    ControlUtils.select_dropdown_value(signup_p.get_dropdown("country"),data.get("country"))
    ControlUtils.validate_dropdown_value(signup_p.get_dropdown("country"),data.get("country"))

    ControlUtils.fill_input_field(signup_p.get_input_field("state"),data.get("state"))
    ControlUtils.validate_input(signup_p.get_input_field("state"),data.get("state"))

    ControlUtils.fill_input_field(signup_p.get_input_field("city"),data.get("city"))
    ControlUtils.validate_input(signup_p.get_input_field("city"),data.get("city"))

    ControlUtils.fill_input_field(signup_p.get_input_field("zipcode"),data.get("zip_code"))
    ControlUtils.validate_input(signup_p.get_input_field("zipcode"),data.get("zip_code"))

    ControlUtils.fill_input_field(signup_p.get_input_field("mobile_number"),data.get("phone"))
    ControlUtils.validate_input(signup_p.get_input_field("mobile_number"),data.get("phone"))

    # account_created_p =signup_p.signup()
    # page.wait_for_timeout(1000)
    # expect(account_created_p.account_header).to_be_visible()

    page = ControlUtils.click_on_element(signup_p.get_signup_button)
    account_created_p = AccountCreated(page)
    ControlUtils.validate_element_have_text(account_created_p.account_header,text="Account Created!")


