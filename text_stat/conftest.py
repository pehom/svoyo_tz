import random
import string

import pytest


def get_word():
    alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'+string.ascii_lowercase
    word = ''
    for _ in range(1, random.randint(2, 10)):
        i = random.randint(0, len(alpha)-1)
        if random.randint(0, 1):
            word += alpha[i]
        else:
            word += alpha[i].upper()
    return word


def get_line():
    line = ''
    for _ in range(9):
        line += get_word()
        if random.randint(0, 100) > 80:
            line += random.choice(string.punctuation)
        else:
            line += ' '
    line += get_word() + '\n'
    return line


@pytest.fixture(scope='function')
def create_testfile():
    testfile = 'text_stat/random_file_from_fixture.txt'
    lines = []
    for _ in range(5):
        line = ''
        if random.randint(0, 1):
            line += '\t'
        lines.append(line + get_line())
    with open(testfile, mode='w', encoding='utf-8') as f:
        f.writelines(lines)

    return testfile
