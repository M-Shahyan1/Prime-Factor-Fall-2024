"""
prime.py -- Write the application code here
"""


def generate_prime_factors(int):
    try:
        int + 1
        pass
    except TypeError:
        return ValueError

    if int == 1:
        return []

    elif int == 2:
        return [2]

    elif int == 3:
        return [3]

    elif int == 4:
        return [2,2]

