import string


def text_stat(filename: str):
    try:
        if type(filename) != str:
            raise TypeError(f'Wrong argument: {filename}. It must be string')
        with open(filename, mode='r', encoding='utf-8') as f:
            data = f.readlines()
        ru_letters = set('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        letters = set('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя' + string.ascii_letters)
        temp_res = {'word_amount': 0,
                    'paragraph_amount': 0,
                    'bilingual_word_amount': 0}
        current_word_number = 0
        for line in data:
            words = line.split()
            if words:  # check if line is not empty
                if line[:1] == '\t':
                    temp_res['paragraph_amount'] += 1
                for item in words:
                    is_en = False
                    is_ru = False
                    is_word = False
                    current_word_number += 1
                    for c in item:
                        if c in letters:
                            is_word = True
                            if c in ru_letters:
                                is_ru = True
                            else:
                                is_en = True
                            try:
                                temp_res[c]['c_amount'] += 1
                                if current_word_number != temp_res[c]['last_word_number'] and is_word:
                                    temp_res[c]['w_amount'] += 1
                                    temp_res[c]['last_word_number'] = current_word_number
                            except KeyError:
                                temp_res[c] = {'c_amount': 1, 'w_amount': 1,
                                               'last_word_number': current_word_number}
                    if is_ru and is_en:
                        temp_res['bilingual_word_amount'] += 1
                    if is_word:
                        temp_res['word_amount'] += 1

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

