import re

def check_password_strength(password):
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"[0-9]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = 0
    if length:
        score += 1
    if upper:
        score += 1
    if lower:
        score += 1
    if digit:
        score += 1
    if special:
        score += 1

    if score <= 2:
        return "Weak Password ❌"
    elif score == 3 or score == 4:
        return "Medium Password ⚠"
    else:
        return "Strong Password ✅"

password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
