from src.pages.login.LoginPage import Login
class Home:
    def __init__(self,page):
        self.page = page
        self._login_signup_button = page.locator("//a[normalize-space()='Signup / Login']")
    
    def click_signup_login(self):
        self._login_signup_button.click()
        return Login(self.page)