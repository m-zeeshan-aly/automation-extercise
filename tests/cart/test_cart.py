from playwright.sync_api import expect
from src.pages.cart.cartPage import Cart
from src.pages.cart.cartPopupPage import CartPopup
from src.pages.category.categoryPage import Category
from src.pages.category.subCategoryPage import SubCategory
from src.pages.home.homePage import Home
from src.pages.login.loginPage import Login
from src.pages.products.productCardPage import ProductCard
from src.utils.constants.constantsUtils import KIND, SUB_KIND
from src.utils.controlutils.controlUtils import ControlUtils

def _navigate_to_subcategory(page, kind, sub_kind):
    """
    Navigate Home → Category → SubCategory.
    Returns the SubCategory page object.
    """
    home = Home(page)
    ControlUtils.validate_element_is_visible(home.get_button("Logout"))

    category_p = Category(page)
    ControlUtils.validate_element_is_visible(category_p.get_category(category=kind))
    ControlUtils.click_on_element(category_p.get_category(category=kind))

    ControlUtils.validate_element_is_visible(
        category_p.get_subcategory(kind=kind, section=sub_kind)
    )
    ControlUtils.click_on_element(category_p.get_subcategory(kind=kind, section=sub_kind))

    sub_category_p = SubCategory(page)
    ControlUtils.validate_element_have_text(
        sub_category_p.get_heading, f"{kind} - {sub_kind} Products"
    )
    return sub_category_p


def _add_product_to_cart_twice(page, product_card_p):
    """
    Selects a random product, adds it to the cart twice
    (first time: continue shopping; second time: view cart).

    Returns (CartPopup after second add, ProductSnapshot).
    """
    product_card_p.wait_for_products()
    product, index = product_card_p.get_random_product()
    description=ControlUtils.get_clean_text(product_card_p.description_locator(product))
    price=ControlUtils.get_clean_text(product_card_p.price_locator(product))
    # Handling specific cleaning like lstrip inside the snapshot logic
    image_src=ControlUtils.get_clean_attribute(product_card_p.image_locator(product), "src").lstrip("/")
    snapshot = product_card_p.snapshot(index,description,price,image_src)

    # Verify hover data matches card data
    product.hover()
    page.wait_for_timeout(500)

    # Capture the UI values once
    hover_price = ControlUtils.get_clean_text(product_card_p.hover_price_locator(product))
    hover_desc = ControlUtils.get_clean_text(product_card_p.hover_description_locator(product))

    assert hover_price == snapshot.price, f"Price mismatch! Expected {snapshot.price!r} but got {hover_price!r}"
    assert hover_desc == snapshot.description, f"Desc mismatch! Expected {snapshot.description!r} but got {hover_desc!r}"

    page = ControlUtils.click_on_element(product_card_p.get_add_to_cart_button(product))

    popup = CartPopup(page)
    ControlUtils.validate_element_have_text(popup.get_heading, "Added!")
    ControlUtils.click_on_element(popup.get_continue_shopping_button)

    page = ControlUtils.click_on_element(product_card_p.get_add_to_cart_button(product))
    popup = CartPopup(page)
    ControlUtils.validate_element_have_text(popup.get_heading, "Added!")

    return popup, snapshot


def _parse_price(raw: str) -> int:
    """Convert 'Rs. 500' → 500. Raises ValueError on bad input."""
    return int(raw.replace("Rs.", "").strip())


def test_verify_product_added_to_cart(use_saved_login):
    """
    Verify that after adding a product to the cart:
      - The cart is not empty
      - Product name, price, and image in the cart match the product card
      - Total = quantity × unit price
      - Checkout button is visible
    """
    page = use_saved_login
    _navigate_to_subcategory(page, KIND, SUB_KIND)

    product_card_p = ProductCard(page)
    popup, snapshot = _add_product_to_cart_twice(page, product_card_p)

    page = ControlUtils.click_on_element(popup.get_view_cart_button)
    cart_p = Cart(page)
    ControlUtils.validate_element_is_visible(cart_p.get_checkout_button)

    target_row = cart_p.get_row_by_name(snapshot.description)
    
    # Ensure that specific row is visible before asserting
    ControlUtils.validate_element_is_visible(target_row)

    unit_price = _parse_price(
        ControlUtils.get_clean_text(cart_p.get_product_price(target_row))
    )
    quantity = int(cart_p.get_product_quantity(target_row).text_content().strip())
    expected_total = f"Rs. {unit_price * quantity}"

    ControlUtils.validate_element_have_text(cart_p.get_product_name(target_row), snapshot.description)
    ControlUtils.validate_element_have_text(cart_p.get_product_price(target_row), snapshot.price)
    ControlUtils.validate_element_have_text(cart_p.get_product_total(target_row), expected_total)

    cart_image_src = (
        cart_p.get_product_image_src(target_row).get_attribute("src") or ""
    ).lstrip("/")
    assert cart_image_src == snapshot.image_src, (
        f"Image mismatch — card: {snapshot.image_src!r}, cart: {cart_image_src!r}"
    )


def test_verify_product_deleted_from_cart(use_saved_login):
    """
    Verify that deleting a product from the cart reduces the item count by one.
    """
    page = use_saved_login
    _navigate_to_subcategory(page, KIND, SUB_KIND)

    product_card_p = ProductCard(page)
    popup, _ = _add_product_to_cart_twice(page, product_card_p)

    page = ControlUtils.click_on_element(popup.get_view_cart_button)
    cart_p = Cart(page)
    cart_items = cart_p.get_all_cart_items()
    count_before = cart_items.count()

    last_item = cart_items.nth(count_before - 1)
    page = ControlUtils.click_on_element(cart_p.get_delete_button(last_item))
    page.reload(wait_until="networkidle")

    count_after = cart_p.get_all_cart_items().count()
    assert count_after < count_before, (
        f"Item was not deleted — count before: {count_before}, after: {count_after}"
    )

def test_unauthenticated_checkout_redirects_to_login(setup):
    """
    Verify that an unauthenticated user attempting checkout
    is redirected to the Login/Signup page.
    """
    page = setup
    home_p = Home(page)
    ControlUtils.click_on_element(home_p.get_nav_link("products"))

    sub_p = SubCategory(page)
    ControlUtils.validate_element_have_text(sub_p.get_heading, "All Products")

    product_card_p = ProductCard(page)
    product_card_p.wait_for_products()
    product, index = product_card_p.get_random_product()

    # description=ControlUtils.get_clean_text(product_card_p.description_locator(product)),
    # price=ControlUtils.get_clean_text(product_card_p.price_locator(product)),
    # image_src=ControlUtils.get_clean_attribute(product_card_p.image_locator(product), "src").lstrip("/")
    # snapshot = product_card_p.snapshot(index,description,price,image_src)


    page = ControlUtils.click_on_element(product_card_p.get_add_to_cart_button(product))

    popup = CartPopup(page)
    ControlUtils.validate_element_have_text(popup.get_heading, "Added!")
    ControlUtils.click_on_element(popup.get_continue_shopping_button)

    page = ControlUtils.click_on_element(product_card_p.get_add_to_cart_button(product))
    popup = CartPopup(page)
    ControlUtils.validate_element_have_text(popup.get_heading, "Added!")

    page = ControlUtils.click_on_element(popup.get_view_cart_button)
    cart_p = Cart(page)

    expect(cart_p.get_cart_empty).not_to_be_visible()
    ControlUtils.click_on_element(cart_p.get_checkout_button)

    ControlUtils.validate_element_is_visible(popup.get_checkout_heading)
    page = ControlUtils.click_on_element(popup.get_login_signup_button)
    login_p = Login(page)
    ControlUtils.validate_element_is_visible(login_p.signup_header)