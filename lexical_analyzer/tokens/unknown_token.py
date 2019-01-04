from lexical_analyzer.tokens.token import Token, TokenType


class UnknownToken(Token):
    def __init__(self, word):
        super().__init__(word, TokenType.UNKNOWN)
        self.error = 'Unknown type of token!'
