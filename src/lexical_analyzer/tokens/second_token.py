def start(transliterated):
    return __A(transliterated, 0)


def __A(transliterated, current_index):
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == 'c':
        return __B(transliterated, next_index)


def __B(transliterated, current_index):
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == 'a':
        return __CFin(transliterated, next_index)


def __CFin(transliterated, current_index):
    if len(transliterated) == current_index:
        return None
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value in "abcd":
        return __CFin(transliterated, next_index)
