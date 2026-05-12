from src.pages.signup.signupPage import Signup
# from src.pages.home.HomePage import Home
class Login:
    EMAIL = "//input[@data-qa='{method}-email']"
    BUTTON = "//button[normalize-space()='{title}']"
    INPUT = "//input[@placeholder='{placeholder}']"
    ERROR = "//button[normalize-space()='Signup' or normalize-space()='Login']/preceding-sibling::p"
    def __init__(self,page):
        self.page = page
        self._signup_header = page.locator("//h2[normalize-space()='New User Signup!']")
        self._login_header = page.locator("//h2[normalize-space()='Login to your account']")
    
    @property
    def signup_header(self):
        return self._signup_header
    
    @property
    def login_header(self):
        return self._signup_header
    
    def email_locator(self,method):
        return self.page.locator(self.EMAIL.format(method=method))
    
    def button_locator(self,title):
        return self.page.locator(self.BUTTON.format(title=title))
    
    def get_input_field(self,placeholder):
        return self.page.locator(self.INPUT.format(placeholder=placeholder))
    
    def error_message(self):
        return self.page.locator(self.ERROR)

    
    # def login(self,button):
    #     from src.pages.home.homePage import Home
    #     button.click()
    #     return Home(self.page)
    
    # def logout(self,button):
    #     from src.pages.home.homePage import Home
    #     button.click()
    #     return Home(self.page)
    