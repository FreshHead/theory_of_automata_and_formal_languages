from lexical_analyzer.tokens.token import Token, TokenName


class UnknownToken(Token):
    def __init__(self, word):
        super().__init__(word)
        self.type = TokenName.UNKNOWN
        self.error = 'Unknown type of token!'