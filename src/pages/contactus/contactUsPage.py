class ContactUs:
    INPUT = "//input[@name='{name}']"
    def __init__(self,page):
        self.page = page 
        self._heading  = page.locator("//div[@class='col-sm-12']//h2[@class='title text-center']")
        self._message_text = page.locator("//textarea[@id='message']")
        self._home_button = page.locator("//div[@id='form-section']/a")
        self._success_message = page.locator("//div[@class='status alert alert-success']")
        

    @property
    def get_heading(self):
        return self._heading
    
    @property
    def success_message(self):
        return self._success_message
    
    def click_home_button(self):
        self._home_button.click()
        from src.pages.home.homePage import Home
        return Home(self.page)
    
    
    def get_message_field(self):
        return self._message_text
    
    def get_input(self,name):
        return self.page.locator(self.INPUT.format(name=name))
    