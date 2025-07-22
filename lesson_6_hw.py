import string


def is_strong_password(password):
    if len(password) < 6:
        return False

    has_upper = any(c.isupper() for c in password) # True, если хотя бы один символ в пароле — заглавная буква
    has_lower = any(c.islower() for c in password) # True, если хотя бы один символ — строчная буква.
    has_digit = any(c.isdigit() for c in password) # True, если хотя бы одна цифра есть в пароле.
    special_chars = [c for c in password if c in string.punctuation] # это список всех спецсимволов в пароле

    if has_upper and has_lower and has_digit and len(special_chars) >= 2: # проверяет на все наши условия
        return True
    return False

print(is_strong_password("SPass?W/12"))  # ✅ True
print(is_strong_password("3gT*5?0"))     # ✅ True
print(is_strong_password("k2-IRI!?49"))  # ✅ True
print(is_strong_password("12345"))       # ❌ False
print(is_strong_password("password"))    # ❌ False
print(is_strong_password("77211"))       # ❌ False


def nearest_number(sequence, target=0):
    return min(sequence, key=lambda x: abs(x - target))


print(nearest_number([1, 2, 3], 5))          # 3
print(nearest_number((10.5, -2.3, 0), 1))  # 0
print(nearest_number([100, 200, 300], 150))  # 100
print(nearest_number([7, 8, 9]))             # 7 (ближе всего к 0)