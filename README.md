# User Registration Test (Python + Selenium)

This project contains both manual and automated test cases for the **user registration feature** of the [automationexercise.com](https://automationexercise.com) web application.  
It simulates a real-world testing scenario suitable for a **Middle QA Engineer** portfolio.

---

## Features

- 5 clearly written manual test cases covering:
  - Valid registration
  - Mismatched passwords
  - Invalid email format
  - Empty fields
  - Duplicate email
- Automated test script in **Python using Selenium WebDriver**
- Dynamic email generation to prevent conflicts
- Assert-based validation and error handling
- Screenshot saved on test failure for debugging

---

## Project Structure

registration_test/
├── registration_test.py # Selenium automation script
├── test_cases.md # Manual test cases in markdown
├── registration_test_fail.png # Screenshot captured on test failure (if any)
└── README.md # Project description


---

## Tech Stack

- Python 3.9+
- Selenium WebDriver
- ChromeDriver
- WebDriverWait for dynamic page handling

---

## How to Run the Script

1. Install required packages:
```bash
pip install selenium

2. Run the test:
python registration_test.py

3. If the test fails, check the screenshot:
registration_test_fail.png


Manual Test Cases Overview
Test Case	Description
TC1	Valid registration with correct data
TC2	Password and confirmation mismatch
TC3	Invalid email format
TC4	Submit with all fields empty
TC5	Attempt to register with existing email

Full details in test_cases.md


---

## Projects in This Repository

### 1. Registration Test (automationexercise.com)

Includes manual test cases and Selenium automation for user registration form.  
Covers valid input, invalid email, mismatched passwords, and duplicate email handling.

**Files:**
- `registration_test.py`
- `test_cases.md`

---

### 🛒 2. E-commerce Cart Test

Simulates adding two products to cart, verifying item count and total price ($50).  
Also includes 3 manual test cases for adding, removing, and checking cart total.

**Files:**
- `cart_test.py`
- `cart_test_cases.md`
