"""Determine if a number is an Armstrong number."""

def is_armstrong_number(number):
    """
    Check if a number is an Armstrong number.
    
    An Armstrong number equals the sum of its digits each raised to the power
    of the number of digits.
    
    Args:
        number (int): The number to check.
        
    Returns:
        bool: True if Armstrong number, False otherwise.
    """
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
