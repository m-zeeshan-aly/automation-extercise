from src.pages.payment.paymentPage import Payment
class Checkout:
    def __init__(self,page):
        self.page = page
        self._heading = page.locator("//h2[normalize-space()='Address Details']")
        self._place_order_button = page.locator("//a[normalize-space()='Place Order']")
        self._checkout_table = page.locator("//div[@id='cart_info']/table")

        self._p_name = "xpath=.//td[@class='cart_description']//h4"
        self._p_category = "xpath=.//td[@class='cart_description']//p"
        self._p_price = "xpath=.//td[@class='cart_price']//p"
        self._p_quantity = "xpath=.//td[@class='cart_quantity']//button"
        self._p_total = "xpath=.//td[@class='cart_total']//p"
        self._p_image_src = "xpath=.//td[@class='cart_product']//img"

        self._bill = "//tbody/tr//td[@colspan='2']//following-sibling::td/p"

        self._text_area = page.locator("//div[@id='ordermsg']//textarea")

        self._billing_address = page.locator("//ul[@id='address_invoice']//li")
        self._delivery_address = page.locator("//ul[@id='address_delivery']//li")

    @property
    def get_checkout_button(self):
        return self._checkout_button
    
    @property
    def get_heading(self):
        return self._heading
    
    @property
    def get_cart_empty(self):
        return self._cart_empty
    
    @property
    def get_bill(self):
        return self._checkout_table.locator(self._bill)
    
    @property
    def get_palce_order_button(self):
        return self._place_order_button
    
    def get_text_area(self):
        return self._text_area
    
    def click_palce_order_button(self):
        self._place_order_button.click()
        return Payment(self.page)
    
    def get_all_checkout_items(self):
        return self._checkout_table.locator("//tbody/tr")
    
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
    
    def calculate_bill(self):
        cart_items = self.get_all_checkout_items()
        cart_items_count = cart_items.count()-1
        bill = 0
        for i in range(cart_items_count):
            product = cart_items.nth(i)
            total = self.get_product_total(product).text_content().strip()
            total = total.strip("Rs. ")
            bill = bill + int(total)
        return bill
    
    def get_billing_address(self):
        number_of_fields = self._billing_address.count()
        items = []
        for i in range(1,number_of_fields):
            item = self._billing_address.nth(i)
            items.append(item.inner_text().strip())
        return items

    def get_delivery_address(self):
        number_of_fields = self._delivery_address.count()
        items = []
        for i in range(1,number_of_fields):
            item = self._billing_address.nth(i)
            items.append(item.inner_text().strip())
        return items
    
   



        
    
