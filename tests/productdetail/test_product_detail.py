from playwright.sync_api import expect
from src.pages.home.homePage import Home
from src.pages.category.categoryPage import Category
from src.pages.products.productCardPage import ProductCard


def test_verify_selected_product_details(use_saved_login):
    page = use_saved_login

    home_p = Home(page)
    logout_button = home_p.get_logout_button
    expect(logout_button).to_be_visible()

    category_p = Category(page)

    kind ="Men"
    sub_kind ="Tshirts"

    category = category_p.get_category(category=kind)
    expect(category).to_be_visible()

    sub_category = category_p.get_subcategory(kind=kind,section=sub_kind)
    expect(sub_category).not_to_be_visible()
    category.click()
    expect(sub_category).to_be_visible()

    sub_category_p = category_p.click_subcategory(sub_category)
    heading = sub_category_p.get_heading
    expect(heading).to_contain_text(f"{kind} - {sub_kind} Products")
    page.wait_for_timeout(2000)


    product_card_p = ProductCard(page)

    selected_product = product_card_p.select_product()
    price = product_card_p.get_price(selected_product)
    description = product_card_p.get_description(selected_product)
    selected_product.hover()
    page.wait_for_timeout(1000)
    hover_price = product_card_p.get_price_on_hover(selected_product)
    hover_description = product_card_p.get_description_on_hover(selected_product)
    
    assert hover_price == price, "Price mismatch with card and on hover over the card"
    assert hover_description == description, "Description mismatch with card and on hover over the card"

    image = product_card_p.get_image(selected_product)
    card_image_src = image.get_attribute("src")
    
    view_product_button = product_card_p.get_view_product_button(selected_product)
    page.wait_for_timeout(1000)

    product_detail_p = product_card_p.click_view_product(view_product_button)

    tab = product_detail_p.get_product_tab

    expect(tab).to_have_css("color", "rgb(255, 165, 0)")

    product_description_locator = product_detail_p.get_description
    product_price_locator = product_detail_p.get_product_price
    product_image_locator = product_detail_p.get_product_image

    expect(product_description_locator).to_have_text(description)
    expect(product_price_locator).to_have_text(price)

    detail_image_src = product_image_locator.get_attribute("src")

    # print("Card image src:", card_image_src)
    # print("Detail image src:", detail_image_src)

    assert card_image_src == detail_image_src, "Image Mismatch"

    page.wait_for_timeout(2000)

