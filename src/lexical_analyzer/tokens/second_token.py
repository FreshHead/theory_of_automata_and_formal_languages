from src.lexical_analyzer.tokens.token import Token
from src.lexical_analyzer.tokens.token import TokenName


class SecondToken(Token):
    type = TokenName.UNKNOWN
    error = None

    def __init__(self, word):
        super().__init__(word)
        self.error = self.__A(self.transliterated, 0)

    def __A(self, transliterated, current_index):
        current = transliterated[current_index]
        next_index = current_index + 1
        if current.value == 'c':
            return self.__B(transliterated, next_index)
        return 'Wrong ' + str(next_index) + ' symbol!' + ' Perhaps you mean c ?'

    def __B(self, transliterated, current_index):
        current = transliterated[current_index]
        next_index = current_index + 1
        if current.value == 'a':
            return self.__CFin(transliterated, next_index)
        return 'Wrong ' + str(next_index) + ' symbol!' + ' Perhaps you mean a ?'


    def __CFin(self, transliterated, current_index):
        if len(transliterated) == current_index:
            return None
        current = transliterated[current_index]
        next_index = current_index + 1
        if current.value in 'abcd':
            return self.__CFin(transliterated, next_index)
        return 'Wrong ' + str(next_index) + ' symbol!' + ' Perhaps you mean a, b, c or d ?'
