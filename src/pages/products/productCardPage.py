from src.pages.products.productDetailPage import ProductDetail
from src.pages.cart.cartPopupPage import CartPopup
import random
class ProductCard:

    def __init__(self,page):
        self.page = page
        self._all_products = page.locator("//div[@class='features_items']//div[@class='col-sm-4']")

        self._simple_class = "//div[@class='productinfo text-center']"
        self._hover_class = "//div[@class='overlay-content']"

        self._price = "/h2"
        self._description = "/p"

        self._view_product_button = "//a[normalize-space()='View Product']"
        self._cart_button = "/a"

        self._card_img = "//div[@class='productinfo text-center']/img"

    @property
    def get_all_products(self):
        return self._all_products
    
    def select_product(self):
        index = random.randint(0, self._all_products.count() - 1)
        return self._all_products.nth(index)
    
    def get_price(self,product):
        return product.locator(self._simple_class+self._price).text_content().strip()
    
    def get_description(self,product):
        return product.locator(self._simple_class+self._description).text_content().strip()
    
    def get_price_on_hover(self,product):
        return product.locator(self._hover_class+self._price).text_content().strip()
    
    def get_description_on_hover(self,product):
        return product.locator(self._hover_class+self._description).text_content().strip()
    
    def get_view_product_button(self,product):
        return product.locator(self._view_product_button)
    
    def get_add_to_cart_button(self,product):
        return product.locator(self._simple_class+self._cart_button)
    
    def get_add_to_cart_button_on_hover(self,product):
        return product.locator(self._hover_class+self._cart_button)
    
    def get_image(self,product):
        return product.locator(self._card_img)
    
    def click_view_product(self,button):
        button.click()
        return ProductDetail(self.page)
    
    def click_add_to_cart(self,button):
        button.click()
        return CartPopup(self.page)


            
