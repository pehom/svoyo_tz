
import re


def roman_numerals_to_int(roman_numeral: str):

    pattern = re.compile(r"^M*(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$", re.VERBOSE)
    try:

        if pattern.match(roman_numeral) and len(roman_numeral) > 0:
            dec = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            res = dec[roman_numeral[0]]
            prev_rom = roman_numeral[0]
            for rom in roman_numeral[1:]:
                if dec[rom] > dec[prev_rom]:
                    res += dec[rom] - 2 * dec[prev_rom]
                else:
                    res += dec[rom]
                prev_rom = rom
            return res
        else:
            return None
    except TypeError:
        return None


if __name__ == '__main__':
    pass

