from src.pages.home.homePage import Home
from src.pages.category.categoryPage import Category
from src.utils.constants.constantsUtils import CATEGORIES, BRANDS
from src.utils.controlutils.controlUtils import ControlUtils
from src.pages.category.subCategoryPage import SubCategory
import pytest

@pytest.mark.parametrize("kind", CATEGORIES.keys()) 
def test_click_category(use_saved_login,kind):
    page = use_saved_login
    home = Home(page)
    ControlUtils.validate_element_is_visible(home.get_button("Logout"))
    category_p = Category(page)
    ControlUtils.validate_element_is_visible(category_p.get_category(category=kind))
    page = ControlUtils.click_on_element(category_p.get_category(category=kind))

    ControlUtils.validate_element_is_visible(category_p.get_subcategory(kind=kind,section=CATEGORIES[kind][0]))
    page.wait_for_timeout(1000)


@pytest.mark.parametrize("brand", BRANDS) 
def test_click_brand(use_saved_login,brand):
    page = use_saved_login
    home = Home(page)
    ControlUtils.validate_element_is_visible(home.get_button("Logout"))
    category_p = Category(page)

    ControlUtils.validate_element_is_visible(category_p.get_brand(brand))
    page = ControlUtils.click_on_element(category_p.get_brand(brand))
    sub_category = SubCategory(page)
    ControlUtils.validate_element_contain_text(sub_category.get_heading,brand)
    page.wait_for_timeout(1000)
