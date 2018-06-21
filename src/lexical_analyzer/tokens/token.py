from src.transliterator.transliterator import transliterate_symbol
from enum import Enum


# class TokenName(Enum):
#     FIRST = 1
#     SECOND = 2
#     UNKNOWN = 3


class Token:
    def __init__(self, word):
        self.word = word
        self.transliterated = []
        for symbol in word:
            self.transliterated.append(transliterate_symbol(symbol))
