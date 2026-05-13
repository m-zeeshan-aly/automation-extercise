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
    def get_checkout_heading(self):
        return self._checkout_heading
    
    @property
    def get_continue_shopping_button(self):
        return self._continue_button
    
    @property
    def get_view_cart_button(self):
        return self._cart_button
    
    @property
    def get_login_signup_button(self):
        return self._login_signup_button
    
    @property
    def get_continue_on_cart_button(self):
        return self._continue_on_cart_button
