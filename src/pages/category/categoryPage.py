class Category:
    CATEGORY = "//div[@id='accordian']//a[normalize-space()= '{category}']"
    SUB_CATEGORY = "//div[@id='{kind}']//a[normalize-space()='{section}']"
    BRAND = "//div[@class='brands-name']//a[contains(@href,'/{brand}')]"
    def __init__(self,page):
        self.page = page

    def get_category(self,category):
        return self.page.locator(self.CATEGORY.format(category=category))
    
    def get_brand(self,brand):
        return self.page.locator(self.BRAND.format(brand = brand))
    
    def get_subcategory(self,kind,section):
        return self.page.locator(self.SUB_CATEGORY.format(kind=kind,section=section))