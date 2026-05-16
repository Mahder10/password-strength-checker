import string

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isalpha() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    if strength <= 1:
        return "Weak"
    elif strength == 2 or strength == 3:
        return "Medium"
    else:
        return "Strong"

print("=== Password Strength Checker ===")
password = input("Enter password: ")

print("Strength:", check_password_strength(password))
