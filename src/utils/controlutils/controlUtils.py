from playwright.sync_api import expect
class ControlUtils:
    @staticmethod
    def click_on_element(locator):
        page = locator.page
        locator.click()
        return page
    
    @staticmethod
    def fill_input_field(locator,input):
        locator.fill(input)
        return locator
    
    @staticmethod
    def validate_input(locator,input):
        expect(locator).to_have_value(input)

    @staticmethod
    def validate_element_is_visible(locator):
        expect(locator).to_be_visible()

    @staticmethod
    def valodate_element_is_editable(locator):
        expect(locator).to_be_editable()

    @staticmethod
    def check_radio_and_checkbox_button(locator):
        locator.check()
        return locator
    
    @staticmethod
    def validate_element_is_checked(locator):
        expect(locator).to_be_checked()

    @staticmethod
    def select_dropdown_value(locator,value):
        locator.select_option(value)

    @staticmethod
    def validate_dropdown_value(locator,value):
        expect(locator).to_have_value(value)

    @staticmethod
    def validate_element_have_text(locator,text):
        expect(locator).to_have_text(text)

    @staticmethod
    def validate_element_contain_text(locator,text):
        expect(locator).to_contain_text(text)

    @staticmethod
    def get_clean_text(locator):
        """Extracts text content and applies standard professional cleaning."""
        text = locator.text_content()
        return text.strip() if text else ""

    @staticmethod
    def get_clean_attribute(locator, attribute):
        """Extracts an attribute and ensures it is a clean string."""
        attr = locator.get_attribute(attribute)
        return attr.strip() if attr else ""

    
    