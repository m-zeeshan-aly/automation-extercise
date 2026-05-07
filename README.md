# Automation Exercise - Playwright Test Suite

A comprehensive browser automation test suite built with **Playwright** and **pytest** for testing user registration and login workflows on [automationexercise.com](https://automationexercise.com/).

## 📋 Project Overview

This project demonstrates test automation best practices including:
- **Page Object Model (POM)** - Organized page structure for maintainability
- **Data Generation** - Dynamic test data creation for signup scenarios
- **Fixture-based Setup** - Centralized browser initialization and teardown
- **Parameterized Tests** - Running the same test with multiple data sets
- **Assertions & Validations** - Comprehensive test assertions using Playwright expectations

### What This Code Does

The test suite automates the following workflows on automationexercise.com:

1. **Home Page Navigation** (`test_home.py`)
   - Verifies the home page loads correctly
   - Validates the URL is as expected
   - **Note**: Currently disabled (prefixed with `x`)

2. **Login & Logout** (`test_login.py`)
   - **Login Navigation**: Tests navigation from home to login/signup page
   - **Successful Login**: Authenticates with valid credentials and verifies successful login state
   - **Failed Login**: Tests login attempts with invalid credentials and validates error messages
   - **Login & Logout Workflow**: Tests complete login and logout flow with state validation
   - Validates correct URLs and UI state changes (logout button visibility, etc.)
   - Uses parameterized locators for flexible form field selection

3. **User Registration/Signup** (`test_signup.py`)
   - Creates new user accounts with randomly generated test data
   - Fills out complete signup forms including:
     - Personal information (name, email, password, title)
     - Date of birth (day, month, year)
     - Address information (company, address, city, state, country)
     - Contact details (phone, zip code)
     - Newsletter opt-in preferences
   - Validates form field behavior (editable, read-only, checked states)
   - Handles existing user scenarios
   - Runs parametrized tests to create user accounts (currently set to 1 iteration)

4. **Category Navigation** (`test_category.py`) - NEW
   - **Status**: Disabled (prefixed with `xtest`)
   - Tests category menu expansion and visibility
   - Verifies subcategories are hidden until parent category is clicked
   - Uses parameterized tests to iterate through all categories (Men, Women, Kids)
   - Validates proper UI state transitions

5. **Product Card Interactions** (`test_product_card.py`) - NEW
   - **Status**: Disabled (prefixed with `xtest`)
   - **Test 1: Product Card Hover**: Verifies price and description consistency between card and hover state
   - **Test 2: View Product Navigation**: Tests "View Product" button navigation to product detail page
   - **Test 3: Add to Cart Flow**: Tests adding products to cart and cart popup interactions
   - Uses random product selection for variety
   - Validates hover effects and information consistency
   - Tests cart popup functionality (Added! message, Continue Shopping, View Cart)

6. **Product Detail Page** (`test_product_detail.py`) - NEW
   - **Status**: One active test (`test_verify_selected_product_details`)
   - Verifies product details match between card and detail page
   - Validates price, description, and image consistency
   - Tests product tab highlighting (orange color)
   - Confirms image sources match between card and detail views
   - Tests complete navigation flow from products list to detail page

7. **Subcategory Navigation** (`test_subcategory.py`) - NEW
   - **Status**: Disabled (prefixed with `xtest`)
   - Tests subcategory click navigation from all categories
   - Uses parameterized tests to iterate through all category/subcategory combinations
   - Validates heading text contains correct category and subcategory information
   - Tests complete category → subcategory → products listing flow

8. **Complete Order Workflow** (`test_place_order.py`) - UPDATED
   - **Status**: Disabled (converted to `xtest`)
   - Comprehensive end-to-end test combining all features:
     - Category and subcategory navigation
     - Product card interactions
     - Add to cart functionality
     - Cart popup handling
     - Cart page verification
   - Tests multiple product additions to cart
   - Validates checkout button visibility on cart page

## 🏗️ Project Structure

```
automationextercise/
├── src/
│   ├── pages/                                    # Page Object Models
│   │   ├── account/
│   │   │   └── accountCreatedPage.py           # Account created page interactions
│   │   ├── cart/
│   │   │   ├── cartPage.py                    # Cart page interactions (NEW)
│   │   │   └── cartPopupPage.py               # Add to cart popup interactions (NEW)
│   │   ├── category/
│   │   │   ├── categoryPage.py                # Category navigation interactions
│   │   │   └── subCategoryPage.py             # Subcategory interactions (REFACTORED)
│   │   ├── home/
│   │   │   └── homePage.py                    # Home page interactions
│   │   ├── login/
│   │   │   └── loginPage.py                   # Login/signup page interactions
│   │   ├── products/
│   │   │   ├── productCardPage.py             # Product card interactions (NEW)
│   │   │   └── productDetailPage.py           # Product detail page interactions (NEW)
│   │   └── signup/
│   │       └── SignupPage.py                  # Account info form interactions
│   └── utils/
│       ├── constants/
│       │   └── constantsUtils.py              # Test data constants (countries, months, etc.)
│       └── generatedata/
│           ├── GenerateDataUtils.py           # Test data generation utilities
│           └── dataUtils.py                   # Data formatting and factory functions
├── tests/
│   ├── category/
│   │   └── test_category.py                   # Category navigation tests (NEW - disabled)
│   ├── home/
│   │   └── test_home.py                       # Home page tests
│   ├── login/
│   │   └── test_login.py                      # Login/logout workflow tests
│   ├── placeorder/
│   │   └── test_place_order.py                # Complete order workflow test (UPDATED - disabled)
│   ├── productcard/
│   │   └── test_product_card.py               # Product card interaction tests (NEW - disabled)
│   ├── productdetail/
│   │   └── test_product_detail.py             # Product detail page tests (NEW - one active)
│   ├── signup/
│   │   └── test_signup.py                     # Complete signup workflow tests
│   └── subcategory/
│       └── test_subcategory.py                # Subcategory navigation tests (NEW - disabled)
├── conftest.py                                # pytest fixtures and setup
├── pytest.ini                                 # pytest configuration
├── requirements.txt                           # Python dependencies
├── auth.json                                  # Stored browser session state (UPDATED)
└── README.md                                  # This file
```

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd automationextercise
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**
   ```bash
   playwright install chromium
   ```

## 🚀 Running Tests

### Run All Tests
```bash
pytest
```

### Run Specific Test File
```bash
pytest tests/signup/test_signup.py
```

### Run Specific Test
```bash
pytest tests/home/test_home.py::test_home_navigation
```

### Run with Verbose Output
```bash
pytest -v
```

### Run in Headed Mode (with visible browser)
The default configuration already runs in headed mode with a 500ms slowdown between actions for debugging visibility.

### Run with Markers
```bash
# Run only smoke tests
pytest -m smoke

# Run regression tests
pytest -m regression
```

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `playwright` | Browser automation library |
| `pytest` | Test framework |
| `pytest-playwright` | Playwright pytest plugin |

See [requirements.txt](requirements.txt) for complete dependency list.

## 🔧 Configuration

### pytest.ini Settings
- **Headed Mode**: Tests run with visible browser window
- **Browser**: Chromium (configurable in pytest.ini)
- **Slowmo**: 500ms delay between actions (for debugging)
- **Test Discovery**: Looks for `test_*.py` files with `test_*` functions

### conftest.py Fixture
The `setup` fixture handles:
- Launching Chromium browser in headless=False mode
- Creating a browser context
- Creating a new page and navigating to https://automationexercise.com/
- Cleanup after test completion

## 📋 Recent Changes & Architecture Updates

### New Page Object Models - Product Management System
Four new page object classes have been added to support product and cart interactions:

#### 1. **ProductCard** (`productCardPage.py`) - NEW
   - Handles interactions with product cards in the products listing
   - Methods:
     - `select_product()` - Randomly selects a product from the listing
     - `get_price(product)` - Extracts price from product card
     - `get_description(product)` - Extracts description from product card
     - `get_price_on_hover(product)` - Gets price displayed on hover
     - `get_description_on_hover(product)` - Gets description displayed on hover
     - `get_view_product_button(product)` - Returns view product button
     - `get_add_to_cart_button(product)` - Returns add to cart button
     - `get_image(product)` - Returns product image element
     - `click_view_product(button)` - Clicks view product and returns ProductDetail object
     - `click_add_to_cart(button)` - Clicks add to cart and returns CartPopup object
   - Uses XPath selectors for card, hover state, and button localization
   - Supports dynamic product selection with random index

#### 2. **ProductDetail** (`productDetailPage.py`) - NEW
   - Handles interactions on individual product detail pages
   - Properties:
     - `get_product_tab` - Product navigation tab link
     - `get_description` - Product heading/name
     - `get_product_price` - Product price element
     - `get_product_image` - Product main image
   - Used for validating product information consistency

#### 3. **Cart** (`cartPage.py`) - NEW
   - Manages shopping cart page interactions
   - Properties:
     - `get_checkout_button` - Proceed to checkout button
   - Methods:
     - `get_all_cart_items()` - Returns all items in cart
   - Supports cart review and checkout initiation

#### 4. **CartPopup** (`cartPopupPage.py`) - NEW
   - Manages the "Added!" popup after adding items to cart
   - Properties:
     - `get_heading` - Popup heading element
   - Methods:
     - `click_continue_shoping()` - Continues shopping (closes popup)
     - `click_view_cart_button()` - Opens cart page and returns Cart object
   - Enables multi-product additions and cart management workflows

### SubCategory Page Refactoring
The `SubCategory` class has been refactored for cleaner, more maintainable code:

**Before:**
```python
class SubCategory:
    # CATEGORY = "//div[@id='accordian']//a[...]"
    # SUB_CATEGORY = "//div[@id='{kind}']//a[...]"
    # def get_category(self,category): ...
    # def get_subcategory(self,kind,section): ...
```

**After:**
```python
class SubCategory:
    def __init__(self,page):
        self.page = page
        self._heading = page.locator("//h2[contains(text(),' Products')]")

    @property
    def get_heading(self):
        return self._heading
```

**Benefits:**
- Removed commented-out code
- Added direct heading element access
- Uses property decorator for cleaner API
- Simpler, more focused functionality

### Category Constants Update
Updated `CATEGORIES` dictionary in `constantsUtils.py`:

**Before:**
```python
CATEGORIES = {
    "Men"   :  ["Dress","Tops","Saree"],
    "Women" :  ["Tshirts","Jeans"],
    "Kids"  :  ["Dress","Tops & Shirts"]
}
```

**After:**
```python
CATEGORIES = {
    "Men"   :  ["Tshirts","Jeans"],
    "Women" :  ["Dress","Tops","Saree"],
    "Kids"  :  ["Dress","Tops & Shirts"]
}
```

**Changes:**
- Swapped Men and Women category subcategories
- Reflects current website product structure

### Test Architecture Expansion
Added 4 new test modules with comprehensive product management testing:
- `tests/category/test_category.py` - Category navigation tests (disabled)
- `tests/productcard/test_product_card.py` - Product card interaction tests (disabled)
- `tests/productdetail/test_product_detail.py` - Product detail validation tests (1 active)
- `tests/subcategory/test_subcategory.py` - Subcategory navigation tests (disabled)

### Test Status Summary
- **Enabled Tests**:
  - `test_verify_selected_product_details` in `test_product_detail.py` - Validates product information consistency
- **Disabled Tests** (prefixed with `xtest`):
  - Used for development and future enablement
  - Includes comprehensive test logic for validation purposes

## 📋 Original Architecture Updates

### LoginPage Refactoring
The LoginPage has been refactored from a class with individual methods for each form field to a more flexible, parameterized approach:

**Before:**
```python
login_p.enterName(data.get("full_name"))
login_p.enterEmail(data.get("email"))
login_p.click_signup_button()
```

**After:**
```python
login_p.get_input_field("Name").fill(data.get("full_name"))
login_p.email_locator("signup").fill(data.get("email"))
button = login_p.button_locator("Signup")
login_p.click_button(button)
```

**Benefits:**
- More maintainable: Uses XPath patterns that can be reused
- More flexible: Supports both login and signup flows without duplicating code
- Better separation of concerns: Locators are defined as class constants
- Easier to extend: New input types can be handled without adding new methods

### New Login/Logout Testing
Added comprehensive login testing including:
- Login form validation with both valid and invalid credentials
- Error message validation for failed login attempts
- Complete login and logout workflow testing
- UI state verification (logout button visibility changes)

## 🔑 Key Classes and Methods

### HomePage
- `click_signup_login()` - Navigate to signup/login page
- `user_name` (property) - Get the logged-in username element
- `get_logout_button` (property) - Get the logout button element

### Category Navigation
- **Category** (`categoryPage.py`)
  - `get_category(category)` - Get category element by name
  - `get_subcategory(kind, section)` - Get subcategory element
  - `click_subcategory(sub_category)` - Click subcategory and return SubCategory object
  
- **SubCategory** (`subCategoryPage.py`)
  - `get_heading` (property) - Get the products heading showing category and subcategory

### Product Management
- **ProductCard** (`productCardPage.py`)
  - `select_product()` - Randomly select a product
  - `get_price(product)` - Get product price
  - `get_description(product)` - Get product description
  - `get_price_on_hover(product)` - Get price displayed on hover
  - `get_description_on_hover(product)` - Get description displayed on hover
  - `click_view_product(button)` - Navigate to product detail page
  - `click_add_to_cart(button)` - Add product to cart and show popup

- **ProductDetail** (`productDetailPage.py`)
  - `get_description` (property) - Product name/heading
  - `get_product_price` (property) - Product price element
  - `get_product_image` (property) - Product image element
  - `get_product_tab` (property) - Products navigation tab

- **Cart** (`cartPage.py`)
  - `get_checkout_button` (property) - Proceed to checkout button
  - `get_all_cart_items()` - Get all items in shopping cart

- **CartPopup** (`cartPopupPage.py`)
  - `get_heading` (property) - Popup heading ("Added!")
  - `click_continue_shoping()` - Continue shopping (close popup)
  - `click_view_cart_button()` - View cart page

### Test Fixtures
- **setup** - Basic browser setup fixture
- **save_login_state** - Saves authenticated session to auth.json
- **use_saved_login** - Launches browser with saved authentication

## 📝 Changed Files Summary

| File | Type | Changes |
|------|------|---------|
| `auth.json` | Updated | New session cookies and configuration data |
| `src/pages/category/subCategoryPage.py` | Refactored | Cleaned up code, added heading property |
| `src/utils/constants/constantsUtils.py` | Updated | Swapped Men and Women subcategories |
| `tests/placeorder/test_place_order.py` | Updated | Converted to xtest, expanded test logic significantly |
| `src/pages/cart/cartPage.py` | NEW | Cart page object model |
| `src/pages/cart/cartPopupPage.py` | NEW | Add to cart popup object model |
| `src/pages/products/productCardPage.py` | NEW | Product card interactions object model |
| `src/pages/products/productDetailPage.py` | NEW | Product detail page object model |
| `tests/category/test_category.py` | NEW | Category navigation tests (disabled) |
| `tests/productcard/test_product_card.py` | NEW | Product card interaction tests (disabled) |
| `tests/productdetail/test_product_detail.py` | NEW | Product detail validation tests |
| `tests/subcategory/test_subcategory.py` | NEW | Subcategory navigation tests (disabled) |
| `README.md` | Updated | Comprehensive documentation of all changes |

## ✅ Test Execution Guide

### Run Only Active Tests
```bash
pytest -v
```
This will run only the enabled tests:
- All signup tests
- All login tests
- `test_verify_selected_product_details` from product detail tests

### Run Specific Test Files
```bash
# Product detail tests only
pytest tests/productdetail/test_product_detail.py -v

# Login tests only
pytest tests/login/test_login.py -v

# Signup tests only
pytest tests/signup/test_signup.py -v
```

### Enable Disabled Tests (for debugging/development)
To enable the xtest functions temporarily, edit the test file and change `xtest_` to `test_`:
```python
# Change this:
def xtest_product_card_hover(use_saved_login):

# To this:
def test_product_card_hover(use_saved_login):
```

### Run with Additional Options
```bash
# Verbose with timing
pytest -v --tb=short

# Stop after first failure
pytest -x

# Show print statements
pytest -s

# Run with specific marker
pytest -m smoke -v
```

## 🔍 Testing Workflow

The automated tests follow this typical workflow:

1. **Setup**: Browser launched, logged in via saved session (auth.json)
2. **Navigation**: From home page → category → subcategory
3. **Product Selection**: Random product selection from listing
4. **Validation**: Price, description, image consistency checks
5. **Interaction**: Add to cart, view cart, verify checkout button
6. **Cleanup**: Browser context and session closed

## 🛠️ Fixture Lifecycle

The `conftest.py` manages the following:

1. **save_login_state** (Session scope)
   - Runs once per test session
   - Logs in with credentials: dummybaba@gmail.com / pakistan123
   - Saves browser storage state to auth.json

2. **use_saved_login** (Function scope)
   - Runs before each test function
   - Launches browser with saved authentication from auth.json
   - Navigates to home page
   - Provides authenticated page context to tests

## 🚨 Current Test Status

| Test Module | Status | Count | Notes |
|-------------|--------|-------|-------|
| test_home.py | Disabled | 1 | Prefixed with xtest |
| test_login.py | Enabled | 4 | All active |
| test_signup.py | Enabled | 1 | Parameterized signup |
| test_category.py | Disabled | 1 | Prefixed with xtest |
| test_product_card.py | Disabled | 3 | All prefixed with xtest |
| test_product_detail.py | Enabled | 1 | Active test (1 disabled) |
| test_subcategory.py | Disabled | 1 | Prefixed with xtest |
| test_place_order.py | Disabled | 1 | Converted to xtest |
| **TOTAL** | | **13** | **6 Active, 7 Disabled** |

### LoginPage (Refactored)
**Class Constants:**
- `EMAIL` - XPath pattern for email inputs: `"//input[@data-qa='{method}-email']"`
- `BUTTON` - XPath pattern for buttons: `"//button[normalize-space()='{title}']"`
- `INPUT` - XPath pattern for input fields: `"//input[@placeholder='{placeholder}']"`
- `ERROR` - XPath pattern for error messages

**Properties:**
- `signup_header` - Get signup form header

**Methods:**
- `email_locator(method)` - Get email input locator by method (e.g., "login", "signup")
- `button_locator(title)` - Get button locator by title (e.g., "Login", "Signup")
- `get_input_field(placeholder)` - Get input field by placeholder text (e.g., "Password", "Name")
- `error_message()` - Get error message locator
- `click_button(button)` - Click button and return Signup page
- `login(button)` - Click login button and return Home page
- `logout(button)` - Click logout button and return Home page

### AccountCreatedPage
- `account_header` (property) - Get the "Account Created!" header element
- `account_continue_button` (property) - Get the Continue button element

### SignupPage
- `get_title_radio_locator(title)` - Get title radio button (Mr/Mrs)
- `get_input_field(name)` - Get form input field by ID
- `get_dropdown(title)` - Get dropdown by ID
- `get_checkbox_locator(text)` - Get checkbox by label text
- `signup()` - Submit account creation form
- Property: `signup_header`

### GenerateData
Utility class for creating random test data:
- `fullName()`, `firstName()`, `lastName()`
- `email()` - Unique test email
- `phone()` - Random phone number
- `day()`, `month()`, `year()` - Random date components
- `country()`, `city()`, `state()`, `address()`
- `company()`, `zip_code()`
- `title()` - Random title (Mr/Mrs)
- `checkboxes()` - Random checkbox selections

## 📝 Test Examples

### Running Signup Tests
```bash
pytest tests/signup/test_signup.py -v
```
This creates 1 user account with randomly generated data and validates the entire signup process.

### Running Login Tests
```bash
pytest tests/login/test_login.py -v
```
This runs the following test scenarios:
- **test_login_url**: Validates navigation to login page
- **test_login_and_logout**: Tests complete login and logout workflow with error checking
- **test_login_suceess**: Tests successful login scenario and logout button visibility
- **test_login_with_wrong_email_pass**: Tests failed login with invalid credentials and error message validation

### Running All Tests
```bash
pytest -v
```

### Checking Test Assertions in Action
The test suite validates:
- Form fields have expected values
- Radio buttons toggle correctly
- Dropdowns select proper options
- Error messages display for invalid credentials
- UI state changes correctly after login/logout
- Checkboxes check/uncheck appropriately
- Address fields populate correctly
- Existing user email error handling

## 🐛 Debugging

- Tests run with **500ms slowdown** between actions for visual debugging
- Browser runs **headless=False** so you can see interactions
- Use `-v` flag for verbose output
- Check terminal output with `-s` flag (enabled in pytest.ini)

## 📊 Test Coverage

Current test coverage includes:
- ✅ Home page load validation
- ✅ Navigation to login/signup
- ✅ New user signup form filling
- ✅ Form field validation
- ✅ Date picker selection
- ✅ Dropdown selection
- ✅ Checkbox selection
- ✅ Duplicate email handling
- ✅ Multi-run parametrized testing

## 🔄 Continuous Integration Ready

The pytest.ini includes configurations suitable for CI/CD pipelines with markers for:
- `@pytest.mark.smoke` - Quick sanity checks
- `@pytest.mark.regression` - Full test suite
- `@pytest.mark.sanity` - Basic health checks

## 📄 License

This is a learning/training automation project for testing purposes.
