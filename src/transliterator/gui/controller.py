from src.transliterator.transliterator import transliterate_symbol


def on_start_clicked(self, input_buffer, output_buffer):
    source = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    # source = source_text.get('1.0', 'end')[:-1]  # [:-1] is removing last '\n' added from Text class
    for symbol in source:
        token = transliterate_symbol(symbol)
        output_buffer.insert_at_cursor('%s\n' % token.to_string())
        # message_listbox.insert(len(message_listbox.children), token.to_string())
