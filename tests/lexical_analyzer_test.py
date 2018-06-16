from src.lexical_analyzer import analyze

"""
первый тип слов: (010)*000(001)*
"""
print(analyze('000'))
print(analyze('000001'))
print(analyze('000001001'))
print(analyze('010010000001001'))
