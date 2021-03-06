"""
========================================================================================================================
Задание:
    Сформировать алфавит входного языка транслятора. К алфавиту необходимо добавить символ «Пробел».
    Для полученного алфавита разработать транслитератор (читатель символов).
    На вход подаются символы алфавита в любом порядке. Текст может быть многострочным.
    Вариант 14
    первый тип слов: (010)*000(001)*
    второй тип слов: (a|b|c|d)+
========================================================================================================================
Алфавит: {0, 1, a, b, c, d, 'символ " "'}
========================================================================================================================
"""
from enum import Enum

_special = {"\n": "'\\n'", "\t": "'\\t'"}


class SymbolType(Enum):
    DIGIT = ('0', '1')
    LETTER = ('a', 'b', 'c', 'd')
    SPACE = ' '
    SPECIAL = ('!', '=', '#', '(', ')', '-', '+')
    UNKNOWN = 'UNKNOWN'


class Symbol:
    def __init__(self, symbol_type, value):
        self.symbol_type = symbol_type
        self.value = value

    def to_string(self):
        prepared_value = self.value
        if self.value in _special:
            prepared_value = _special[self.value]
        return "'" + prepared_value + "' type is '" + str(self.symbol_type.name) + "'"


def transliterate_symbol(symbol):
    assert len(symbol) == 1, "Length of symbol must be 1!"
    for symbol_type in SymbolType:
        if symbol in symbol_type.value:
            return Symbol(symbol_type, symbol)
    return Symbol(SymbolType.UNKNOWN, symbol)


def transliterate_word(word):
    result = []
    for symbol in word:
        result.append(transliterate_symbol(symbol))
    return result
