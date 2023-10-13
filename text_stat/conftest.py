import random

import pytest


def get_word():
    alpha = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
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
    syms = [',', '.', '?', ':', ';', '!', '@']
    for _ in range(9):
        line += get_word()
        if random.randint(0, 100) > 80:
            line += syms[random.randint(0, len(syms)-1)] + ' '
        else:
            line += ' '
    line += get_word() + '\n'
    return line


@pytest.fixture(scope='function')
def create_testfile():
    testfile = 'text_stat/randomly_generated_file.txt'
    with open(testfile, mode='w', encoding='utf-8') as f:
        for _ in range(5):
            line = ''
            if random.randint(0, 1):
                line += '\t'
            f.write(line+get_line())
    return testfile


if __name__ == '__main__':
    # get_testfile()
    pass