from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://example.com/products")  # Replace with the actual product page URL

try:
    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Add first product to cart
    add_first = driver.find_element(By.XPATH, "//button[@data-product-name='Product 1']")
    add_first.click()

    # Add second product to cart
    add_second = driver.find_element(By.XPATH, "//button[@data-product-name='Product 2']")
    add_second.click()

    # Go to cart
    cart_button = driver.find_element(By.ID, "cart-icon")
    cart_button.click()

    # Wait for cart page
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cart-item")))

    # Verify 2 items are in the cart
    items = driver.find_elements(By.CLASS_NAME, "cart-item")
    assert len(items) == 2, f"Expected 2 items in cart, found {len(items)}"

    # Verify total amount
    total_text = driver.find_element(By.ID, "cart-total").text
    total = float(total_text.replace('$', '').strip())
    assert total == 50.0, f"Expected total $50.00, but got ${total}"

    print("✅ Cart test passed successfully!")

except Exception as e:
    driver.save_screenshot("cart_test_fail.png")
    print("❌ Test failed:", str(e))

finally:
    time.sleep(2)
    driver.quit()
