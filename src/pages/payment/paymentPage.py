class Payment:
    INPUT = "//input[@name='{name}']"
    def __init__(self,page):
        self.page = page
        self._heading = page.locator("//h2[normalize-space()='Payment']")
        self._submit_button = page.locator("//button[@id='submit']")
    @property
    def get_heading(self):
        return self._heading
    
    @property
    def get_submit_button(self):
        return self._submit_button

    def get_input_field(self, name):
        return self.page.locator(self.INPUT.format(name=name))
    