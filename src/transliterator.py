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
From wiki:
    A lexical token or simply token is a string with an assigned and thus identified meaning.
    It is structured as a pair consisting of a token name and an optional token value.
    The token name is a category of lexical unit.
========================================================================================================================
"""
from enum import Enum


class TokenName(Enum):
    DIGIT = ('0', '1')
    LETTER = ('a', 'b', 'c', 'd', '1')
    SPACE = ' '
    UNKNOWN = 'UNKNOWN'


class Token:
    special = {"\n": "'\\n'", "\t": "'\\t'"}

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def to_string(self):
        prepared_value = self.value
        if self.value in self.special:
            prepared_value = self.special[self.value]
        return "'" + prepared_value + "' is " + str(self.name)


def transliterate_symbol(symbol):
    assert len(symbol) == 1, "Length of symbol must be 1!"
    for name in TokenName:
        if symbol in name.value:
            return Token(name, symbol)
    return Token(TokenName.UNKNOWN, symbol)