class Cart:
    def __init__(self,page):
        self.page = page
        self._checkout_button = page.locator("//a[normalize-space()='Proceed To Checkout']")
        self._cart_items = page.locator("//tbody//tr")

    @property
    def get_checkout_button(self):
        return self._checkout_button
    
    def get_all_cart_items(self):
        return self._cart_items