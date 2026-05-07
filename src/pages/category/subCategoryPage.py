class SubCategory:
    def __init__(self,page):
        self.page = page
        self._heading = page.locator("//h2[contains(text(),' Products')]")

    @property
    def get_heading(self):
        return self._heading
            