from src.transliterator import transliterate_symbol
import time


def on_start_clicked(self, input_buffer, output_buffer):
    output_string = "New transliteration started:\n"
    input_string = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    iter_ = output_buffer.get_end_iter()
    for symbol in input_string:
        token = transliterate_symbol(symbol)
        output_buffer.insert(iter_, "[%s] %s is %s\n" % (str(time.time()), token.value, str(token.name)))
        # output_string += "'" + token.value + "' is " + str(token.name) + '\n'
        # output_buffer.set_text(output_string)
