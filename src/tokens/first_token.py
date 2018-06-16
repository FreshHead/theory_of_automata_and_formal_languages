def start(transliterated, current_index):
    return __A(transliterated, current_index)


def __A(transliterated, current_index):
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == '0':
        return __B(transliterated, next_index)


def __B(transliterated, current_index):
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == '0':
        return __D(transliterated, next_index)
    elif current.value == '1':
        return __C(transliterated, next_index)


def __D(transliterated, current_index):
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == '0':
        return __EFin(transliterated, next_index)


def __C(transliterated, current_index):
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == '0':
        return __A(transliterated, next_index)


def __EFin(transliterated, current_index):
    if len(transliterated) == current_index:
        return "Done"
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == '0':
        return __F(transliterated, next_index)


def __F(transliterated, current_index):
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == '0':
        return __G(transliterated, next_index)


def __G(transliterated, current_index):
    current = transliterated[current_index]
    next_index = current_index + 1
    if current.value == '1':
        return __EFin(transliterated, next_index)
