from all_in_one.custom_exceptions import SyntaxAnalyzeException
from lexical_analyzer.tokens.token import TokenType
from syntax_analyzer.syntax_analyzer import Node


def analyze(tokens_iter):
    root = s(tokens_iter)
    return root


def s(tokens_iter):
    try:
        terminal = next(tokens_iter).token_type
    except StopIteration:
        raise SyntaxAnalyzeException("Unexpected end of sentence! Terminal for S is expected!")
    if terminal == TokenType.FIRST:
        return Node("S", Node(terminal.value), a(tokens_iter), s(tokens_iter))
    elif terminal == TokenType.SECOND:
        return Node("S", Node(terminal.value))
    else:
        raise SyntaxAnalyzeException("Unknown token!")


def a(tokens):
    try:
        terminal = next(tokens).token_type
    except StopIteration:
        raise SyntaxAnalyzeException("Unexpected end of sentence! Terminal for A is expected!")
    if terminal == TokenType.FIRST:
        return Node("A", Node(terminal.value))
    elif terminal == TokenType.SECOND:
        return Node("A", Node(terminal.value), s(tokens), a(tokens))
    else:
        raise SyntaxAnalyzeException("Unknown token!")
