from src.pages.login.loginPage import Login
from src.pages.contactus.contactUsPage import ContactUs
class Home:
    def __init__(self,page):
        self.page = page
        self._login_signup_button = page.locator("//a[normalize-space()='Signup / Login']")
        self._user_name = page.locator("//li[contains(a,'Logged in as')]//b")
        self._logout_button = page.locator("//a[normalize-space()='Logout']")
        self._cart_button = page.locator("//li//a[@href='/view_cart']")
        self._products_button = page.locator("//li//a[@href='/products']")
        self._contact_us_button = page.locator("//li//a[@href='/contact_us']")
    
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
    
    @property
    def get_products_button(self):
        return self._products_button
    
    @property
    def get_contact_us_button(self):
        return self._contact_us_button
    
    def click_contact_us_button(self):
        self._contact_us_button.click()
        return ContactUs(self.page)
    
    def click_cart_button(self):
        from src.pages.cart.cartPage import Cart
        self._cart_button.click()
        return Cart(self.page)
    
    