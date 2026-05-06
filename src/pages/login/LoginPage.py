from src.pages.signup.SignupPage import Signup
class Login:
    def __init__(self,page):
        self.page = page
        self._signup_header = page.locator("//h2[normalize-space()='New User Signup!']")
        self._name_input = page.locator("//input[@placeholder='Name']")
        self._email_input = page.locator("//input[@data-qa='signup-email']")
        self._signup_button = page.locator("//button[normalize-space()='Signup']")
        self._signup_error_message = page.locator("//button[normalize-space()='Signup']/preceding-sibling::p")

        self._login_header = page.locator("//h2[normalize-space()='Login to your account']")
        self._login_email_input = page.locator("//input[@data-qa='login-email']")
        self._login_password_input = page.locator("//input[@placeholder='Password']")
        self._login_button = page.locator("//button[normalize-space()='Login']")
    
    @property
    def signup_header(self):
        return self._signup_header
    @property
    def email_input(self):
        return self._email_input
    @property
    def name_input(self):
        return self._name_input
    @property
    def signup_error_message(self):
        return self._signup_error_message
    
    def enterName(self,name):
        self._name_input.clear()
        self._name_input.fill(name)
    def enterEmail(self,email):
        self._email_input.clear()
        self._email_input.fill(email)

    def click_signup_button(self):
        self._signup_button.click()
        return self

    def create_new_user(self):
        self._signup_button.click()
        return Signup(self.page)