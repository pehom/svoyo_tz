import pytest

from text_stat import text_stat


@pytest.mark.parametrize('filename', [
    'text_stat/normal_file.txt'
])
def test_normal_file(filename):
    alpha_l = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alpha_u = alpha_l.upper()
    exp = {'bilingual_word_amount': 1, 'paragraph_amount': 2, 'word_amount': 16}
    for c in alpha_u + alpha_l:
        exp[c] = (1, 0.06)
    exp['A'] = (2, 0.12)
    assert text_stat(filename) == exp


@pytest.mark.parametrize('filename', [
    'text_stat/normal_file.txt',
    'text_stat/testfile2.txt',
    'text_stat/randomly_generated_file.txt'
])
def test_result_keys(filename, create_testfile):
    alpha_l = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alpha_u = alpha_l.upper()
    keys = {'bilingual_word_amount', 'paragraph_amount', 'word_amount'}
    for c in alpha_u+alpha_l:
        keys.add(c)
    assert set(text_stat(filename).keys()).issubset(keys)


@pytest.mark.parametrize('filename', [
    123,
    'not_existing_file.txt'
])
def test_wrong_argument(filename):
    assert 'error' in text_stat(filename).keys()


@pytest.mark.parametrize('filename', [
    'text_stat/no_words_file.txt'
])
def test_no_words_file(filename):
    keys = {'bilingual_word_amount', 'paragraph_amount', 'word_amount'}
    assert set(text_stat(filename).keys()) == keys
