import os
import pytest
from src.pages.home.homePage import Home
from src.pages.cart.cartPage import Cart
from src.pages.products.productCardPage import ProductCard
from src.pages.checkout.checkoutPage import Checkout
from src.pages.payment.paymentPage import Payment
from src.pages.ordersuccess.orderSuccessPage import OrderSuccess
from src.utils.constants.constantsUtils import KIND, SUB_KIND
from src.utils.controlutils.controlUtils import ControlUtils
from src.utils.generatedata.generateDataUtils import GenerateData
from src.pages.cart.cartPopupPage import CartPopup
from src.utils.constants.constantsUtils import ORDER_COMMENTS
import random


# --- Helpers ---
def _parse_price(raw: str) -> int:
    """Convert 'Rs. 500' → 500. Raises ValueError on bad input."""
    return int(raw.replace("Rs.", "").strip())
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


def _navigate_to_subcategory(page, kind, sub_kind):
    home = Home(page)
    ControlUtils.validate_element_is_visible(home.get_button("Logout"))
    
    from src.pages.category.categoryPage import Category
    category_p = Category(page)
    ControlUtils.click_on_element(category_p.get_category(category=kind))
    ControlUtils.click_on_element(category_p.get_subcategory(kind=kind, section=sub_kind))
    return page

def _prepare_order_until_checkout(page):
    """Navigates, adds items, verifies cart, and reaches checkout page."""
    _navigate_to_subcategory(page, KIND, SUB_KIND)
    
    product_card_p = ProductCard(page)
    popup, snapshot = _add_product_to_cart_twice(page, product_card_p)
    
    page = ControlUtils.click_on_element(popup.get_view_cart_button)
    cart_p = Cart(page)
    
    # Capture bill from cart
    cart_total = cart_p.get_bill()
    
    page = ControlUtils.click_on_element(cart_p.get_checkout_button)
    checkout_p = Checkout(page)
    ControlUtils.validate_element_is_visible(checkout_p.get_heading)
    
    return checkout_p, cart_total

def _fill_payment_details(payment_p):
    """Fills payment form using the 'Fill and Validate' pattern."""
    generate_data = GenerateData()
    data = generate_data.get_payment_data()
    
    fields = [
        ("name_on_card", data.get("name")),
        ("card_number", data.get("card_number")),
        ("cvc", data.get("cvc")),
        ("expiry_month", data.get("mm")),
        ("expiry_year", data.get("year")),
    ]
    
    for field_name, value in fields:
        locator = payment_p.get_input_field(field_name)
        ControlUtils.fill_input_field(locator, value)
        ControlUtils.validate_input(locator, value)

# --- Tests ---

@pytest.mark.parametrize("run", range(1))
def test_place_order_and_clicks_continue_button(use_saved_login, run):
    page = use_saved_login
    checkout_p, cart_total = _prepare_order_until_checkout(page)

    # 1. Checkout Page Validations
    bill_text = ControlUtils.get_clean_text(checkout_p.get_bill).replace("Rs. ", "")
    assert cart_total == int(bill_text), f"Bill mismatch! Cart: {cart_total}, Checkout: {bill_text}"
    
    # Address Validation
    assert checkout_p.get_billing_address() == checkout_p.get_delivery_address(), "Address Mismatch"

    ControlUtils.fill_input_field(checkout_p.get_text_area(), random.choice(ORDER_COMMENTS))
    ControlUtils.validate_input(checkout_p.get_text_area(), random.choice(ORDER_COMMENTS))

    # 2. Payment Flow
    page = ControlUtils.click_on_element(checkout_p.get_place_order_button)
    payment_p = Payment(page)
    _fill_payment_details(payment_p)
    
    page = ControlUtils.click_on_element(payment_p.get_submit_button)
    order_success_p = OrderSuccess(page)
    
    # 3. Final Success & Verification
    ControlUtils.validate_element_have_text(
        order_success_p.get_success_message, 
        "Congratulations! Your order has been confirmed!"
    )
    
    page = ControlUtils.click_on_element(order_success_p.get_button("Continue"))
    home_p = Home(page)
    
    # Verify cart is now empty
    page = ControlUtils.click_on_element(home_p.get_nav_link("view_cart"))
    cart_p = Cart(page)
    ControlUtils.validate_element_is_visible(cart_p.get_cart_empty)


@pytest.mark.parametrize("run", range(1))
def test_place_order_and_clicks_download_invoice_button(use_saved_login, run):
    page = use_saved_login
    checkout_p, _ = _prepare_order_until_checkout(page)
    page.wait_for_timeout(2000)

    # # Address Validation
    assert checkout_p.get_billing_address() == checkout_p.get_delivery_address(), "Address Mismatch"
    ControlUtils.fill_input_field(checkout_p.get_text_area(), random.choice(ORDER_COMMENTS))
    ControlUtils.validate_input(checkout_p.get_text_area(), random.choice(ORDER_COMMENTS))

    # Navigate to Payment
    page = ControlUtils.click_on_element(checkout_p.get_place_order_button)
    payment_p = Payment(page)
    _fill_payment_details(payment_p)
    
    page = ControlUtils.click_on_element(payment_p.get_submit_button)
    order_success_p = OrderSuccess(page)

    # Download Logic
    download_dir = "./downloads"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    file_path = os.path.join(download_dir, "invoice.pdf")

    with page.expect_download() as download_info:
        # Use ControlUtils for the click even during download expectation
        ControlUtils.click_on_element(order_success_p.get_button("Download Invoice"))
    
    download = download_info.value
    download.save_as(file_path)

    # Assertions
    assert os.path.exists(file_path), "Invoice file not found"
    assert os.path.getsize(file_path) > 0, "Invoice file is empty"