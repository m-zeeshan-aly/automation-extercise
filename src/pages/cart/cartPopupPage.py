from src.pages.cart.cartPage import Cart
class CartPopup:
    def __init__(self,page):
        self.page = page
        self._heading = page.locator("//div[@class='modal-content']//h4")
        self._continue_button = page.locator("//button[normalize-space()='Continue Shopping']")
        self._cart_button = page.locator("//u[normalize-space()='View Cart']")

    @property
    def get_heading(self):
        return self._heading
    
    def click_continue_shoping(self):
        self._continue_button.click()
        return self
    
    def click_view_cart_button(self):
        self._cart_button.click()
        return Cart(self.page)