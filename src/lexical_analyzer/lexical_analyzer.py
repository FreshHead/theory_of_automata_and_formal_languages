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
from src.lexical_analyzer.tokens import first_token

from src.lexical_analyzer.tokens import second_token
from src.transliterator.transliterator import transliterate_symbol, transliterate_word, SymbolName


def analyze(string):
    words = []
    string = string.replace('\n', '')
    for word in string.split(' '):
        if len(word) != 0:
            words.append(word)
    word_type = ""
    error = None
    results = []
    for word in words:
        t_symbol = transliterate_symbol(word[0])
        if t_symbol.name == SymbolName.DIGIT:
            word_type = "FIRST"
            error = first_token.start(transliterate_word(word))
        elif t_symbol.name == SymbolName.LETTER:
            word_type = "SECOND"
            error = second_token.start((transliterate_word(word)))
        word_result = "Type of " + word + " is: " + word_type
        if error:
            word_result += " Error: " + error
        results.append(word_result)
    return results
