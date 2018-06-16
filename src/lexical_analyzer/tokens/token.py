from src.transliterator import transliterate_symbol
from enum import Enum


# class TokenName(Enum):
#     FIRST = 1
#     SECOND = 2
#     UNKNOWN = 3


class Token:
    def __init__(self, value):
        self.value = value
        self.transliterated_value = []
        for symbol in value:
            self.transliterated_value.append(transliterate_symbol(symbol))
        pass
