from prime import generate_prime_factors


def test_integer_check():
    assert generate_prime_factors('X') == ValueError

def test_result_one():
    assert generate_prime_factors(1) == []