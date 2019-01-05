class AnalyzeException(Exception):
    pass


class LexicalAnalyzeException(AnalyzeException):
    def __init__(self, message, token=None):
        super(LexicalAnalyzeException, self).__init__(message)
        self.token = token


class SyntaxAnalyzeException(AnalyzeException):
    pass
