"""
   S--> <1> A S
   S--> <2>
   A--> <1>
   A-->  <2> S A
"""
from src.lexical_analyzer.lexical_analyzer import analyze
from src.lexical_analyzer.tokens.token import TokenName


class Node:
    def __init__(self, name, left=None, middle=None, right=None):
        self.name = name
        self.left = left
        self.middle = middle
        self.right = right

    def to_string(self):
        result = self.name
        if self.left:
            result += "=>(" + self.left.to_string()
        else:
            return result
        if self.middle:
            result += ", " + self.middle.to_string()
        if self.right:
            result += ", " + self.right.to_string()
        return result + ")"


class SyntaxAnalyzer:
    def __init__(self, string):
        self.tokens = analyze(string)
        self.current_index = -1

    def analyze(self):
        root = self.S()
        if len(self.tokens) > self.current_index + 1:
            raise Exception("Can't analyze after " + str(self.current_index + 1) + " word. Maybe this must be the last?")
        return root

    def S(self):
        self.current_index = self.current_index + 1
        if len(self.tokens) <= self.current_index:
            raise Exception(
                "Syntax error: Unexpected end of sentence! Cannot get " + str(self.current_index + 1) + " word for S")
        terminal = self.tokens[self.current_index].type
        if terminal == TokenName.FIRST:
            return Node("S", Node(terminal.value), self.A(), self.S())
        elif terminal == TokenName.SECOND:
            return Node("S", Node(terminal.value))
        else:
            raise Exception("Syntax error: Unknown token!")

    def A(self):
        self.current_index = self.current_index + 1
        if len(self.tokens) <= self.current_index:
            raise Exception(
                "Syntax error: Unexpected end of sentence! Cannot get " + str(self.current_index + 1) + " word for A")
        terminal = self.tokens[self.current_index].type
        if terminal == TokenName.FIRST:
            return Node("A", Node(terminal.value))
        elif terminal == TokenName.SECOND:
            return Node("A", Node(terminal.value), self.S(), self.A())
        else:
            raise Exception("Syntax error: Unknown token!")
