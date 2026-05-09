from playwright.sync_api import expect
from src.pages.home.homePage import Home
from src.pages.category.categoryPage import Category
from src.pages.products.productCardPage import ProductCard


# def xtest_verify_product_added_to_cart(use_saved_login):
#     """
#     This test ensure the followings when a prodct is added to to cart
#     The quantity must the number that we added 
#     The image of the product must along with name and price
#     This also enures that the calculated total also matches the quantity * price
#     NOTE
#     The product must not be in the cart before which could fail the test because we add and verify the quantity too
#     """
#     page = use_saved_login

#     home_p = Home(page)
#     logout_button = home_p.get_logout_button
#     expect(logout_button).to_be_visible()

#     category_p = Category(page)

#     kind ="Men"
#     sub_kind ="Tshirts"

#     category = category_p.get_category(category=kind)
#     expect(category).to_be_visible()

#     sub_category = category_p.get_subcategory(kind=kind,section=sub_kind)
#     expect(sub_category).not_to_be_visible()
#     category.click()
#     expect(sub_category).to_be_visible()

#     sub_category_p = category_p.click_subcategory(sub_category)
#     heading = sub_category_p.get_heading
#     expect(heading).to_contain_text(f"{kind} - {sub_kind} Products")
#     page.wait_for_timeout(2000)


#     product_card_p = ProductCard(page)

#     selected_product = product_card_p.select_product()
#     price = product_card_p.get_price(selected_product)
#     description = product_card_p.get_description(selected_product)
#     selected_product.hover()
#     page.wait_for_timeout(1000)
#     hover_price = product_card_p.get_price_on_hover(selected_product)
#     hover_description = product_card_p.get_description_on_hover(selected_product)
    
#     assert hover_price == price, "Price mismatch with card and on hover over the card"
#     assert hover_description == description, "Description mismatch with card and on hover over the card"

#     image = product_card_p.get_image(selected_product)
#     card_image_src = image.get_attribute("src").lstrip("/")

#     # This piece of code adds product twice in the cart and at second attampt it move to the cart page
#     # So the Total = 2*price and the quantity = 2, verify this at cart page

#     add_to_cart_button = product_card_p.get_add_to_cart_button(selected_product)
#     page.wait_for_timeout(1000)
#     cart_popup = product_card_p.click_add_to_cart(add_to_cart_button)
#     heading = cart_popup.get_heading
#     expect(heading).to_have_text("Added!")
#     page.wait_for_timeout(1000)

#     cart_popup.click_continue_shoping()
#     cart_popup = product_card_p.click_add_to_cart(add_to_cart_button)
#     heading = cart_popup.get_heading
#     expect(heading).to_have_text("Added!")
#     cart_p = cart_popup.click_view_cart_button()
#     checkout_button = cart_p.get_checkout_button

#     expect(checkout_button).to_be_visible()
   

#     expect(cart_p.get_cart_empty).not_to_be_visible()
#     # verified that cart is not empty

#     cart_items = cart_p.get_all_cart_items()

#     number_of_items = cart_items.count()
#     # recently added product goes to the end 
#     # so we must select that item from the cart to verify that we added the right product
#     last_item = number_of_items -1

#     item = cart_items.nth(last_item)

#     p_price = cart_p.get_product_price(item).text_content().strip()
#     p_price = p_price.strip("Rs. ")

#     quantity = cart_p.get_product_quantity(item).text_content().strip()

#     expect(cart_p.get_product_name(item)).to_have_text(description)
#     expect(cart_p.get_product_price(item)).to_have_text(price)
#     # remember we added the same item twice in the cart
#     expect(cart_p.get_product_quantity(item)).to_have_text("2")

#     expect(cart_p.get_product_total(item)).to_have_text("Rs. "+str(int(quantity)*int(p_price)))
    
#     cart_image_src = cart_p.get_product_image_src(item).get_attribute("src").lstrip("/")
#     assert card_image_src == cart_image_src, "Image Mismatch"

#     page.wait_for_timeout(2000)






# completed
def xtest_verify_product_added_to_cart(use_saved_login):
    """
    This test ensure the followings when a prodct is added to to cart
    The image of the product must along with name and price
    This also enures that the calculated total also matches the quantity * price
    """
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
    card_image_src = image.get_attribute("src").lstrip("/")

    # This piece of code adds product twice in the cart and at second attampt it move to the cart page
    # So the mimum Total = 2*price if the prduct was not already added in the cart.

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
    
    expect(cart_p.get_cart_empty).not_to_be_visible()
    # verified that cart is not empty
    checkout_button = cart_p.get_checkout_button
    expect(checkout_button).to_be_visible()
    page.wait_for_timeout(1000)
    # This button i also visible when cart has items

    cart_items = cart_p.get_all_cart_items()

    number_of_items = cart_items.count()
    # recently added product goes to the end 
    # so we must select that item from the cart to verify that we added the right product
    last_item = number_of_items -1

    item = cart_items.nth(last_item)

    p_price = cart_p.get_product_price(item).text_content().strip()
    p_price = p_price.strip("Rs. ")

    quantity = cart_p.get_product_quantity(item).text_content().strip()

    expect(cart_p.get_product_name(item)).to_have_text(description)
    expect(cart_p.get_product_price(item)).to_have_text(price)

    expect(cart_p.get_product_total(item)).to_have_text("Rs. "+str(int(quantity)*int(p_price)))
    
    cart_image_src = cart_p.get_product_image_src(item).get_attribute("src").lstrip("/")
    assert card_image_src == cart_image_src, "Image Mismatch"

    cart_items_total_amount = cart_p.get_bill()

    checkout_p = cart_p.click_checkout_button()

    expect(checkout_p.get_heading).to_be_visible()
    page.wait_for_timeout(2000)




# not completed  yet
def xtest_verify_product_deleted_from_cart(use_saved_login):
    """
    This test ensure the followings when a prodct is added to to cart
    The image of the product must along with name and price
    This also enures that the calculated total also matches the quantity * price
    """
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
    card_image_src = image.get_attribute("src").lstrip("/")

    # This piece of code adds product twice in the cart and at second attampt it move to the cart page
    # So the mimum Total = 2*price if the prduct was not already added in the cart.

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
    
    expect(cart_p.get_cart_empty).not_to_be_visible()
    # verified that cart is not empty
    checkout_button = cart_p.get_checkout_button
    expect(checkout_button).to_be_visible()
    page.wait_for_timeout(1000)
    # This button i also visible when cart has items

    cart_items = cart_p.get_all_cart_items()

    number_of_items = cart_items.count()
    # recently added product goes to the end 
    # so we must select that item from the cart to verify that we added the right product
    last_item = number_of_items -1

    item = cart_items.nth(last_item)

    p_price = cart_p.get_product_price(item).text_content().strip()
    p_price = p_price.strip("Rs. ")

    quantity = cart_p.get_product_quantity(item).text_content().strip()

    expect(cart_p.get_product_name(item)).to_have_text(description)
    expect(cart_p.get_product_price(item)).to_have_text(price)

    expect(cart_p.get_product_total(item)).to_have_text("Rs. "+str(int(quantity)*int(p_price)))
    
    cart_image_src = cart_p.get_product_image_src(item).get_attribute("src").lstrip("/")
    assert card_image_src == cart_image_src, "Image Mismatch"

    cart_items_total_amount = cart_p.get_bill()


    page.wait_for_timeout(2000)