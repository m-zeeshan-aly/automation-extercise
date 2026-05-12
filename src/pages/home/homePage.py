from src.pages.login.loginPage import Login
from src.pages.contactus.contactUsPage import ContactUs
class Home:
    BUTTON = "//a[normalize-space()='{button}']"
    NAV_LINK = "//li//a[@href='/{nav_page}']"
    def __init__(self,page):
        self.page = page
        self._user_name = page.locator("//li[contains(a,'Logged in as')]//b")
    @property
    def user_name(self):
        return self._user_name
        
    def get_button(self,button):
        return self.page.locator(self.BUTTON.format(button=button))
    
    def get_nav_link(self,page_link):
        return self.page.locator(self.NAV_LINK.format(nav_page=page_link))