from playwright.sync_api import expect
from src.pages.home.homePage import Home
# from src.utils.generatedata.generateDataUtils import GenerateData
from src.utils.generatedata.dataUtils import signup_data
import pytest 

@pytest.mark.parametrize("run", range(1))  # runs 1 time increase number to run multiple time
def xtest_signup_form(setup,run):
    page = setup
    home = Home(page)
    login_p = home.click_signup_login()
    expect(login_p.signup_header).to_have_text("New User Signup!")

    data = signup_data()
    # print(data)

    login_p.get_input_field("Name").fill(data.get("full_name"))
    expect(login_p.get_input_field("Name")).to_have_value(data.get("full_name"))

    login_p.email_locator("signup").fill(data.get("email"))
    expect(login_p.email_locator("signup")).to_have_value(data.get("email"))

    button = login_p.button_locator("Signup")
    signup_p = login_p.click_button(button)

    error = login_p.error_message()
    if error.is_visible():
        error_text = error.text_content().strip()
        assert error_text == "Email Address already exist!", "User already exist cannot add"

    expect(signup_p.signup_header).to_be_visible()

    expect(signup_p.get_input_field("name")).to_be_editable()
    signup_p.get_input_field("name").fill(("sk "+data.get("full_name")))

    expect(signup_p.get_input_field("email")).not_to_be_editable()

    signup_p.get_title_radio_locator(data.get("title")).check()
    expect(signup_p.get_title_radio_locator(data.get("title"))).to_be_checked()

    if data.get("title")=="Mr":
        expect(signup_p.get_title_radio_locator("Mrs")).not_to_be_checked()
    if data.get("title")=="Mrs":
        expect(signup_p.get_title_radio_locator("Mr")).not_to_be_checked()

    signup_p.get_input_field("password").fill(''.join([data.get("first_name"),data.get("phone")]))
    expect(signup_p.get_input_field("password")).to_have_value(''.join([data.get("first_name"),data.get("phone")]))
    
    signup_p.get_dropdown("days").select_option(value=data.get("day"))
    expect(signup_p.get_dropdown("days")).to_have_value(data.get("day"))

    signup_p.get_dropdown("months").select_option(data.get("month"))
    selected_month = signup_p.get_dropdown("months").text_content()

    assert data.get("month") in selected_month

    signup_p.get_dropdown("years").select_option(data.get("year"))
    expect(signup_p.get_dropdown("years")).to_have_value(data.get("year"))

    for checkbox in data.get("checkboxes"):
        signup_p.get_checkbox_locator(checkbox).check()

    for checkbox in data.get("checkboxes"):
        expect(signup_p.get_checkbox_locator(checkbox)).to_be_checked()


    signup_p.get_input_field("first_name").fill(data.get("first_name"))
    expect(signup_p.get_input_field("first_name")).to_have_value(data.get("first_name"))
    signup_p.get_input_field("last_name").fill(data.get("last_name"))
    expect(signup_p.get_input_field("last_name")).to_have_value(data.get("last_name"))
    signup_p.get_input_field("company").fill(data.get("company"))
    expect(signup_p.get_input_field("company")).to_have_value(data.get("company"))

    signup_p.get_input_field("address1").fill(data.get("address"))
    expect(signup_p.get_input_field("address1")).to_have_value(data.get("address"))
    signup_p.get_input_field("address2").fill(data.get("address"))
    expect(signup_p.get_input_field("address2")).to_have_value(data.get("address"))

     
    signup_p.get_dropdown("country").select_option(data.get("country"))
    expect(signup_p.get_dropdown("country")).to_have_value(data.get("country"))

    signup_p.get_input_field("state").fill(data.get("state"))
    expect(signup_p.get_input_field("state")).to_have_value(data.get("state"))

    signup_p.get_input_field("city").fill(data.get("city"))
    expect(signup_p.get_input_field("city")).to_have_value(data.get("city"))

    signup_p.get_input_field("zipcode").fill(data.get("zip_code"))
    expect(signup_p.get_input_field("zipcode")).to_have_value(data.get("zip_code"))

    signup_p.get_input_field("mobile_number").fill(data.get("phone"))
    expect(signup_p.get_input_field("mobile_number")).to_have_value(data.get("phone"))

    account_created_p =signup_p.signup()
    page.wait_for_timeout(1000)
    expect(account_created_p.account_header).to_be_visible()


