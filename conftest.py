import pytest
from playwright.sync_api import Playwright
from src.pages.login.loginPage import Login
from src.utils.constants.constantsUtils import EMAIL, PASSWORD
from src.pages.cart.cartPage import Cart

@pytest.fixture(scope="function")
def setup(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://automationexercise.com/")
    yield page
    context.close()
    browser.close()



# @pytest.fixture(scope="session")
# def save_login_state(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()

#     page = context.new_page()
#     page.goto("https://automationexercise.com/login")

#     login_p = Login(page)

#     login_p.email_locator("login").fill("dummybaba@gmail.com")
#     login_p.get_input_field("Password").fill("pakistan123")
#     login_p.button_locator("Login").click()

#     context.storage_state(path="auth.json")

#     context.close()
#     browser.close()


# @pytest.fixture(scope="function")
# def use_saved_login(playwright: Playwright, save_login_state):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context(storage_state="auth.json")

#     page = context.new_page()

#     page.goto("https://automationexercise.com/")

#     yield page

#     context.close()
#     browser.close()











AUTH_FILE = "auth.json"
 
 
# ─────────────────────────────────────────────
# 1. Session-scoped: log in ONCE, save state
#    The browser opened here is kept alive so
#    the first test can reuse it directly.
# ─────────────────────────────────────────────
@pytest.fixture(scope="session")
def _login_session(playwright: Playwright):
    """
    Opens a browser, logs in, saves auth.json,
    then yields the (browser, context, page) tuple
    so the FIRST test can reuse this exact browser.
 
    After the whole session finishes, the browser
    is closed here — not in the individual tests.
    """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
 
    page.goto("https://automationexercise.com/login")
 
    login_p = Login(page)
    login_p.email_locator("login").fill(EMAIL)
    login_p.get_input_field("Password").fill(PASSWORD)
    login_p.button_locator("Login").click()
 
    # Persist login cookies/storage to disk
    context.storage_state(path=AUTH_FILE)
 
    yield browser, context, page   # <-- yielding the live session
 
    context.close()
    browser.close()
 
 
# ─────────────────────────────────────────────
# 2. Function-scoped: one browser per test
#
#    HOW IT WORKS:
#    • First call  → reuses the already-open
#      login browser (no extra open/close).
#    • Subsequent  → opens a fresh browser
#      loaded from auth.json.
#
#    This gives you:
#      single test  → 1 browser open total
#      N tests      → login browser + N-1 fresh
# ─────────────────────────────────────────────
_first_call = True   # module-level flag
 
@pytest.fixture(scope="function")
def use_saved_login(playwright: Playwright, _login_session):
    global _first_call
 
    if _first_call:
        # ── Reuse the login browser for the first test ──
        _first_call = False
        browser, context, page = _login_session
        page.goto("https://automationexercise.com/")
 
        yield page
        # Do NOT close — _login_session owns the lifecycle
 
    else:
        # ── Open a fresh isolated browser for every other test ──
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state=AUTH_FILE)
        page = context.new_page()
        page.goto("https://automationexercise.com/")
 
        yield page
 
        context.close()
        browser.close()
 




# @pytest.fixture()
# def clean_cart(use_saved_login):
#     """
#     Ensures the cart is empty before AND after each cart test.
#     Guarantees full test isolation — no leftover items from previous runs.

#     Usage:
#         def test_something(use_saved_login, clean_cart):
#             page = use_saved_login
#             ...
#     """
#     def _empty_cart(page):
#         page.goto("https://automationexercise.com/view_cart")
#         cart = Cart(page)

#         # If cart is already showing the empty message, nothing to do
#         if cart.get_cart_empty.is_visible():
#             return

#         items = cart.get_all_cart_items()
#         count = items.count()

#         for i in range(count):
#             # Always delete the FIRST remaining row — after each deletion
#             # the table re-renders, so nth(0) is always the next live item
#             first_item = cart.get_all_cart_items().nth(0)
#             cart.get_delete_button(first_item).click()
#             page.wait_for_timeout(300)  # let the row animate out

#         # Final guard — confirm the empty state is now visible
#         cart.get_cart_empty.wait_for(state="visible", timeout=5000)

#     page = use_saved_login

#     _empty_cart(page)   # ── setup: clear before test
#     yield
#     _empty_cart(page)   # ── teardown: clear after test