def is_armstrong_number(number):
    if number < 0:
        return False
    original = number
    num_digits = 0
    temp = number
    while temp > 0:
        temp //= 10
        num_digits += 1
    total = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10
    return total == original
