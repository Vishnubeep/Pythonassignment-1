# math_utils.py

def factorial(num):
    """Return num! for a non-negative integer."""
    if not isinstance(num, int):
        raise TypeError("factorial() only accepts integers")
    if num < 0:
        raise ValueError("factorial() not defined for negative numbers")

    if num == 0 or num == 1:
        return 1

    return num * factorial(num - 1)


def is_prime(num):
    """Return True if num is prime, False if not."""
    if not isinstance(num, int):
        raise TypeError("is_prime() only accepts integers")
    if num <= 1:
        raise ValueError("is_prime() only defined for integers greater than 1")

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for check in range(3, int(num**0.5) + 1, 2):
        if num % check == 0:
            return False

    return True
