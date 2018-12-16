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
        try:
            self.S()
            return "Sentence is correct!"
        except Exception as e:
            return e.args[0]

    def S(self):
        self.current_index = self.current_index + 1
        if len(self.tokens) <= self.current_index:
            raise Exception("Syntax error: Unexpected end of sentence!")
        if self.tokens[self.current_index].type == TokenName.FIRST:
            return self.A() + self.S()
        elif self.tokens[self.current_index].type == TokenName.SECOND:
            return
        else:
            raise Exception("Syntax error: Unknown token!")

    def A(self):
        self.current_index = self.current_index + 1
        if len(self.tokens) <= self.current_index:
            raise Exception("Syntax error: Unexpected end of sentence!")
        if self.tokens[self.current_index].type == TokenName.FIRST:
            return
        elif self.tokens[self.current_index].type == TokenName.SECOND:
            return self.S() + self.A()
        else:
            raise Exception("Syntax error: Unknown token!")