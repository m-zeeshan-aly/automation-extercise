from src.pages.login.loginPage import Login
class Home:
    def __init__(self,page):
        self.page = page
        self._login_signup_button = page.locator("//a[normalize-space()='Signup / Login']")
        self._user_name = page.locator("//li[contains(a,'Logged in as')]//b")
        self._logout_button = page.locator("//a[normalize-space()='Logout']")
        self._cart_button = page.locator("//li//a[@href='/view_cart']")
    
    def click_signup_login(self):
        self._login_signup_button.click()
        return Login(self.page)
    @property
    def user_name(self):
        return self._user_name
    
    @property
    def get_logout_button(self):
        return self._logout_button
    
    @property
    def get_cart_button(self):
        return self._cart_button
    
    def click_cart_button(self):
        from src.pages.cart.cartPage import Cart
        self._cart_button.click()
        return Cart(self.page)
    
    