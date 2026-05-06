class AccountCreated:
    def __init__(self,page):
        self.page = page
        self._account_header = page.locator("//b[normalize-space()='Account Created!']")
        self._continue_button = page.locator("//a[normalize-space()='Continue']")
    
    @property
    def account_header(self):
        return self._account_header
    
    @property
    def account_continue_button(self):
        return self._continue_button