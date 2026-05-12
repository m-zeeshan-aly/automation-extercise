from src.pages.account.accountCreatedPage import AccountCreated
class Signup:
    TITLE_RADIO_INPUT = "//input[@type='radio' and @value='{title}']"
    INPUT_FIELD = "//input[@id='{name}']"
    DROPDOWN = "//select[@id='{title}']"
    CHECKBOX = "//div[@class='checkbox'][.//label[normalize-space()='{text}']]//input"

    def __init__(self,page):
        
        self.page = page
        self._signup_header = page.locator("//div[@class='login-form']/h2/b[text()='Enter Account Information']")
        self._signup_button = page.locator("//button[normalize-space()='Create Account']")

    @property
    def signup_header(self):
        return self._signup_header
    
    @property
    def get_signup_button(self):
        return self._signup_button
    
    def get_title_radio_locator(self, title):
        """
        This give the radio button locator of the specific title Mr or Mrs
        """
        return self.page.locator(self.TITLE_RADIO_INPUT.format(title=title))
    
    def get_input_field(self, name):
        """
        This works for the in input filed like name email and password form the account section
        This also work for the at the Address section like first and last name etc.
        """
        return self.page.locator(self.INPUT_FIELD.format(name=name))
    
    def get_dropdown(self, title):
        """
        This takes in the value like days months years and country and return the specific locator 
        """
        return self.page.locator(self.DROPDOWN.format(title=title))
    
    def get_checkbox_locator(self, text):
        """
        This gives the checkbox input locator of the specific id newsletter or optin
        """
        return self.page.locator(self.CHECKBOX.format(text=text))
