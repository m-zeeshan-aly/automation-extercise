# Automation Exercise - Playwright Test Suite

A comprehensive browser automation test suite built with **Playwright** and **pytest** for testing end-to-end ecommerce workflows on [automationexercise.com](https://automationexercise.com/). The project follows the **Page Object Model (POM)** design pattern with clean separation of concerns, reusable utilities, and dynamic test data generation.

## 📋 Project Overview

This suite provides comprehensive test coverage for:

- **Authentication**: User login, signup, account creation, and logout flows
- **Navigation**: Category, subcategory, and brand navigation with dynamic content
- **Product Browsing**: Product cards with hover states, pricing, descriptions, and image validation
- **Shopping Cart**: Add/remove items, quantity management, bill calculation, and empty cart states
- **Checkout**: Address validation, checkout process, and order summary verification
- **Payment Processing**: Payment form submission and order success confirmation
- **Forms**: Contact-us form submission with dynamic data generation and file uploads
- **Data Generation**: Random user data, product data, and test fixtures for realistic test scenarios

## 🏗️ Architecture & Design Patterns

### Page Object Model (POM)

Each page in the application has a corresponding page object class that:
- **Encapsulates all element locators**: XPath, CSS selectors stored as class-level strings
- **Provides methods to interact with page elements**: Methods return locators for both actions and assertions
- **Returns clean locators for test assertions**: Enables tests to call methods without knowing implementation details
- **Maintains loose coupling between tests and UI**: UI changes only require updating page object classes, not tests

**Example**: The `CartPage` class provides methods like `get_product_name()`, `get_product_price()`, `get_product_total()` that return clean locators for assertions, and `get_delete_button()` for actions.

### Control Utilities

Centralized static utility methods in `ControlUtils` for:
- **Element interaction**: `click_on_element()`, `fill_input_field()`, `check_radio_and_checkbox_button()`, `select_dropdown_value()`
- **Assertions and validations**: `validate_element_is_visible()`, `validate_element_is_checked()`, `validate_input()`, `validate_dropdown_value()`
- **Text extraction and cleanup**: `get_clean_text()`, `get_clean_attribute()` for removing whitespace and handling edge cases
- **Preventing null pointer and assertion failures**: All assertions use Playwright's `expect()` for reliable test stability

### Data Generation

Dynamic test data generator in `GenerateData` that creates:
- **Random names**: First name, last name, full name (6-character random strings, capitalized)
- **Email addresses**: Unique emails using UUID with `@test.com` domain
- **Phone numbers**: Pakistan format (03 + 9 digits)
- **Payment info**: 13-digit card numbers, 3-digit CVC codes
- **Date fields**: Random day (1-31), random month from predefined list, random year (past 100 years)
- **Address data**: Random street addresses with landmarks
- **City names**: 1-3 word city names with proper capitalization
- **Postal codes**: 5-8 digit random zip codes
- **Country selection**: Random selection from list of 7 countries (India, US, Canada, Australia, Israel, New Zealand, Singapore)
- **Title selection**: Mr or Mrs with even distribution
- **Checkbox selections**: Random subset of newsletter and offers checkboxes

## 📁 Project Structure

```text
automationextercise/
├── src/
│   ├── pages/                          # Page Object Model classes
│   │   ├── account/
│   │   │   └── accountCreatedPage.py   # Account creation confirmation
│   │   ├── cart/
│   │   │   ├── cartPage.py             # Shopping cart page - item verification, deletion, bill calculation
│   │   │   └── cartPopupPage.py        # Add to cart popup modal - "Added!" confirmation
│   │   ├── category/
│   │   │   ├── categoryPage.py         # Category and brand listing - navigation elements
│   │   │   └── subCategoryPage.py      # Subcategory products - product display after category click
│   │   ├── checkout/
│   │   │   └── checkoutPage.py         # Checkout address & order summary - billing/delivery addresses, bill
│   │   ├── contactus/
│   │   │   └── contactUsPage.py        # Contact form page - subject, message, file upload
│   │   ├── home/
│   │   │   └── homePage.py             # Home page navigation - navigation links, buttons
│   │   ├── login/
│   │   │   └── loginPage.py            # Login/signup entry point - login form, signup form
│   │   ├── ordersuccess/
│   │   │   └── orderSuccessPage.py     # Order confirmation page - order success message, download invoice
│   │   ├── payment/
│   │   │   └── paymentPage.py          # Payment form fields - card number, CVC, month, year
│   │   └── products/
│   │       ├── productCardPage.py      # Product grid & cards - product list, hover states, add to cart
│   │       └── productDetailPage.py    # Individual product details - full product info page
│   ├── utils/
│   │   ├── constants/
│   │   │   └── constantsUtils.py       # Test data & constants - hardcoded credentials, categories, countries, etc.
│   │   ├── controlutils/
│   │   │   └── controlUtils.py         # Reusable action & assertion methods - static utility methods
│   │   └── generatedata/
│   │       ├── dataUtils.py            # Test data generation functions - signup_data(), contact data generators
│   │       └── generateDataUtils.py    # GenerateData class - random data creation for tests
├── tests/                              # Test cases organized by feature
│   ├── cart/
│   │   └── test_cart.py                # Cart functionality tests - add, remove, verify items
│   ├── category/
│   │   └── test_category.py            # Category & brand navigation tests - click categories, view products
│   ├── contactus/
│   │   └── test_contactus.py           # Contact form tests - submit form, verify submission
│   ├── home/
│   │   └── test_home.py                # Home page tests - navigation, button visibility
│   ├── login/
│   │   └── test_login.py               # Login/logout tests - valid/invalid credentials, logout
│   ├── placeorder/
│   │   └── test_place_order.py         # End-to-end order placement - full user journey from product to payment
│   ├── productcard/
│   │   └── test_product_card.py        # Product card display tests - verify card data, hover validation
│   ├── productdetail/
│   │   └── test_product_detail.py      # Product detail page tests - individual product information
│   ├── signup/
│   │   └── test_signup.py              # User signup tests - account creation, form validation
│   └── subcategory/
│       └── test_subcategory.py         # Subcategory navigation tests - navigate and view products
├── testdata/                           # Test data files
│   └── (files uploaded during testing)
├── downloads/                          # Downloaded files from tests
│   └── (invoices, receipts, etc.)
├── conftest.py                         # pytest fixtures & session setup
├── pytest.ini                          # pytest configuration
├── requirements.txt                    # Python dependencies
├── auth.json                           # Saved login session state (auto-generated)
└── README.md                           # This file
```

## 🚀 Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for version control)

### Installation Steps

1. **Clone or navigate to the project directory**:
   ```bash
   cd automationextercise
   ```

2. **Create a Python virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   
   **On Linux/macOS**:
   ```bash
   source venv/bin/activate
   ```
   
   **On Windows**:
   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Install Playwright browsers**:
   ```bash
   playwright install chromium
   ```

   > Note: You only need to run this once after installing the package. It downloads the Chromium browser binaries required for testing.

## 📦 Dependencies

Key packages included in `requirements.txt`:
- **pytest** (9.0.3): Test framework for running test cases
- **playwright** (1.59.0): Browser automation library supporting Chromium, Firefox, WebKit
- **pytest-playwright** (0.7.2): Integration plugin between pytest and Playwright
- **pytest-base-url** (2.1.0): Base URL fixture support for tests
- **requests** (2.33.1): HTTP library for API requests
- Other supporting libraries: python-slugify, Pygments, typing_extensions, etc.

## 🧪 Running Tests

### Default Configuration

The `pytest.ini` file configures:
- **Headed mode**: Tests run with browser UI visible (not headless)
- **Slow motion**: 500ms delay between actions for visual debugging
- **Standard output**: `-s` flag prints test output to console
- **Browser**: Chromium

### Basic Commands

**Run all tests**:
```bash
pytest
```

**Run with verbose output**:
```bash
pytest -v
```

**Run a specific test file**:
```bash
pytest tests/login/test_login.py
```

**Run a specific test**:
```bash
pytest tests/login/test_login.py::test_login_with_valid_credentials -v
```

**Run tests matching a pattern**:
```bash
pytest -k "login" -v
```

**Run tests by marker**:
```bash
pytest -m smoke       # Quick sanity checks
pytest -m regression  # Full suite testing
pytest -m sanity      # Basic health checks
```

**Run tests and stop on first failure**:
```bash
pytest -x
```

**Run tests with specific number of workers (parallel execution)**:
```bash
pytest -n 4  # Requires pytest-xdist package
```

## 🔧 Configuration Files

### pytest.ini

```ini
[pytest]
addopts = --headed --browser chromium --slowmo 500 -s
testpaths = tests
python_files = test_*.py
python_functions = test_*
markers =
    smoke: Quick check of critical functionality
    regression: Full suite testing
    sanity: Basic health check of the build
```

**Key options**:
- `--headed`: Show browser window during test execution
- `--browser chromium`: Use Chromium browser (required by pytest-playwright)
- `--slowmo 500`: Add 500ms delay between Playwright actions
- `-s`: Show stdout/print statements from tests
- `testpaths = tests`: Only look for tests in the `tests` directory

### conftest.py

Defines global pytest fixtures:

**`setup` fixture** (function scope):
- Launches a new Chromium browser instance for each test
- Navigates to `https://automationexercise.com/`
- Returns the page object for use in tests
- Closes the browser after test completes

**`_login_session` fixture** (session scope):
- Runs once at the start of the entire test session
- Logs in using credentials from `constantsUtils.py` (EMAIL, PASSWORD)
- Saves authentication state to `auth.json` for reuse
- Keeps the session alive during the session, allowing subsequent tests to reuse it
- Closes the browser after all tests complete

This enables efficient session-based login reuse for tests that require authenticated access.

## 💡 Important Notes

### Test Naming Convention

**Disabled tests**: Tests prefixed with `x` are intentionally disabled:
```python
def test_login_navigation(setup):  # This test is disabled
    ...

def test_login_valid_credentials(setup):  # This test runs
    ...
```

To enable a disabled test, simply remove the leading `x`:
```bash
# Change xtest_login_navigation → test_login_navigation
# Then run: pytest tests/login/test_login.py::test_login_navigation
```

### Authentication State (`auth.json`)

The `conftest.py` session fixture automatically:
1. Logs in once using credentials from `constantsUtils.py`
2. Saves browser cookies and storage to `auth.json`
3. Enables subsequent tests to reuse this authenticated state

The `auth.json` file is auto-generated and should not be manually edited.

### Page Object Best Practices

1. **Locators**: Store as class-level strings using XPath or CSS selectors
2. **Methods**: Return page object instances to enable method chaining
3. **Properties**: Use `@property` decorator for frequently accessed elements
4. **Naming**: Use descriptive names like `get_delete_button()` instead of `delete_btn()`
5. **Assertions**: Let tests use `ControlUtils` methods to validate state

### Test Data Management

The `GenerateData` class creates unique test data for each test run:
```python
from src.utils.generatedata.dataUtils import signup_data

data = signup_data()  # Returns dict with generated user info
print(data["email"])  # user_a1b2c3d4@test.com (unique each time)
print(data["phone"])  # 03123456789 (Pakistan format)
```

## 🔑 Key Utilities & Helpers

### ControlUtils Class

Common assertion and action methods:

| Method | Purpose |
|--------|---------|
| `click_on_element(locator)` | Click element and return page object |
| `fill_input_field(locator, input)` | Fill text input field |
| `validate_input(locator, input)` | Assert field has expected value |
| `validate_element_is_visible(locator)` | Assert element is visible |
| `check_radio_and_checkbox_button(locator)` | Check radio or checkbox |
| `validate_element_is_checked(locator)` | Assert element is checked |
| `select_dropdown_value(locator, value)` | Select dropdown option |
| `validate_dropdown_value(locator, value)` | Assert dropdown has value |
| `validate_element_have_text(locator, text)` | Assert element has exact text |
| `validate_element_contain_text(locator, text)` | Assert element contains text |
| `get_clean_text(locator)` | Extract text and strip whitespace |
| `get_clean_attribute(locator, attr)` | Extract attribute and strip whitespace |

### GenerateData Class

Methods for random test data:

| Method | Returns | Example |
|--------|---------|---------|
| `firstName()` | Capitalized 6-letter string | "Rashid" |
| `lastName()` | Capitalized 6-letter string | "Saleem" |
| `fullName()` | First + Last name | "Rashid Saleem" |
| `email()` | Unique UUID-based email | "user_a1b2c3d4@test.com" |
| `phone()` | Pakistan format | "03123456789" |
| `day()` | 1-31 | "15" |
| `month()` | Month name | "January" |
| `year()` | Past 100 years | "1975" |
| `country()` | From predefined list | "India" |
| `title()` | Mr or Mrs | "Mr" |
| `zip_code()` | 5-8 digits | "50300" |
| `cvc_expiry()` | 3 digits | "123" |
| `address()` | Street address | "Main, Downtown, Street" |
| `city()` | 1-3 word city name | "Los Angeles" |
| `checkboxes()` | List of checkboxes | ["Sign up for our newsletter!"] |
| `card_number()` | 13 digits | "1234567890123" |

## 📝 Test Coverage Summary

### Authentication Tests
- Login with valid credentials
- Login with invalid credentials
- User signup and account creation
- Logout functionality

### Navigation Tests
- Category browsing
- Subcategory filtering
- Brand navigation
- Home page elements

### Product Tests
- Product card display validation
- Hover state verification
- Price and description accuracy
- Product images loading
- Product detail pages

### Cart Tests
- Add items to cart
- Remove items from cart
- Cart bill calculation
- Empty cart state
- Quantity management

### Checkout Tests
- Address entry and validation
- Billing address verification
- Delivery address verification
- Order summary display

### Payment Tests
- Payment form submission
- Order success confirmation
- Invoice download (if applicable)

### Contact Form Tests
- Form submission with valid data
- File upload functionality
- Subject and message validation
- Dynamic form data generation

## 🐛 Debugging Tips

1. **Increase logging**: Run tests with `-vv` flag for more output
   ```bash
   pytest tests/login/test_login.py -vv
   ```

2. **Slow down execution**: Increase slowmo in pytest.ini for visual inspection
   ```ini
   addopts = --headed --browser chromium --slowmo 2000 -s
   ```

3. **Run single test**: Isolate failures by running one test at a time
   ```bash
   pytest tests/login/test_login.py::test_login_with_valid_credentials -v
   ```

4. **Keep browser open**: Add `page.pause()` in test code to stop execution for inspection
   ```python
   page.pause()  # Browser stays open for manual inspection
   ```

5. **Check test output**: Review console output and captured logs for error messages

## 📚 Additional Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Best Practices](https://selenium.dev/documentation/en/guidelines_and_recommendations/page_object_models/)
- [Test Automation Framework Patterns](https://www.lambdatest.com/blog/test-automation-frameworks/)

## ✅ Best Practices in This Project

1. **Separation of Concerns**: Page objects handle UI locators, tests handle test logic
2. **Reusable Utilities**: ControlUtils provides common operations used across all tests
3. **Dynamic Data Generation**: Tests use realistic, randomized data instead of hardcoded values
4. **Clear Naming**: Test names describe what they test (e.g., `test_add_product_to_cart`)
5. **Fixture Usage**: Shared setup via pytest fixtures reduces code duplication
6. **Assertion Clarity**: Each test has clear assertions about expected behavior
7. **Comments**: Complex logic includes docstrings explaining purpose and parameters
8. **Marker Organization**: Tests use pytest markers for categorization (smoke, regression, sanity)

---

**Last Updated**: May 2026  
**Test Framework**: Playwright + pytest  
**Target Application**: automationexercise.com  
**Maintained By**: QA Automation Team
