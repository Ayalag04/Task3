import re

def validate_password(password):
    print(f"Checking password: {password}")
    
    if len(password) < 8:
        return "Password is too short. It must be at least 8 characters long."
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r'[\W_]', password):
        return "Password must contain at least one special character."
    if not re.search(r'\d', password):
        return "Password must contain at least one digit."
    if re.search(r'(.)\1\1', password):
        return "Password cannot contain more than two repeating characters."
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i+1]) and ord(password[i+1]) + 1 == ord(password[i+2]):
            return "Password cannot contain sequential characters (e.g., abc, 123)."
    return "Password is valid."


#my tests
passwords_to_test = [
    "short1", "12345678",  # אורך מינימלי
    "ABCDEFGH1!", "Abcd1234!",  # אות קטנה
    "abcd1234!", "Abcd1234!",  # אות גדולה
    "Abcd1234", "Abcd1234!",  # תו מיוחד
    "Abcd!efg", "Abcd123!",  # ספרה
    "AaaBbbCcc", "A1B2C3!",  # תווים חוזרים
    "abc123!", "Xyz789!", "Abcd123!"  # רצפים עוקבים
]

for password in passwords_to_test:
    result = validate_password(password)
    if result == "Password is valid.":
        print(f"Password '{password}' is valid.")
    else:
        print(f"Password '{password}' is invalid because: " + result)
