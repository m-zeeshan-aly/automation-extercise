# Automation Exercise - Playwright Test Suite

A browser automation test suite built with **Playwright** and **pytest** for testing ecommerce workflows on [automationexercise.com](https://automationexercise.com/). The project follows the Page Object Model pattern and covers navigation, login, signup, categories, product cards, cart behavior, checkout, payment, invoice download, and the contact-us form.

> Important test naming note: pytest only discovers functions that start with `test_`. If you see a function in the code that starts with `xtest_`, that test is intentionally disabled. Remove the leading `x` so it becomes `test_...`, then run the normal pytest command and the test will be executed.

## Project Overview

This suite demonstrates:

- Page Object Model structure across page classes in `src/pages/`
- Dynamic signup, contact-us, and payment data generation
- Session-based login state saved to `auth.json`
- Category and subcategory navigation coverage
- Product card, hover, product-detail, image, price, and description validation
- Cart item verification, deletion, checkout prompts, and bill calculation
- End-to-end order placement with payment and invoice download
- Contact-us form submission with file upload and dialog handling

## Project Structure

```text
automationextercise/
├── src/
│   ├── pages/
│   │   ├── account/
│   │   │   └── accountCreatedPage.py
│   │   ├── cart/
│   │   │   ├── cartPage.py
│   │   │   └── cartPopupPage.py
│   │   ├── category/
│   │   │   ├── categoryPage.py
│   │   │   └── subCategoryPage.py
│   │   ├── checkout/
│   │   │   └── checkoutPage.py
│   │   ├── contactus/
│   │   │   └── contactUsPage.py
│   │   ├── home/
│   │   │   └── homePage.py
│   │   ├── login/
│   │   │   └── loginPage.py
│   │   ├── ordersuccess/
│   │   │   └── orderSuccessPage.py
│   │   ├── payment/
│   │   │   └── paymentPage.py
│   │   ├── products/
│   │   │   ├── productCardPage.py
│   │   │   └── productDetailPage.py
│   │   └── signup/
│   │       └── SignupPage.py
│   └── utils/
│       ├── constants/
│       │   └── constantsUtils.py
│       └── generatedata/
│           ├── dataUtils.py
│           └── generateDataUtils.py
├── tests/
│   ├── cart/
│   │   └── test_cart.py
│   ├── category/
│   │   └── test_category.py
│   ├── contactus/
│   │   └── test_contactus.py
│   ├── home/
│   │   └── test_home.py
│   ├── login/
│   │   └── test_login.py
│   ├── placeorder/
│   │   └── test_place_order.py
│   ├── productcard/
│   │   └── test_product_card.py
│   ├── productdetail/
│   │   └── test_product_detail.py
│   ├── signup/
│   │   └── test_signup.py
│   └── subcategory/
│       └── test_subcategory.py
├── testdata/
│   └── upload_file.jpg
├── downloads/
│   └── invoice.pdf
├── auth.json
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites

- Python 3.8 or higher
- pip
- Chromium browser installed through Playwright

### Installation

```bash
cd automationextercise
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

On Windows, activate the virtual environment with:

```bash
.venv\Scripts\activate
```

## Running Tests

The default pytest configuration runs Chromium in headed mode with a 500ms slow motion delay and prints output with `-s`.

Run all discovered tests:

```bash
pytest
```

Run one test file:

```bash
pytest tests/cart/test_cart.py -v
```

Run one test:

```bash
pytest tests/cart/test_cart.py::test_verify_product_added_to_cart -v
```

Run by marker:

```bash
pytest -m smoke
pytest -m regression
pytest -m sanity
```

## Configuration

`pytest.ini` configures:

- `addopts = --headed --browser chromium --slowmo 500 -s`
- test discovery under the `tests/` directory
- test files matching `test_*.py`
- test functions matching `test_*`
- markers: `smoke`, `regression`, and `sanity`

## Fixtures

`conftest.py` provides three fixtures:

- `setup`: launches Chromium, creates a new context/page, opens `https://automationexercise.com/`, and closes the browser after the test.
- `save_login_state`: logs in with the configured test account and saves browser storage state to `auth.json`.
- `use_saved_login`: creates a browser context from `auth.json`, opens the home page, and gives tests an already-authenticated page.

Tests that require a logged-in user use `use_saved_login`. Public flows such as signup, login failure, contact-us, and checkout login prompts can use `setup`.

## Test Coverage

### Home

File: `tests/home/test_home.py`

- `test_home_navigation`: verifies the home page URL.

### Login

File: `tests/login/test_login.py`

- `test_login_url`: navigates from home to the login/signup page.
- `test_login_and_logout`: logs in with valid credentials, verifies logout visibility, then logs out.
- `test_login_suceess`: verifies successful login state.
- `test_login_with_wrong_email_pass`: verifies the invalid-login error message.

### Signup

File: `tests/signup/test_signup.py`

- `test_signup_form`: creates a new user with generated data, fills account details, validates fields/dropdowns/checkboxes, and verifies the account-created page.

Signup data comes from `signup_data()` in `src/utils/generatedata/dataUtils.py`.

### Category

File: `tests/category/test_category.py`

- `test_click_category`: parameterized over all configured categories and verifies that subcategories become visible after clicking the parent category.

Category data comes from `CATEGORIES` in `src/utils/constants/constantsUtils.py`:

```python
CATEGORIES = {
    "Men": ["Tshirts", "Jeans"],
    "Women": ["Dress", "Tops", "Saree"],
    "Kids": ["Dress", "Tops & Shirts"],
}
```

### Subcategory

File: `tests/subcategory/test_subcategory.py`

- `test_click_subcategory_for_navigation`: parameterized over every category/subcategory pair and validates the target product-listing heading.

### Product Cards

File: `tests/productcard/test_product_card.py`

- `test_product_card_hover`: checks that product price and description match between the card and hover overlay.
- `test_product_card_view_product_button_navigation`: clicks "View Product" and verifies product-page navigation styling.
- `test_product_card_add_to_cart_button`: adds a product to cart, uses the add-to-cart popup, and verifies cart navigation.

Product selection is random through `ProductCard.select_product()`.

### Product Detail

File: `tests/productdetail/test_product_detail.py`

- `test_verify_selected_product_details`: validates that product description, price, and image source match between the product card and product detail page.

### Cart

File: `tests/cart/test_cart.py`

- `test_verify_product_added_to_cart`: adds a product twice, verifies cart item name, price, total, image, bill calculation, and checkout visibility.
- `test_verify_product_deleted_from_cart`: adds a product, deletes it from cart, reloads, and verifies the item count decreases.
- `test_ask_for_login`: adds a product without being logged in, attempts checkout, verifies the checkout popup, continues on cart, then follows the register/login link.

### Contact Us

File: `tests/contactus/test_contactus.py`

- `test_contactus_form`: parameterized for two submissions, opens Contact Us, fills generated name/email/subject/message data, uploads `testdata/upload_file.jpg`, accepts the confirmation dialog, verifies the success message, and returns home.

Contact-us subjects and messages are stored in `CONTACT_SUBJECTS` and `CONTACT_MESSAGES`. Runtime form data is produced by `get_contact_us_data()`.

### Place Order

File: `tests/placeorder/test_place_order.py`

- `test_place_order_and_clicks_continue_button`: completes category navigation, product selection, cart validation, checkout, generated payment data entry, order success validation, continue button navigation, and empty-cart validation.
- `test_place_order_and_clicks_download_invoice_button`: completes the order flow, clicks "Download Invoice", saves the file to `downloads/invoice.pdf`, and verifies that the downloaded PDF exists and is not empty.

Payment data is generated by `GenerateData.get_payment_data()`.

## Page Objects

### Home

`src/pages/home/homePage.py`

- Opens signup/login through `click_signup_login()`
- Exposes logged-in user and logout button locators
- Exposes cart, products, and contact-us buttons
- Navigates to cart with `click_cart_button()`
- Navigates to Contact Us with `click_contact_us_button()`

### Login and Signup

`src/pages/login/loginPage.py`

- Provides reusable locators for login/signup email fields, buttons, inputs, and error messages
- Navigates into signup with `click_button()`
- Logs in and logs out through page-object methods

`src/pages/signup/SignupPage.py`

- Handles title radio buttons, account/address inputs, dropdowns, checkboxes, and Create Account submission

`src/pages/account/accountCreatedPage.py`

- Verifies the account-created header and exposes the Continue button

### Category and Products

`src/pages/category/categoryPage.py`

- Locates categories and subcategories by visible text
- Clicks a subcategory and returns `SubCategory`

`src/pages/category/subCategoryPage.py`

- Exposes the product-listing heading for category/subcategory assertions

`src/pages/products/productCardPage.py`

- Selects random products
- Reads card price, description, image, hover price, and hover description
- Opens product detail pages
- Adds products to cart and returns `CartPopup`

`src/pages/products/productDetailPage.py`

- Exposes product tab, product heading, price, add-to-cart button, and product image

### Cart, Checkout, Payment, and Success

`src/pages/cart/cartPopupPage.py`

- Verifies the "Added!" popup
- Continues shopping
- Opens cart
- Handles unauthenticated checkout popup actions: "Continue On Cart" and "Register / Login"

`src/pages/cart/cartPage.py`

- Reads cart items, names, categories, prices, quantities, totals, images, and delete buttons
- Calculates the cart bill
- Opens checkout
- Exposes empty-cart and checkout-button locators

`src/pages/checkout/checkoutPage.py`

- Reads checkout items, totals, image sources, displayed bill, and calculated bill
- Handles order message text area
- Extracts billing and delivery address lines
- Clicks Place Order and returns `Payment`

`src/pages/payment/paymentPage.py`

- Exposes payment heading and submit button
- Locates payment inputs by field name: `name_on_card`, `card_number`, `cvc`, `expiry_month`, and `expiry_year`
- Submits payment and returns `OrderSuccess`

`src/pages/ordersuccess/orderSuccessPage.py`

- Verifies the order confirmation message
- Locates buttons by label, including "Continue" and "Download Invoice"
- Returns home after clicking Continue

### Contact Us

`src/pages/contactus/contactUsPage.py`

- Exposes the Contact Us heading and success message
- Locates inputs by name: `name`, `email`, `subject`, `upload_file`, and `submit`
- Exposes the message textarea
- Returns home after successful submission

## Data Utilities

`src/utils/generatedata/generateDataUtils.py` contains the `GenerateData` class for:

- first name, last name, and full name
- unique email
- phone number
- title
- date of birth values
- country
- company, address, city, state, and zip code
- checkbox selection
- card number, CVC, expiry month/year, and name on card

`src/utils/generatedata/dataUtils.py` provides:

- `signup_data()`: full signup data dictionary
- `get_contact_us_data()`: contact-us name, email, subject, and message dictionary
- `print_formatted_data()`: helper for readable generated-data output

`src/utils/constants/constantsUtils.py` stores:

- countries
- months
- titles
- checkbox labels
- categories/subcategories
- contact-us subject pool
- contact-us message pool

## Recent Code Updates Reflected Here

- Added Contact Us page object and tests with generated contact data, file upload, dialog handling, and success validation.
- Added product and contact-us navigation helpers to the Home page object.
- Added unauthenticated checkout popup handling in the CartPopup page object.
- Added cart delete-button support and cart deletion verification.
- Added generated payment data for order placement flows.
- Updated generated-data imports to use `generateDataUtils.py`.
- Updated the order invoice flow so `downloads/invoice.pdf` is saved and verified.

## Notes

- Tests hit the live `automationexercise.com` website, so failures can happen if the site changes, responds slowly, or test account/cart state changes.
- Some tests use random product or data selection. Re-run a failed test before assuming the application behavior changed.
- The order and cart tests use an authenticated session through `auth.json`; refresh that file by allowing `save_login_state` to run if the stored session expires.
