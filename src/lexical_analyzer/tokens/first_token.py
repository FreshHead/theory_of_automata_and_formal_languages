from src.lexical_analyzer.tokens.token import Token
from src.lexical_analyzer.tokens.token import TokenName


class FirstToken(Token):
    type = TokenName.FIRST
    error = None

    def __init__(self, word):
        super().__init__(word)
        self.error = self.__A(self.transliterated, 0)

    def __A(self, transliterated, current_index):
        current = transliterated[current_index]
        next_index = current_index + 1
        if current.value == '0':
            return self.__B(transliterated, next_index)
        return 'Wrong ' + str(next_index) + ' symbol!' + ' Perhaps you mean 0 ?'

    def __B(self, transliterated, current_index):
        current = transliterated[current_index]
        next_index = current_index + 1
        if current.value == '0':
            return self.__D(transliterated, next_index)
        elif current.value == '1':
            return self.__C(transliterated, next_index)
        return 'Wrong ' + str(next_index) + ' symbol!' + ' Perhaps you mean 0 or 1 ?'

    def __D(self, transliterated, current_index):
        current = transliterated[current_index]
        next_index = current_index + 1
        if current.value == '0':
            return self.__EFin(transliterated, next_index)
        return 'Wrong ' + str(next_index) + ' symbol!' + ' Perhaps you mean 0 ?'

    def __C(self, transliterated, current_index):
        current = transliterated[current_index]
        next_index = current_index + 1
        if current.value == '0':
            return self.__A(transliterated, next_index)
        return 'Wrong ' + str(next_index) + ' symbol!' + ' Perhaps you mean 0 ?'

    def __EFin(self, transliterated, current_index):
        if len(transliterated) == current_index:
            return None
        current = transliterated[current_index]
        next_index = current_index + 1
        if current.value == '0':
            return self.__F(transliterated, next_index)
        return 'Wrong ' + str(next_index) + ' symbol!' + ' Perhaps you mean 0 ?'

    def __F(self, transliterated, current_index):
        current = transliterated[current_index]
        next_index = current_index + 1
        if current.value == '0':
            return self.__G(transliterated, next_index)
        return 'Wrong ' + str(next_index) + ' symbol!' + ' Perhaps you mean 0 ?'

    def __G(self, transliterated, current_index):
        current = transliterated[current_index]
        next_index = current_index + 1
        if current.value == '1':
            return self.__EFin(transliterated, next_index)
        return 'Wrong ' + str(next_index) + ' symbol!' + ' Perhaps you mean 1 ?'
