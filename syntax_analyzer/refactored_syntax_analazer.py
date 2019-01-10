from all_in_one.custom_exceptions import SyntaxAnalyzeException
from lexical_analyzer.tokens.token import TokenType
from syntax_analyzer.syntax_analyzer import Node


def analyze(tokens_iter):
    root = s(tokens_iter)
    if has_next(tokens_iter):
        raise SyntaxAnalyzeException("Can't create syntax tree check tokens order.")
    if root:
        return root
    else:
        raise SyntaxAnalyzeException("Can't find root non terminal. Check the source string.")


def has_next(token_iter):
    try:
        next(token_iter)
        return True
    except StopIteration:
        return False


def s(tokens_iter):
    try:
        terminal = next(tokens_iter).token_type
    except StopIteration:
        raise SyntaxAnalyzeException("Unexpected end of sentence! Terminal for S is expected!")
    if terminal == TokenType.FIRST:
        return Node("S", Node(terminal.value), a(tokens_iter), s(tokens_iter))
    elif terminal == TokenType.SECOND:
        return Node("S", Node(terminal.value))
    elif terminal == TokenType.SPECIAL:
        return None
    else:
        raise SyntaxAnalyzeException("Unknown token!")


def a(tokens_iter):
    try:
        terminal = next(tokens_iter).token_type
    except StopIteration:
        raise SyntaxAnalyzeException("Unexpected end of sentence! Terminal for A is expected!")
    if terminal == TokenType.FIRST:
        return Node("A", Node(terminal.value))
    elif terminal == TokenType.SECOND:
        return Node("A", Node(terminal.value), s(tokens_iter), a(tokens_iter))
    elif terminal == TokenType.SPECIAL:
        return None
    else:
        raise SyntaxAnalyzeException("Unknown token!")


def check_for_duplicates(string, identifier_dict):
    duplicates_list = set()
    words = string.split(" ")
    for i in words:
        if words.count(i) >= 2:
            duplicates_list.add(i)
    identifier_set = set(identifier_dict.values())
    duplicates_list = identifier_set.intersection(set(duplicates_list)) # Исключим все дубликаты кроме идентифкаторов
    if duplicates_list:
        raise SyntaxAnalyzeException("Found duplicates in identifiers: " + str(duplicates_list) + "!")