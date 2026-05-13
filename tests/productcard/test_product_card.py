from playwright.sync_api import expect
from src.pages.home.homePage import Home
from src.pages.category.categoryPage import Category
from src.pages.category.subCategoryPage import SubCategory
from src.pages.products.productCardPage import ProductCard
from src.pages.cart.cartPopupPage import CartPopup
from src.pages.cart.cartPage import Cart
from src.pages.products.productDetailPage import ProductDetail
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


def xtest_product_card_hover_validation(use_saved_login):
    """
    Verify that hovering over a product card displays correct 
    price and description matching the static card data.
    """
    page = use_saved_login
    _navigate_to_subcategory(page, KIND, SUB_KIND)

    product_card_p = ProductCard(page)
    product_card_p.wait_for_products()

    # Testing 3 random products to ensure UI consistency
    for _ in range(3):
        product, index = product_card_p.get_random_product()
        
        # Capture static data
        card_price = ControlUtils.get_clean_text(product_card_p.price_locator(product))
        card_desc = ControlUtils.get_clean_text(product_card_p.description_locator(product))
        
        # Perform hover
        product.hover()
        page.wait_for_timeout(500) 

        # Capture hover data
        hover_price = ControlUtils.get_clean_text(product_card_p.hover_price_locator(product))
        hover_desc = ControlUtils.get_clean_text(product_card_p.hover_description_locator(product))
        
        assert hover_price == card_price, f"Price mismatch! Card: {card_price}, Hover: {hover_price}"
        assert hover_desc == card_desc, f"Desc mismatch! Card: {card_desc}, Hover: {hover_desc}"

        page.wait_for_timeout(2000)


def xtest_product_card_view_product_navigation(use_saved_login):
    """
    Verify that clicking 'View Product' navigates to the details page
    and the 'Product' tab is correctly highlighted.
    """
    page = use_saved_login
    _navigate_to_subcategory(page, KIND, SUB_KIND)

    product_card_p = ProductCard(page)
    product_card_p.wait_for_products()
    
    product, _ = product_card_p.get_random_product()
    view_btn = product_card_p.get_view_product_button(product)
    
    # Navigate to Details
    page = ControlUtils.click_on_element(view_btn)
    product_detail_p = ProductDetail(page)
    
    # Validate highlight color (Orange: rgb(255, 165, 0))
    tab = product_detail_p.get_product_tab
    expect(tab).to_have_css("color", "rgb(255, 165, 0)")

    page.wait_for_timeout(2000)


def xtest_product_card_add_to_cart_and_popup_flow(use_saved_login):
    """
    Verify the full flow of adding an item, continuing shopping, 
    re-adding, and navigating to the cart.
    """
    page = use_saved_login
    _navigate_to_subcategory(page, KIND, SUB_KIND)

    product_card_p = ProductCard(page)
    product_card_p.wait_for_products()
    product, _ = product_card_p.get_random_product()
    
    # 1. First Add & Continue
    ControlUtils.click_on_element(product_card_p.get_add_to_cart_button(product))
    popup = CartPopup(page)
    ControlUtils.validate_element_have_text(popup.get_heading, "Added!")
    ControlUtils.click_on_element(popup.get_continue_shopping_button)

    # 2. Second Add & View Cart
    ControlUtils.click_on_element(product_card_p.get_add_to_cart_button(product))
    ControlUtils.validate_element_have_text(popup.get_heading, "Added!")
    
    page = ControlUtils.click_on_element(popup.get_view_cart_button)
    cart_p = Cart(page)
    
    # Final Validation
    ControlUtils.validate_element_is_visible(cart_p.get_checkout_button)
    expect(cart_p.get_cart_empty).not_to_be_visible()
    page.wait_for_timeout(2000)