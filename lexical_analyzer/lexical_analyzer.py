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
from lexical_analyzer.tokens.first_token import FirstToken
from lexical_analyzer.tokens.second_token import SecondToken
from lexical_analyzer.tokens.special_token import SpecialToken
from lexical_analyzer.tokens.unknown_token import UnknownToken
from all_in_one.custom_exceptions import LexicalAnalyzeException
from transliterator.transliterator import transliterate_symbol, SymbolType


def to_list(string):
    words = []
    string = string.replace('\n', '')
    for word in string.split(SymbolType.SPACE.value):
        if len(word) != 0:
            words.append(word)
    return words


def analyze_word(word):
    t_symbol = transliterate_symbol(word[0])
    if t_symbol.symbol_type == SymbolType.DIGIT:
        return FirstToken(word)
    elif t_symbol.symbol_type == SymbolType.LETTER:
        return SecondToken(word)
    elif t_symbol.symbol_type == SymbolType.SPECIAL:
        return SpecialToken(word)
    else:
        raise LexicalAnalyzeException("Unknown token!", UnknownToken(word))


def analyze(string):
    tokens = []
    for word in to_list(string):
        tokens.append(analyze_word(word))
    return tokens
