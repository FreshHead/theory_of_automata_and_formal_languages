from transliterator.transliterator import SymbolType, transliterate_symbol

assert transliterate_symbol('a').name == SymbolType.LETTER
assert transliterate_symbol('1').name == SymbolType.DIGIT
assert transliterate_symbol(' ').name == SymbolType.SPACE
assert transliterate_symbol('@').name == SymbolType.UNKNOWN

for symbol in "010000001aaadddc adc  dcc 0100001 , nope!":
    token = transliterate_symbol(symbol)
    print("'", token.value, "' is ", token.name, sep='')
