from src.transliterator.transliterator import SymbolName, transliterate_symbol

assert transliterate_symbol('a').name == SymbolName.LETTER
assert transliterate_symbol('1').name == SymbolName.DIGIT
assert transliterate_symbol(' ').name == SymbolName.SPACE
assert transliterate_symbol('@').name == SymbolName.UNKNOWN
for symbol in "010000001aaadddc adc  dcc 0100001 , nope!":
    token = transliterate_symbol(symbol)
    print("'", token.value, "' is ", token.name, sep='')
