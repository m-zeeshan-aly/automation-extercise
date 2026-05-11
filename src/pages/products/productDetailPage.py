class ProductDetail:
    def __init__(self,page):
        self.page = page
        self._product_tab = page.locator("//a[@href='/products']")
        self._product_heading = page.locator("//div[@class='product-information']//h2")
        self._product_price = page.locator("//span//span")
        self._add_to_cart_button = page.locator("//button[normalize-space()='Add to cart']")
        self._product_image = page.locator("//div[@class='view-product']//img[@alt='ecommerce website products']")
    @property
    def get_product_tab(self):
        return self._product_tab
    
    @property
    def get_description(self):
        return self._product_heading
    
    @property
    def get_product_price(self):
        return self._product_price
    
    @property
    def get_product_image(self):
        return self._product_image