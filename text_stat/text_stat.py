def is_bilingual(word: str):
    is_en = False
    is_ru = False
    for c in word:
        if c.isalpha():
            if c.lower() in 'abcdefghijklmnopqrstuvwxyz':
                is_en = True
            else:
                is_ru = True
            if c.lower() in 'abcdefghijklmnopqrstuvwxyz' and is_ru or c.lower() not in 'abcdefghijklmnopqrstuvwxyz' and is_en:
                return True
    return False


def is_word(data: str):
    for c in data:
        if c.isalpha():
            return True
    return False


def text_stat(filename: str):
    try:
        if type(filename) != str:
            raise TypeError(f'Wrong argument: {filename}. It must be string')
        with open(filename, mode='r', encoding='utf-8') as f:
            data = f.readlines()
            temp_res = {'word_amount': 0,
                        'paragraph_amount': 0,
                        'bilingual_word_amount': 0}
            current_word_number = 0
            for line in data:
                words = line.split()
                if words:   # check if line is not empty
                    if line[:1] == '\t':
                        temp_res['paragraph_amount'] += 1
                    for item in words:
                        if is_word(item):  # check if item is a word if it has any letter
                            current_word_number += 1
                            temp_res['word_amount'] += 1
                            if is_bilingual(item):
                                temp_res['bilingual_word_amount'] += 1
                            for c in item:
                                if c.isalpha():
                                    try:
                                        temp_res[c]['c_amount'] += 1
                                        if current_word_number != temp_res[c]['last_word_number']:
                                            temp_res[c]['w_amount'] += 1
                                            temp_res[c]['last_word_number'] = current_word_number
                                    except KeyError:
                                        temp_res[c] = {'c_amount': 1, 'w_amount': 1,
                                                       'last_word_number': current_word_number}
        res = {'bilingual_word_amount': temp_res['bilingual_word_amount'],
               'paragraph_amount': temp_res['paragraph_amount'],
               'word_amount': temp_res['word_amount']
               }
        for key in temp_res.keys():
            if len(key) == 1:
                # res[key] = (temp_res[key]['c_amount'], round(temp_res[key]['w_amount'] / res['word_amount'], 4))
                res[key] = (temp_res[key]['c_amount'], round(temp_res[key]['w_amount'] / res['word_amount'], 2))

        return res
    except (OSError, TypeError) as e:
        return {'error': e}

if __name__ == '__main__':
    print(text_stat('testfile2.txt'))
