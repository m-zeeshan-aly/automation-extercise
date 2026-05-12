from playwright.sync_api import expect
from src.pages.home.homePage import Home
from src.pages.category.categoryPage import Category
from src.pages.products.productCardPage import ProductCard
from src.utils.generatedata.generateDataUtils import GenerateData
import os

def xtest_place_order_and_clicks_continue_button(use_saved_login):
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

    cart_popup.click_continue_shopping()
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

    place_order_button = checkout_p.get_place_order_button

    expect(place_order_button).to_be_visible()

    bill = checkout_p.get_bill.text_content().strip()
    bill = bill.strip("Rs. ")

    calculated_bill = checkout_p.calculate_bill()
    assert cart_items_total_amount == int(bill), "Bill Amount Mismatch"

    text_field = checkout_p.get_text_area()
    text_field.clear()
    expect(text_field).to_be_empty()
    text_field.fill("Do not bring order after 5pm")

    expect(text_field).to_have_value("Do not bring order after 5pm")

    assert checkout_p.get_billing_address() == checkout_p.get_delivery_address(),"Address Mismatch error"


    page.wait_for_timeout(1000)
    payment_p = checkout_p.click_place_order_button()

    expect(payment_p.get_heading).to_have_text("Payment")

    generate_data = GenerateData()
    card_data = generate_data.get_payment_data()

    input = payment_p.get_input_field("name_on_card")
    input.clear()
    expect(input).to_be_empty()
    input.fill(card_data.get("name"))

    input = payment_p.get_input_field("card_number")
    input.clear()
    expect(input).to_be_empty()
    input.fill(card_data.get("card_number"))

    input = payment_p.get_input_field("cvc")
    input.clear()
    expect(input).to_be_empty()
    input.fill(card_data.get("cvc"))

    input = payment_p.get_input_field("expiry_month")
    input.clear()
    expect(input).to_be_empty()
    input.fill(card_data.get("mm"))

    input = payment_p.get_input_field("expiry_year")
    input.clear()
    expect(input).to_be_empty()
    input.fill(card_data.get("year"))
    page.wait_for_timeout(1000)

    payment_button = payment_p.get_submit_button

    expect(payment_button).to_be_visible()

    order_success_p = payment_p.click_submit_button()
    page.wait_for_timeout(1000)

    expect(order_success_p.get_success_message).to_have_text('Congratulations! Your order has been confirmed!')
    
    button = order_success_p.get_button("Continue")
    home_p = order_success_p.click_continue_button(button)
    button = home_p.get_cart_button
    expect(button).to_be_visible()
    page.wait_for_timeout(1000)

    cart_p = home_p.click_cart_button()
    expect(cart_p.get_cart_empty).to_be_visible()

    page.wait_for_timeout(1000)



def xtest_place_order_and_clicks_download_invoice_button(use_saved_login):
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

    cart_popup.click_continue_shopping()
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

    place_order_button = checkout_p.get_place_order_button

    expect(place_order_button).to_be_visible()

    bill = checkout_p.get_bill.text_content().strip()
    bill = bill.strip("Rs. ")

    calculated_bill = checkout_p.calculate_bill()
    assert cart_items_total_amount == int(bill), "Bill Amount Mismatch"

    text_field = checkout_p.get_text_area()
    text_field.clear()
    expect(text_field).to_be_empty()
    text_field.fill("Do not bring order after 5pm")

    expect(text_field).to_have_value("Do not bring order after 5pm")

    assert checkout_p.get_billing_address() == checkout_p.get_delivery_address(),"Address Mismatch error"


    page.wait_for_timeout(1000)
    payment_p = checkout_p.click_place_order_button()

    expect(payment_p.get_heading).to_have_text("Payment")

    generate_data = GenerateData()
    card_data = generate_data.get_payment_data()

    input = payment_p.get_input_field("name_on_card")
    input.clear()
    expect(input).to_be_empty()
    input.fill(card_data.get("name"))

    input = payment_p.get_input_field("card_number")
    input.clear()
    expect(input).to_be_empty()
    input.fill(card_data.get("card_number"))

    input = payment_p.get_input_field("cvc")
    input.clear()
    expect(input).to_be_empty()
    input.fill(card_data.get("cvc"))

    input = payment_p.get_input_field("expiry_month")
    input.clear()
    expect(input).to_be_empty()
    input.fill(card_data.get("mm"))

    input = payment_p.get_input_field("expiry_year")
    input.clear()
    expect(input).to_be_empty()
    input.fill(card_data.get("year"))
    page.wait_for_timeout(1000)

    payment_button = payment_p.get_submit_button

    expect(payment_button).to_be_visible()

    order_success_p = payment_p.click_submit_button()
    page.wait_for_timeout(1000)

    expect(order_success_p.get_success_message).to_have_text('Congratulations! Your order has been confirmed!')

    page.wait_for_timeout(1000)

    # 1. Define your specific path
    download_dir = "./downloads"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    file_path = os.path.join(download_dir, "invoice.pdf")

    # 2. Start waiting for the download before clicking
    with page.expect_download() as download_info:
        button = order_success_p.get_button("Download Invoice")
        button.click()
    
    download = download_info.value
    
    # 3. Save the file to your specific path
    download.save_as(file_path)

    # 4. Final Assertions
    assert os.path.exists(file_path), f"Download failed: {file_path} not found"
    assert os.path.getsize(file_path) > 0, "Downloaded file is empty"
    
    print(f"File successfully downloaded to: {download.path()}")
