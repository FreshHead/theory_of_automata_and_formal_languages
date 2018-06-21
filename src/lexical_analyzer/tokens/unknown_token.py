from src.lexical_analyzer.tokens.token import Token


class UnknownToken(Token):
    def __init__(self, word):
        super().__init__(word)
        self.type = 'UNKNOWN'
        self.error = 'Unknown type of token!'
