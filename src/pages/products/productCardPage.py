from dataclasses import dataclass
import random

@dataclass
class ProductSnapshot:
    """Immutable snapshot of a product card's visible data."""
    index: int
    description: str
    price: str
    image_src: str

class ProductCard:
    """
    Page object for the product card grid.

    Responsibilities:
      - Locate cards and their child elements
      - Extract visible data from a card
      - Return raw locators for actions (clicking is the test's job)

    NOT responsible for:
      - Navigating to other pages (tests own that)
      - Instantiating other page objects
    """

    # ── Locator templates ────────────────────────────────────────────────────
    _GRID = "xpath=.//div[@class='features_items']//div[@class='col-sm-4']"

    _SIMPLE_PRICE       = "xpath=.//div[@class='productinfo text-center']/h2"
    _SIMPLE_DESCRIPTION = "xpath=.//div[@class='productinfo text-center']/p"
    _SIMPLE_IMAGE       = "xpath=.//div[@class='productinfo text-center']/img"
    _SIMPLE_CART_BTN    = "xpath=.//div[@class='productinfo text-center']/a"

    _HOVER_PRICE        = "xpath=.//div[@class='overlay-content']/h2"
    _HOVER_DESCRIPTION  = "xpath=.//div[@class='overlay-content']/p"
    _HOVER_CART_BTN     = "xpath=.//div[@class='overlay-content']/a"

    _VIEW_PRODUCT_BTN   = "xpath=.//a[normalize-space()='View Product']"

    def __init__(self, page):
        self._page = page

    # ── Grid ─────────────────────────────────────────────────────────────────

    @property
    def all_products(self):
        return self._page.locator(self._GRID)

    def wait_for_products(self, min_count= 1):
        """Block until at least `min_count` cards are visible."""
        self.all_products.first.wait_for(state="visible")

    # ── Single-card access ────────────────────────────────────────────────────

    def get_product_at(self, index):
        return self.all_products.nth(index)

    def get_random_product(self):
        """
        Returns (card_locator, index).
        Always call wait_for_products() before this.
        """
        count = self.all_products.count()
        if count == 0:
            raise RuntimeError("No products found on the page.")
        index = random.randint(0, count - 1)
        return self.all_products.nth(index), index

    # ── Data extraction ───────────────────────────────────────────────────────

    def get_price(self, product):
        return product.locator(self._SIMPLE_PRICE).text_content().strip()

    def get_description(self, product):
        return product.locator(self._SIMPLE_DESCRIPTION).text_content().strip()

    def get_image_src(self, product):
        return product.locator(self._SIMPLE_IMAGE).get_attribute("src", timeout=3000) or ""

    def get_hover_price(self, product):
        return product.locator(self._HOVER_PRICE).text_content().strip()

    def get_hover_description(self, product):
        return product.locator(self._HOVER_DESCRIPTION).text_content().strip()

    def snapshot(self, product, index) -> ProductSnapshot:
        """
        Capture a full data snapshot of a card before any interaction.
        Use this to preserve values before hover/click changes the DOM.
        """
        return ProductSnapshot(
            index=index,
            description=self.get_description(product),
            price=self.get_price(product),
            image_src=self.get_image_src(product).lstrip("/"),
        )

    # ── Locators for actions (tests call .click() themselves) ─────────────────

    def get_view_product_button(self, product):
        return product.locator(self._VIEW_PRODUCT_BTN)

    def get_add_to_cart_button(self, product):
        """Visible button (no hover required)."""
        return product.locator(self._SIMPLE_CART_BTN)

    def get_hover_add_to_cart_button(self, product):
        """Button that appears on hover."""
        return product.locator(self._HOVER_CART_BTN)
            
