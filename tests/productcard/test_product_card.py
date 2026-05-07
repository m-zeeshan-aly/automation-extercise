from playwright.sync_api import expect
from src.pages.home.homePage import Home
from src.pages.category.categoryPage import Category
from src.pages.products.productCardPage import ProductCard

def xtest_product_card_hover(use_saved_login):
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

    for i in range(3):
        selected_product = product_card_p.select_product()
        price = product_card_p.get_price(selected_product)
        description = product_card_p.get_description(selected_product)
        selected_product.hover()
        page.wait_for_timeout(1000)
        hover_price = product_card_p.get_price_on_hover(selected_product)
        hover_description = product_card_p.get_description_on_hover(selected_product)
        
        assert hover_price == price, "Price mismatch with card and on hover over the card"
        assert hover_description == description, "Description mismatch with card and on hover over the card"

    page.wait_for_timeout(2000)




def xtest_product_card_view_product_button_navigation(use_saved_login):
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
    
    view_product_button = product_card_p.get_view_product_button(selected_product)
    page.wait_for_timeout(1000)

    product_detail_p = product_card_p.click_view_product(view_product_button)

    tab = product_detail_p.get_product_tab

    expect(tab).to_have_css("color", "rgb(255, 165, 0)")

    page.wait_for_timeout(2000)






def xtest_product_card_add_to_cart_button(use_saved_login):
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
    
    add_to_cart_button = product_card_p.get_add_to_cart_button(selected_product)
    page.wait_for_timeout(1000)
    cart_popup = product_card_p.click_add_to_cart(add_to_cart_button)
    heading = cart_popup.get_heading
    expect(heading).to_have_text("Added!")
    page.wait_for_timeout(1000)

    cart_popup.click_continue_shoping()
    cart_popup = product_card_p.click_add_to_cart(add_to_cart_button)
    heading = cart_popup.get_heading
    expect(heading).to_have_text("Added!")
    cart_p = cart_popup.click_view_cart_button()
    checkout_button = cart_p.get_checkout_button

    expect(checkout_button).to_be_visible()

    page.wait_for_timeout(2000)
