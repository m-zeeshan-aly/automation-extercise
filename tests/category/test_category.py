from playwright.sync_api import expect
from src.pages.home.homePage import Home
from src.pages.category.categoryPage import Category
from src.utils.constants.constantsUtils import CATEGORIES, BRANDS
import pytest 

@pytest.mark.parametrize("kind", CATEGORIES.keys()) 
def xtest_click_category(use_saved_login,kind):
    page = use_saved_login

    home_p = Home(page)
    logout_button = home_p.get_logout_button
    expect(logout_button).to_be_visible()

    category_p = Category(page)

    category = category_p.get_category(category=kind)
    expect(category).to_be_visible()

    sub_category = category_p.get_subcategory(kind=kind,section=CATEGORIES[kind][0])
    expect(sub_category).not_to_be_visible()
    category.click()
    expect(sub_category).to_be_visible()
    
    page.wait_for_timeout(1000)




@pytest.mark.parametrize("brand", BRANDS) 
def xtest_click_brand(use_saved_login,brand):
    page = use_saved_login

    home_p = Home(page)
    logout_button = home_p.get_logout_button
    expect(logout_button).to_be_visible()

    category_p = Category(page)

    brand_loc = category_p.get_brand(brand)
    expect(brand_loc).to_be_visible()

    expect(brand_loc).to_contain_text(brand)
    page.wait_for_timeout(1000)

    sub_category = category_p.click_brand(brand_loc)
    page.wait_for_timeout(2000)

    heading = sub_category.get_heading

    expect(heading).to_contain_text(brand)

    
    page.wait_for_timeout(1000)
