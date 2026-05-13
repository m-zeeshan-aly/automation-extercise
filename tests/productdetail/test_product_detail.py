from playwright.sync_api import expect
from src.pages.home.homePage import Home
from src.pages.category.categoryPage import Category
from src.pages.category.subCategoryPage import SubCategory
from src.pages.products.productCardPage import ProductCard
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

def xtest_verify_selected_product_details_match_card(use_saved_login):
    """
    Verify that the product details page correctly reflects the 
    data (name, price, image) shown on the product card.
    """
    page = use_saved_login
    
    # 1. Navigation using centralized helper
    _navigate_to_subcategory(page, KIND, SUB_KIND)

    # 2. Product Selection and Snapshot
    product_card_p = ProductCard(page)
    product_card_p.wait_for_products()
    
    product, index = product_card_p.get_random_product()
    
    # Capture data using ControlUtils to ensure clean strings
    description = ControlUtils.get_clean_text(product_card_p.description_locator(product))
    price = ControlUtils.get_clean_text(product_card_p.price_locator(product))
    image_src = ControlUtils.get_clean_attribute(product_card_p.image_locator(product), "src")
    
    # Creating snapshot for structured comparison
    snapshot = product_card_p.snapshot(index, description, price, image_src)

    # 3. Hover Validation (Internal consistency check)
    product.hover()
    page.wait_for_timeout(500)
    
    hover_price = ControlUtils.get_clean_text(product_card_p.hover_price_locator(product))
    hover_desc = ControlUtils.get_clean_text(product_card_p.hover_description_locator(product))
    
    assert hover_price == snapshot.price, f"Hover price mismatch! Expected {snapshot.price}"
    assert hover_desc == snapshot.description, f"Hover description mismatch! Expected {snapshot.description}"

    # 4. Navigation to Product Details
    view_product_button = product_card_p.get_view_product_button(product)
    page = ControlUtils.click_on_element(view_product_button)
    
    product_detail_p = ProductDetail(page)

    # 5. Detail Page Assertions
    # Verify the "Product" tab is active/highlighted
    tab = product_detail_p.get_product_tab
    expect(tab).to_have_css("color", "rgb(255, 165, 0)")

    # Validate Name and Price on details page
    ControlUtils.validate_element_have_text(product_detail_p.get_description, snapshot.description)
    ControlUtils.validate_element_have_text(product_detail_p.get_product_price, snapshot.price)

    # Validate Image Source
    detail_image_src = ControlUtils.get_clean_attribute(product_detail_p.get_product_image, "src")
    assert snapshot.image_src == detail_image_src, (
        f"Image mismatch! Card: {snapshot.image_src}, Details: {detail_image_src}"
    )

    # Optional stabilization wait for visual debugging
    page.wait_for_timeout(2000)