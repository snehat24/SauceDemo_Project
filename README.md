# SauceDemo Playwright Automation Framework

## Overview

This project was built to practice automation testing using Python, Playwright, and Pytest.
It automates key SauceDemo user flows including login, product sorting, add-to-cart, checkout, and logout.
The framework follows the Page Object Model (POM) design pattern and uses Pytest fixtures for better code reusability and maintainability.

## Tech Stack

* Python
* Playwright (Sync API)
* Pytest
* Page Object Model (POM)
* Pytest Fixtures
* HTML Reports
* Logging

## Project Structure

* `pages/` → Page Object classes
* `tests/` → Test cases
* `utils/` → Logger and helper files
* `config.py` → Environment and test configuration
* `conftest.py` → Fixtures and Pytest hooks
* `state.json` → Session storage for login reuse
* `requirements.txt` → Required dependencies

## Features Covered

### Positive Scenarios

* Login with valid credentials
* Add product to cart
* Remove product from cart
* Product sorting
* Checkout flow
* Logout functionality

### Negative Scenarios

* Login with invalid credentials
* Checkout without filling mandatory fields

## Execution

### Run all tests

```bash
pytest -v
```

### Run with browser

```bash
pytest --browser chromium
```

### Run specific test

```bash
pytest tests/test_TC01_login.py
```

## Author

Sneha
