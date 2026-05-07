from playwright.sync_api import expect
from src.pages.home.homePage import Home
from src.pages.category.categoryPage import Category
from src.utils.constants.constantsUtils import CATEGORIES
import pytest 

def get_data():
    result =[]
    list_of_tuples=CATEGORIES.items()
    for key, value_list in list_of_tuples:
        for val in value_list:
            result.append((key,val))
    return result

@pytest.mark.parametrize("kind, sub_kind",get_data()) 
def xtest_click_subcategory_for_navigation(use_saved_login,kind,sub_kind):
    page = use_saved_login

    home_p = Home(page)
    logout_button = home_p.get_logout_button
    expect(logout_button).to_be_visible()

    category_p = Category(page)

    category = category_p.get_category(category=kind)
    expect(category).to_be_visible()

    sub_category = category_p.get_subcategory(kind=kind,section=sub_kind)
    expect(sub_category).not_to_be_visible()
    category.click()
    expect(sub_category).to_be_visible()

    sub_category_p = category_p.click_subcategory(sub_category)
    heading = sub_category_p.get_heading
    expect(heading).to_contain_text(f"{kind} - {sub_kind} Products")
    page.wait_for_timeout(1000)
