# 🧾 Manual Test Cases for User Registration

## Test Case 1: Valid Registration
**Steps:**
1. Open registration page
2. Enter:
   - Username: testuser
   - Email: test@example.com
   - Password: StrongPass123!
   - Confirm password: StrongPass123!
3. Click “Register”

**Expected Result:**  
Success message shown, user redirected to login page.

---

## Test Case 2: Password Mismatch
**Steps:**
1. Fill in all fields correctly, but enter different confirm password
2. Click “Register”

**Expected Result:**  
Error: “Passwords do not match”

---

## Test Case 3: Invalid Email Format
**Steps:**
1. Enter `invalidemail` as email
2. Fill other fields correctly

**Expected Result:**  
Error message near email field: “Invalid email format”

---

## Test Case 4: Empty Fields
**Steps:**
1. Click “Register” without filling anything

**Expected Result:**  
Validation errors shown for all required fields

---

## Test Case 5: Duplicate Email
**Steps:**
1. Use an already registered email

**Expected Result:**  
Error: “Email already registered”
