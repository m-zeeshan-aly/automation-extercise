from src.pages.home.homePage import Home
class OrderSuccess:
    BUTTON = "//a[normalize-space()='{name}']"
    def __init__(self,page):
        self.page = page
        self.success_message = page.locator("//p[normalize-space()='Congratulations! Your order has been confirmed!']")
        # self._down_invoice_button("//a[normalize-space()='Download Invoice']")
        # self.contine_

    @property
    def get_success_message(self):
        return self.success_message
    
    def get_button(self,name):
        return self.page.locator(self.BUTTON.format(name=name))
    
    def click_continue_button(self,button):
        button.click()
        return Home(self.page)