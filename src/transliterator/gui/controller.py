from src.transliterator.transliterator import transliterate_symbol


def on_start_clicked(self, input_buffer, output_buffer):
    output_buffer.delete(output_buffer.get_start_iter(), output_buffer.get_end_iter())
    source = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    for symbol in source:
        token = transliterate_symbol(symbol)
        output_buffer.insert_at_cursor('%s\n' % token.to_string())