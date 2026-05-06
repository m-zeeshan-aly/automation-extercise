class AccountCreated:
    def __init__(self,page):
        self.page = page
        self._account_header = page.locator("//b[normalize-space()='Account Created!']")
    
    @property
    def account_header(self):
        return self._account_header