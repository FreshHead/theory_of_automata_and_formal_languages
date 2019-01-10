from transliterator.transliterator import transliterate_symbol
from enum import Enum


class TokenType(Enum):
    FIRST = "1"
    SECOND = "2"
    SPECIAL = "3"
    UNKNOWN = "4"


class Token:
    def __init__(self, word, token_type):
        self.token_type = token_type
        self.word = word
        self.transliterated = []
        for symbol in word:
            self.transliterated.append(transliterate_symbol(symbol))

    def to_string(self):
        return 'Token "' + self.word + '" of type "' + self.token_type.name + '"'
