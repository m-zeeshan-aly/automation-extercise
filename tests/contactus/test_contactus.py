from playwright.sync_api import expect
from src.pages.home.homePage import Home
import os
import pytest
from src.utils.generatedata.dataUtils import get_contact_us_data

def handle_dialog(dialog):
    assert dialog.message == "Press OK to proceed!"
    dialog.accept()

@pytest.mark.parametrize("run", range(2)) 
def xtest_contactus_form(setup,run):
    page= setup
    home_p = Home(page)

    contact_us_button = home_p.get_contact_us_button
    expect(home_p.get_contact_us_button).to_be_visible()

    contactus_p = home_p.click_contact_us_button()
    expect(contactus_p.get_heading).to_be_visible()

    data = get_contact_us_data()

    input = contactus_p.get_input("name")
    expect(input).to_be_editable()
    input.clear()
    input.fill(data.get("name"))

    input = contactus_p.get_input("email")
    expect(input).to_be_editable()
    input.clear()
    input.fill(data.get("email"))

    input = contactus_p.get_input("subject")
    expect(input).to_be_editable()
    input.clear()
    input.fill(data.get("subject"))

    input = contactus_p.get_message_field()
    expect(input).to_be_editable()
    input.clear()
    input.fill(data.get("message"))

    current_working_dir =os.getcwd()
    file_path = os.path.join(current_working_dir,'testdata/upload_file.jpg')

    input = contactus_p.get_input("upload_file")

    input.set_input_files(file_path)

    assert "upload_file.jpg" in input.input_value()

    submit_button = contactus_p.get_input("submit")

    expect(submit_button).to_be_visible()

    page.once("dialog", handle_dialog)
    page.wait_for_load_state("networkidle")
    submit_button.click()
    expect(contactus_p.success_message).to_have_text("Success! Your details have been submitted successfully.")

    home_p = contactus_p.click_home_button()
    # page.wait_for_timeout(2000)

