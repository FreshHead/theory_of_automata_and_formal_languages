from lexical_analyzer.lexical_analyzer import analyze

"""
первый тип слов: (010)*000(001)*
"""
# print(analyze('000'))
# print(analyze('000001'))
# print(analyze('000001001'))
# print(analyze('010010000001001'))

"""
второй тип слов: (a|b|c|d)+ (Первые два символа второго типа всегда ca)
"""
# print(analyze('aabcd'))
# print(analyze('ca'))
# print(analyze('cacbbbd'))
print(analyze('cacbbdb 000         000001 101 \n0000000001'))