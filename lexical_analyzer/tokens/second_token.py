from lexical_analyzer.tokens.token import Token, TokenType
from all_in_one.custom_exceptions import LexicalAnalyzeException


class SecondToken(Token):
    def __init__(self, word):
        super().__init__(word, TokenType.SECOND)
        try:
            self.__A(self.transliterated, 0)
        except LexicalAnalyzeException as e:
            e.token = self
            raise e

    def __A(self, transliterated, current_index):
        current = transliterated[current_index]
        next_index = current_index + 1
        if current.value == 'c':
            self.__B(transliterated, next_index)
        else:
            raise LexicalAnalyzeException("Wrong %s symbol! Do you mean c?" % str(current_index + 1))

    def __B(self, transliterated, current_index):
        current = transliterated[current_index]
        next_index = current_index + 1
        if current.value == 'a':
            self.__CFin(transliterated, next_index)
        else:
            raise LexicalAnalyzeException("Wrong %s symbol! Do you mean a?" % str(current_index + 1))

    def __CFin(self, transliterated, current_index):
        if len(transliterated) == current_index:
            return  # все символы анализированы
        else:
            current = transliterated[current_index]
            next_index = current_index + 1
            if current.value in 'abcd':
                self.__CFin(transliterated, next_index)
            else:
                raise LexicalAnalyzeException("Wrong %s symbol! Do you mean a, b, c or d?" % str(current_index + 1))
