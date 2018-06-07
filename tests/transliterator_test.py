from transliterator import TokenName, transliterate_symbol

assert transliterate_symbol('a').name == TokenName.LETTER
for symbol in "010000001aaadddc adc  dcc 0100001 ":
    token = transliterate_symbol(symbol)
    print("'", token.value, "' is ", token.name, sep='')
