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

    def analyze(self):
        return self.S()

    def S(self):
        self.current_index = self.current_index + 1
        if len(self.tokens) <= self.current_index:
            return "Error"
        if self.tokens[self.current_index].type == TokenName.FIRST:
            return self.A() + self.S()
        elif self.tokens[self.current_index].type == TokenName.SECOND:
            return ""

    def A(self):
        self.current_index = self.current_index + 1
        if len(self.tokens) <= self.current_index:
            return "Error"
        if self.tokens[self.current_index].type == TokenName.FIRST:
            return ""
        elif self.tokens[self.current_index].type == TokenName.SECOND:
            return self.S() + self.A()