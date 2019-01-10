from lexical_analyzer.tokens.token import Token, TokenType


class SpecialToken(Token):
    def __init__(self, word):
        super().__init__(word, TokenType.SPECIAL)