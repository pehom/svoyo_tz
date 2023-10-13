import math


def prime_numbers(low, high):

    try:
        res = []
        for x in range(int(low), int(high)):
            is_good = True
            if x > 1:
                for i in range(2, int(math.sqrt(x)+1)):
                    if x % i == 0:
                        is_good = False
                        break
                if is_good:
                    res.append(x)
        return res
    except (TypeError, ValueError):
        return []

