# 🧾 Manual Test Cases for Cart Functionality

## Test Case 1: Add Product to Cart
**Steps:**
1. Open product listing page
2. Click “Add to cart” on any product
3. Go to cart

**Expected Result:**  
Product appears in the cart with correct name, quantity (1), and price.

---

## Test Case 2: Remove Product from Cart
**Steps:**
1. Add a product to cart
2. Go to cart
3. Click “Remove” next to the product

**Expected Result:**  
Product disappears from cart. Total is updated or becomes $0.

---

## Test Case 3: Verify Total with Two Products
**Steps:**
1. Add Product A ($20) and Product B ($30) to cart
2. Go to cart
3. Verify listed products and total amount

**Expected Result:**  
Two products are listed, total equals $50.
