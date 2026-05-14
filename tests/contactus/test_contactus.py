import os
import pytest
from src.pages.home.homePage import Home
from src.utils.generatedata.dataUtils import get_contact_us_data
from src.utils.controlutils.controlUtils import ControlUtils
from src.pages.contactus.contactUsPage import ContactUs

def handle_dialog(dialog):
    """
    Handles the browser alert 'Press OK to proceed!'
    """
    assert dialog.message == "Press OK to proceed!"
    dialog.accept()

@pytest.mark.parametrize("run", range(1)) 
def test_contactus_form_submission(setup, run, data = get_contact_us_data()):
    page = setup
    home_p = Home(page)
    
    # 1. Navigation and Heading Check
    ControlUtils.validate_element_is_visible(home_p.get_nav_link("contact_us"))
    page = ControlUtils.click_on_element(home_p.get_nav_link("contact_us"))
    
    contactus_p = ContactUs(page)
    ControlUtils.validate_element_is_visible(contactus_p.get_heading)

    # 3. Fill and Validate Inputs (Matching your Signup approach)
    # Name
    ControlUtils.fill_input_field(contactus_p.get_input("name"), data.get("name"))
    ControlUtils.validate_input(contactus_p.get_input("name"), data.get("name"))

    # Email
    ControlUtils.fill_input_field(contactus_p.get_input("email"), data.get("email"))
    ControlUtils.validate_input(contactus_p.get_input("email"), data.get("email"))

    # Subject
    ControlUtils.fill_input_field(contactus_p.get_input("subject"), data.get("subject"))
    ControlUtils.validate_input(contactus_p.get_input("subject"), data.get("subject"))

    # Message (Textarea)
    ControlUtils.fill_input_field(contactus_p.get_message_field(), data.get("message"))
    ControlUtils.validate_input(contactus_p.get_message_field(), data.get("message"))

    # 4. File Upload
    current_working_dir = os.getcwd()
    file_path = os.path.join(current_working_dir, 'testdata/upload_file.jpg')
    
    upload_input = contactus_p.get_input("upload_file")
    upload_input.set_input_files(file_path)
    
    # Assert file name is present in the input
    assert "upload_file.jpg" in upload_input.input_value(), "File failed to upload"

    # 5. Dialog Handling and Submission
    submit_button = contactus_p.get_input("submit")
    ControlUtils.validate_element_is_visible(submit_button)

    # Listen for the popup before clicking
    page.once("dialog", handle_dialog)
    page.wait_for_load_state("networkidle")
    
    # Click submit (Expect navigation/refresh)
    page = ControlUtils.click_on_element(submit_button)

    # 6. Success Validation
    ControlUtils.validate_element_have_text(
        contactus_p.success_message, 
        text="Success! Your details have been submitted successfully."
    )

    # 7. Return to Home
    page = ControlUtils.click_on_element(contactus_p.get_home_button)
    
    # Final check to ensure we are back home
    ControlUtils.validate_element_is_visible(home_p.get_nav_link("contact_us"))