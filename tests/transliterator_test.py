from src.transliterator import TokenName, transliterate_symbol

assert transliterate_symbol('a').name == TokenName.LETTER
assert transliterate_symbol('1').name == TokenName.NUMBER
assert transliterate_symbol(' ').name == TokenName.SPACE
assert transliterate_symbol('@').name == TokenName.UNKNOWN
print(''.isspace())
for symbol in "010000001aaadddc adc  dcc 0100001 , nope!":
    token = transliterate_symbol(symbol)
    print("'", token.value, "' is ", token.name, sep='')
