"""
   S--> <1> A S
   S--> <2>
   A--> <1>
   A-->  <2> S A
"""
from src.lexical_analyzer.lexical_analyzer import analyze
from src.lexical_analyzer.tokens.token import TokenName


class SyntaxAnalyzer:
    def __init__(self, string):
        self.tokens = analyze(string)
        self.current_index = -1
        pass

    def analyze(self):
        return self.S()

    def S(self):
        self.current_index = self.current_index + 1
        if self.tokens[self.current_index] == TokenName.SECOND:
            return self.Fin()
        elif self.tokens[self.current_index] == TokenName.FIRST:
            return self.A() and self.S()

    def Fin(self):
        self.current_index = self.current_index + 1
        if len(self.tokens) == self.current_index:
            return None
        else:
            return 'Previous word must be the last!'

    def A(self):
        self.current_index = self.current_index + 1
        if self.tokens[self.current_index] == TokenName.FIRST:
            return self.Fin()
        elif self.tokens[self.current_index] == TokenName.SECOND:
            return self.S() and self.S()
        pass
