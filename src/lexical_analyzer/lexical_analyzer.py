"""
========================================================================================================================
Задание:
    Разработать лексический анализатор.
    На вход подаются два вида слов в любом порядке, разделенные любым количеством пробелов.
    Текст может быть многострочным.
    Текст может содержать комментарии.
    Шаблон комментария разработать самостоятельно.
    Комментарии и пробелы должны пропускаться.
Вариант 14:
    первый тип слов: (010)*000(001)*
    второй тип слов: (a|b|c|d)+ (Первые два символа второго типа всегда ca)
========================================================================================================================
Пробел используется для разделения типов слов, в остальных случаях он опускается.
========================================================================================================================
"""
from src.lexical_analyzer.tokens.first_token import FirstToken
from src.lexical_analyzer.tokens.second_token import SecondToken
from src.lexical_analyzer.tokens.unknown_token import UnknownToken
from src.transliterator.transliterator import transliterate_symbol, SymbolName


def to_list(string):
    words = []
    string = string.replace('\n', '')
    for word in string.split(' '):
        if len(word) != 0:
            words.append(word)
    return words


def analyze(string):
    tokens = []
    for word in to_list(string):
        t_symbol = transliterate_symbol(word[0])
        if t_symbol.name == SymbolName.DIGIT:
            token = FirstToken(word)
        elif t_symbol.name == SymbolName.LETTER:
            token = SecondToken(word)
        else:
            token = UnknownToken(word)
            pass
        tokens.append(token)
    return tokens
