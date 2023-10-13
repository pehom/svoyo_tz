import math

import pytest
from prime_numbers import prime_numbers


@pytest.mark.parametrize('low, high', [
    (1, 100.1),
    (1.2, 100),
    (0b01, '100')
])
def test_valid_args(low, high):
    exp = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert prime_numbers(low, high) == exp


@pytest.mark.parametrize('low, high', [
    (1, 100)
])
def test_actually_prime_numbers(low, high):
    numbers = prime_numbers(low, high)
    for x in numbers:
        for i in range(2, int(math.sqrt(x)+1)):
            assert x % i != 0


@pytest.mark.parametrize('low, high', [
    (1, 100)
])
def test_sorted_results(low, high):
    data = prime_numbers(low, high)
    if data:
        prev = data[0]
        for x in data[1:]:
            assert x > prev
            prev = x


@pytest.mark.parametrize('low, high', [
    (2, 'fskj'),
    ('asdolk', 10000),

])
def test_invalid_args(low, high):
    assert prime_numbers(low, high) == []
