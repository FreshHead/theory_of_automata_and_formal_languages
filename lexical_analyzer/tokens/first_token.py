from lexical_analyzer.tokens.token import Token, TokenType
from all_in_one.custom_exceptions import LexicalAnalyzeException


class FirstToken(Token):
    def __init__(self, word):
        super().__init__(word, TokenType.FIRST)
        try:
            if len(word) % 3 != 0:
                raise LexicalAnalyzeException("Word length must be a multiple of three!")
            self.__A(self.transliterated, 0)
        except LexicalAnalyzeException as e:
            e.token = self
            raise e

    def __A(self, transliterated, current_index):
        current = transliterated[current_index]
        if current.value == '0':
            self.__B(transliterated, current_index + 1)
        else:
            raise LexicalAnalyzeException("Wrong %s symbol! Do you mean 0?" % str(current_index + 1))

    def __B(self, transliterated, current_index):
        current = transliterated[current_index]
        next_index = current_index + 1
        if current.value == '0':
            self.__D(transliterated, next_index)
        elif current.value == '1':
            self.__C(transliterated, next_index)
        else:
            raise LexicalAnalyzeException("Wrong %s symbol! Do you mean 0 or 1?" % str(current_index + 1))

    def __D(self, transliterated, current_index):
        current = transliterated[current_index]
        next_index = current_index + 1
        if current.value == '0':
            self.__EFin(transliterated, next_index)
        else:
            raise LexicalAnalyzeException("Wrong %s symbol! Do you mean 0?" % str(current_index + 1))

    def __C(self, transliterated, current_index):
        current = transliterated[current_index]
        next_index = current_index + 1
        if current.value == '0':
            self.__A(transliterated, next_index)
        else:
            raise LexicalAnalyzeException("Wrong %s symbol! Do you mean 0?" % str(current_index + 1))

    def __EFin(self, transliterated, current_index):
        if len(transliterated) == current_index:
            return  # все символы анализированы
        else:
            current = transliterated[current_index]
            if current.value == '0':
                self.__F(transliterated, current_index + 1)
            else:
                raise LexicalAnalyzeException("Wrong %s symbol! Do you mean 0?" % str(current_index + 1))

    def __F(self, transliterated, current_index):
        current = transliterated[current_index]
        if current.value == '0':
            self.__G(transliterated, current_index + 1)
        else:
            raise LexicalAnalyzeException("Wrong %s symbol! Do you mean 0?" % str(current_index + 1))

    def __G(self, transliterated, current_index):
        current = transliterated[current_index]
        if current.value == '1':
            self.__EFin(transliterated, current_index + 1)
        else:
            raise LexicalAnalyzeException("Wrong %s symbol! Do you mean 1?" % str(current_index + 1))
