class SubCategory:
    # CATEGORY = "//div[@id='accordian']//a[normalize-space()= '{category}']"
    # SUB_CATEGORY = "//div[@id='{kind}']//a[normalize-space()='{section}']"
    def __init__(self,page):
        self.page = page

    # def get_category(self,category):
    #     return self.page.locator(self.CATEGORY.format(category=category))
    
    # def get_subcategory(self,kind,section):
    #     return self.page.locator(self.SUB_CATEGORY.format(kind=kind,section=section))
    
    # def click_subcategory(self,sub_category):
    #     sub_category.click()
    #     return self
        
            