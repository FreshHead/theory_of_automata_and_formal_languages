# class FirstToken(Token):
#     def __init__(self, value):
#         super(value)
#
#         return __A(transliterated, current_index)
#


def start(transliterated):
    return __A(transliterated, 0)


def __A(transliterated, current_index):
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == '0':
        return __B(transliterated, next_index)
    return "symbol № " + str(next_index) + " Perhaps you mean 0 ?"


def __B(transliterated, current_index):
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == '0':
        return __D(transliterated, next_index)
    elif current.value == '1':
        return __C(transliterated, next_index)
    return "symbol № " + str(next_index) + " Perhaps you mean 0 or 1 ?"


def __D(transliterated, current_index):
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == '0':
        return __EFin(transliterated, next_index)
    return "symbol № " + str(next_index) + " Perhaps you mean 0 ?"


def __C(transliterated, current_index):
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == '0':
        return __A(transliterated, next_index)
    return "symbol №" + str(next_index) + " Perhaps you mean 0 ?"


def __EFin(transliterated, current_index):
    if len(transliterated) == current_index:
        return None
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == '0':
        return __F(transliterated, next_index)
    return "symbol № " + str(next_index) + " Perhaps you mean 0 ?"


def __F(transliterated, current_index):
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == '0':
        return __G(transliterated, next_index)
    return "symbol № " + str(next_index) + " Perhaps you mean 0 ?"


def __G(transliterated, current_index):
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == '1':
        return __EFin(transliterated, next_index)
    return "symbol № " + str(next_index) + " Perhaps you mean 1 ?"
