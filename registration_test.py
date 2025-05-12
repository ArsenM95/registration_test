from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Generate a unique email using timestamp
timestamp = int(time.time())
random_email = f"testuser{timestamp}@example.com"

# Launch Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://automationexercise.com/signup")

try:
    # Wait for signup form to load
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "name")))

    # Fill in name and email for signup
    driver.find_element(By.NAME, "name").send_keys("TestUser")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(random_email)

    # Click "Signup" button
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    # Wait for the account information form to appear
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "id_gender1")))

    # Fill in basic account info
    driver.find_element(By.ID, "id_gender1").click()
    driver.find_element(By.ID, "password").send_keys("StrongPass123!")

    # Set date of birth
    driver.find_element(By.ID, "days").send_keys("1")
    driver.find_element(By.ID, "months").send_keys("January")
    driver.find_element(By.ID, "years").send_keys("2000")

    # Fill in address info
    driver.find_element(By.ID, "first_name").send_keys("Test")
    driver.find_element(By.ID, "last_name").send_keys("User")
    driver.find_element(By.ID, "address1").send_keys("123 Test Street")
    driver.find_element(By.ID, "state").send_keys("TestState")
    driver.find_element(By.ID, "city").send_keys("TestCity")
    driver.find_element(By.ID, "zipcode").send_keys("12345")
    driver.find_element(By.ID, "mobile_number").send_keys("1234567890")

    # Click "Create Account"
    driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()

    # Wait for confirmation
    success_msg = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//b[text()='Account Created!']"))
    )

    assert "Account Created!" in success_msg.text, "❌ Account creation message not found"
    print("✅ Registration test passed successfully!")

except Exception as e:
    driver.save_screenshot("registration_test_fail.png")
    print("❌ Test failed:", str(e))

finally:
    time.sleep(3)
    driver.quit()