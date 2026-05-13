from src.pages.home.homePage import Home
from src.pages.category.categoryPage import Category
from src.utils.constants.constantsUtils import CATEGORIES
from src.pages.category.subCategoryPage import SubCategory
from src.utils.controlutils.controlUtils import ControlUtils
import pytest

def get_data():
    result =[]
    list_of_tuples=CATEGORIES.items()
    for key, value_list in list_of_tuples:
        for val in value_list:
            result.append((key,val))
    return result

@pytest.mark.parametrize("kind, sub_kind",get_data()) 
def xtest_click_subcategory_for_navigation(use_saved_login, kind, sub_kind):
    page = use_saved_login
    home = Home(page)
    ControlUtils.validate_element_is_visible(home.get_button("Logout"))

    category_p = Category(page)

    ControlUtils.validate_element_is_visible(category_p.get_category(category=kind))
    page = ControlUtils.click_on_element(category_p.get_category(category=kind))

    ControlUtils.validate_element_is_visible(category_p.get_subcategory(kind=kind,section=sub_kind))
    page = ControlUtils.click_on_element(category_p.get_subcategory(kind=kind,section=sub_kind))
    sub_category_p = SubCategory(page)
    # We expect the heading to match the selected hierarchy
    expected_heading = f"{kind} - {sub_kind} Products"
    ControlUtils.validate_element_have_text(sub_category_p.get_heading,expected_heading)
    # page.wait_for_timeout(2000)

