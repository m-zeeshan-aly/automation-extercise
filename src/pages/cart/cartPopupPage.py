from src.pages.cart.cartPage import Cart
from src.pages.login.loginPage import Login
class CartPopup:
    def __init__(self,page):
        self.page = page
        self._heading = page.locator("//div[@class='modal-content']//h4")
        self._continue_button = page.locator("//button[normalize-space()='Continue Shopping']")
        self._cart_button = page.locator("//u[normalize-space()='View Cart']")

        self._checkout_heading = page.locator("//h4[normalize-space()='Checkout']")
        self._login_signup_button = page.locator("//u[normalize-space()='Register / Login']")
        self._continue_on_cart_button = page.locator("//button[normalize-space()='Continue On Cart']")

    @property
    def get_heading(self):
        return self._heading
    
    @property
    def get_cehckout_heading(self):
        return self._checkout_heading
    
    def click_continue_shoping(self):
        self._continue_button.click()
        return self
    
    def click_continue_on_cart(self):
        self._continue_on_cart_button.click()
        return self
    
    def click_view_cart_button(self):
        self._cart_button.click()
        return Cart(self.page)
    
    def click_login_signup_button(self):
        self._login_signup_button.click()
        return Login(self.page)