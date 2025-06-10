from prime import generate_prime_factors


def test_integer_check():
    assert generate_prime_factors('X') == ValueError
