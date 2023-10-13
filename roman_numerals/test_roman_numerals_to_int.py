import pytest
from roman_numerals_to_int import roman_numerals_to_int


def test_valid_arg(get_valid_roman_numbers): # using fixture to get roman numbers in [1, 1700)
    print()
    for dec, roman in get_valid_roman_numbers.items():
        print(f'\tin: {roman}    out: {roman_numerals_to_int(roman)}')
        assert roman_numerals_to_int(roman) == dec


@pytest.mark.parametrize('number', [
    'IIIIII',
    '',
    'XXM',
    123,
    'xix',
    'XIХ',  # last letter is Cyrillic
    'MMA',
    'Vi',
    'V8XIX'
])
def test_invalid_arg(number):
    assert roman_numerals_to_int(number) is None

