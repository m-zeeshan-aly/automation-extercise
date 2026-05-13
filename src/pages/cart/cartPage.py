class Cart:
    def __init__(self,page):
        self.page = page
        self._checkout_button = page.locator("//a[normalize-space()='Proceed To Checkout']")
        self._cart_empty = page.locator("//span[@id='empty_cart']")
        self._cart_table = page.locator("//table[@id='cart_info_table']")

        self._p_name = "xpath=.//td[@class='cart_description']//h4"
        self._p_category = "xpath=.//td[@class='cart_description']//p"
        self._p_price = "xpath=.//td[@class='cart_price']//p"
        self._p_quantity = "xpath=.//td[@class='cart_quantity']//button"
        self._p_total = "xpath=.//td[@class='cart_total']//p"
        self._p_image_src = "xpath=.//td[@class='cart_product']//img"

        self._p_delete_button = "xpath=.//td[@class='cart_delete']//a"

    @property
    def get_checkout_button(self):
        return self._checkout_button
    
    @property
    def get_cart_empty(self):
        return self._cart_empty
    
    def get_all_cart_items(self):
        return self._cart_table.locator("//tbody/tr")
    
    def get_row_by_name(self, product_name):
        """
        Finds the specific table row (tr) that contains the product name.
        This is much safer than using indexes.
        """
        return self.page.locator("tr").filter(has_text=product_name)
    
    def get_product_name(self,product):
        return product.locator(self._p_name)
    
    def get_product_category(self,product):
        return product.locator(self._p_category)
    
    def get_product_price(self,product):
        return product.locator(self._p_price)
          
    def get_product_quantity(self,product):
        return product.locator(self._p_quantity)
    
    def get_product_total(self,product):
        return product.locator(self._p_total)
    
    def get_product_image_src(self,product):
        return product.locator(self._p_image_src)
    
    def get_delete_button(self,product):
        return product.locator(self._p_delete_button)
    
    def get_bill(self):
        cart_items = self.get_all_cart_items()
        cart_items_count = cart_items.count()
        bill = 0
        for i in range(cart_items_count):
            product = cart_items.nth(i)
            total = self.get_product_total(product).text_content().strip()
            total = total.strip("Rs. ")
            bill = bill + int(total)
        return bill



        
    
