from src.transliterator.transliterator import transliterate_symbol
import time


def on_start_clicked(self, input_buffer, output_buffer):
    input_string = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    output_buffer.insert_at_cursor("Transliteration started:\n")
    for symbol in input_string:
        token = transliterate_symbol(symbol)
        output_buffer.insert_at_cursor("[%s] %s\n" % (str(time.time()), token.to_string()))
