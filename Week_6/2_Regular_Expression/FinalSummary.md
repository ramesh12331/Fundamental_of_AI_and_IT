# 📘 Python Regular Expressions (RegEx) - Login System Validation

---

# 📖 Definition

This program uses **Python Regular Expressions (RegEx)** to validate a user's **email address** and **password** before checking the login credentials.

The program performs the following tasks:

* 📧 Validates the email format.
* 🔐 Validates the password format.
* 👤 Checks the entered credentials with stored user information.
* ✅ Displays whether the login is successful or not.

---

# 📥 Import Regular Expression Module

## 📖 Definition

Python provides the built-in **`re`** module to work with Regular Expressions.

## ⚙️ Syntax

```python
import re
```

---

# 📧 Email Validation

## 📖 Definition

Email validation checks whether the entered email follows the correct email format.

## ⚙️ Syntax

```python
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
```

## 💻 Example

```python
def validate_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.fullmatch(email_pattern, email):
        return True
    else:
        print("Invalid email address")
        return False
```

### 🖥️ Output

#### Valid Email

```text
karthik@datavalley.ai
```

Output

```text
True
```

#### Invalid Email

```text
karthik@gmail
```

Output

```text
Invalid email address
False
```

---

# 🔐 Password Validation

## 📖 Definition

Password validation checks whether the password satisfies all required security rules.

### Password Rules

* ✅ Minimum 8 Characters
* ✅ At least one Uppercase Letter
* ✅ At least one Lowercase Letter
* ✅ At least one Digit

## ⚙️ Syntax

```python
password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
```

## 💻 Example

```python
def validate_password(password):
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

    if re.fullmatch(password_regex, password):
        return True
    else:
        print("Incorrect password format")
        return False
```

### 🖥️ Output

#### Valid Password

```text
Karthik123
```

Output

```text
True
```

#### Invalid Password

```text
karthik
```

Output

```text
Incorrect password format
False
```

---

# 👤 Stored User Information

## 📖 Definition

The user's information is stored inside a **dictionary**. The entered email and password are compared with these stored values.

## 💻 Example

```python
user_info = {
    "name": "Karthik",
    "email": "karthik@datavalley.ai",
    "password": "Karthik123"
}
```

---

# ⌨️ User Input

## 📖 Definition

The program accepts the email address and password from the user.

## 💻 Example

```python
email = input("Enter your email address: ")
password = input("Enter the password: ")
```

---

# ✅ Credential Validation

## 📖 Definition

After validating the email and password formats, the program compares them with the stored user information.

If both match, login is successful.

Otherwise, an error message is displayed.

## 💻 Example

```python
if validate_email(email) and validate_password(password):

    if user_info["email"] == email and user_info["password"] == password:
        print("Credentials are valid")
    else:
        print("Incorrect credentials")
```

### 🖥️ Output

#### Case 1: Correct Email and Password

```text
Enter your email address:
karthik@datavalley.ai

Enter the password:
Karthik123
```

Output

```text
Credentials are valid
```

---

#### Case 2: Correct Format but Wrong Credentials

```text
Enter your email address:
abc@gmail.com

Enter the password:
Password123
```

Output

```text
Incorrect credentials
```

---

#### Case 3: Invalid Email Format

```text
Enter your email address:
abc@gmail
```

Output

```text
Invalid email address
```

---

#### Case 4: Invalid Password Format

```text
Enter the password:
hello
```

Output

```text
Incorrect password format
```

---

# 📝 Final Summary

✅ **`re.fullmatch()`** checks whether the **entire string** matches the given Regular Expression pattern.

✅ **Email Validation** ensures the entered email follows the correct format.

✅ **Password Validation** ensures the password meets the required security rules.

✅ **Dictionary (`user_info`)** stores the user's name, email, and password.

✅ The program first validates the input format and then checks whether the entered credentials match the stored user information.

---

# 🎤 Interview Questions

### ❓1. What is `re.fullmatch()`?

**Answer:**
`re.fullmatch()` checks whether the **entire string** matches the specified Regular Expression pattern.

---

### ❓2. Why is `re.fullmatch()` used instead of `re.match()`?

**Answer:**
`re.fullmatch()` ensures that the **entire input** matches the pattern, while `re.match()` checks only from the beginning of the string.

---

### ❓3. Why do we validate an email address?

**Answer:**
To ensure that the email follows the correct format before processing or storing it.

---

### ❓4. Why do we validate a password?

**Answer:**
To ensure that the password meets the required security rules, such as minimum length and the presence of uppercase letters, lowercase letters, and digits.

---

### ❓5. What is the purpose of the `user_info` dictionary?

**Answer:**
It stores the user's information (name, email, and password) so that the entered credentials can be compared with the stored values.

---

### ❓6. What happens if the email format is invalid?

**Answer:**
The program prints **"Invalid email address"** and returns `False`.

---

### ❓7. What happens if the password format is invalid?

**Answer:**
The program prints **"Incorrect password format"** and returns `False`.

---

### ❓8. What happens if both the email and password formats are valid, but the credentials do not match?

**Answer:**
The program prints **"Incorrect credentials"** because the entered values do not match the stored user information.
