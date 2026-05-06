from src.pages.login.loginPage import Login
class Home:
    def __init__(self,page):
        self.page = page
        self._login_signup_button = page.locator("//a[normalize-space()='Signup / Login']")
        self._user_name = page.locator("//li[contains(a,'Logged in as')]//b")
        self._logout_button = page.locator("//a[normalize-space()='Logout']")
    
    def click_signup_login(self):
        self._login_signup_button.click()
        return Login(self.page)
    @property
    def user_name(self):
        return self._user_name
    
    @property
    def get_logout_button(self):
        return self._logout_button
    