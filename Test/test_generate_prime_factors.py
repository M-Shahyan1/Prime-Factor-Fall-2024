from prime import generate_prime_factors


def test_integer_check():
    assert generate_prime_factors('X') == ValueError

def test_result_one():
    assert generate_prime_factors(1) == []

def test_result_two():
    assert generate_prime_factors(2) == [2]

def test_result_three():
    assert generate_prime_factors(3) == [3]

def test_result_four():
    assert generate_prime_factors(4) == [2,2]

def test_result_six():
    assert generate_prime_factors(6) == [2,3]

def test_result_eight():
    assert generate_prime_factors(8) == [2,2,2]