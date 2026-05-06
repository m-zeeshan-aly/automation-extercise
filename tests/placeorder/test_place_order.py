from playwright.sync_api import expect
from src.pages.home.homePage import Home
from src.pages.category.categoryPage import Category


def test_place_order(use_saved_login):
    page = use_saved_login

    home_p = Home(page)
    logout_button = home_p.get_logout_button
    expect(logout_button).to_be_visible()

    category_p = Category(page)

    category = category_p.get_category(category="Men")
    expect(category).to_be_visible()

    sub_category = category_p.get_subcategory(kind="Men",section="Tshirts")
    expect(sub_category).not_to_be_visible()
    category.click()

    expect(sub_category).to_be_visible()
    specific_category_products = category_p.click_subcategory(sub_category)
    
    page.wait_for_timeout(5000)
