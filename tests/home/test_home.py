from playwright.sync_api import expect
from src.utils.controlutils.controlUtils import ControlUtils
from src.pages.home.homePage import Home

def test_home_navigation(setup):
    page= setup
    home = Home(page)
    ControlUtils.validate_element_is_visible(home.get_nav_link(""))

