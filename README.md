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

2. **Login Page Navigation** (`test_login.py`)
   - Tests navigation from home to login/signup page
   - Validates the correct URL is reached

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
   - Runs parametrized tests to create multiple user accounts

## 🏗️ Project Structure

```
automationextercise/
├── src/
│   ├── pages/                          # Page Object Models
│   │   ├── home/
│   │   │   └── HomePage.py            # Home page interactions
│   │   ├── login/
│   │   │   └── LoginPage.py           # Login/signup page interactions
│   │   └── signup/
│   │       └── SignupPage.py          # Account info form interactions
│   └── utils/
│       ├── constants/
│       │   └── constantsUtils.py      # Test data constants (countries, months, etc.)
│       └── generatedata/
│           ├── GenerateDataUtils.py   # Test data generation utilities
│           └── dataUtils.py           # Data formatting and factory functions
├── tests/
│   ├── home/
│   │   └── test_home.py               # Home page tests
│   ├── login/
│   │   └── test_login.py              # Login navigation tests
│   └── signup/
│       └── test_signup.py             # Complete signup workflow tests
├── conftest.py                        # pytest fixtures and setup
├── pytest.ini                         # pytest configuration
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
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

## 🔑 Key Classes and Methods

### HomePage
- `click_signup_login()` - Navigate to signup/login page

### LoginPage
- `enterName(name)` - Enter name for signup
- `enterEmail(email)` - Enter email for signup
- `click_signup_button()` - Submit signup form
- `create_new_user()` - Proceed to account details form
- Properties: `signup_header`, `name_input`, `email_input`, `signup_error_message`

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

### Running 2 signup registrations:
```bash
pytest tests/signup/test_signup.py -v
```
This creates 2 different user accounts with randomly generated data and validates the entire signup process.

### Checking test assertions in action:
The signup test validates:
- Form fields have expected values
- Radio buttons toggle correctly
- Dropdowns select proper options
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
