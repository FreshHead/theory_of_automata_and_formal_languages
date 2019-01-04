from transliterator.transliterator import transliterate_symbol
from lexical_analyzer.lexical_analyzer import analyze as lex_analyze
from all_in_one.gui_functions import insert_to_buffer
import time


def on_start_clicked(self, source_buffer, message_buffer, output_buffer):
    message_buffer.delete(message_buffer.get_start_iter(), message_buffer.get_end_iter())
    transliterate(source_buffer, message_buffer)
    lexical_analyze(source_buffer, message_buffer)


def transliterate(input_buffer, output_buffer):
    insert_to_buffer(output_buffer, 'Transliteration started:')
    source = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    for symbol in source:
        token = transliterate_symbol(symbol)
        insert_to_buffer(output_buffer, token.to_string())
    insert_to_buffer(output_buffer, 'Transliteration was finished.')


def lexical_analyze(input_buffer, output_buffer):
    insert_to_buffer(output_buffer, 'Lexical analyze started:')
    input_string = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    tokens = lex_analyze(input_string)
    for token in tokens:
        token_message = 'Token: ' + token.word + ' of type: ' + token.type.name
        if token.error:
            token_message += ' has error: ' + token.error
            spaced_string = ' ' + input_string + ' '
            selection_start = spaced_string.find(' ' + token.word + ' ')
            selection_end = selection_start
            while spaced_string[selection_end + 1] != ' ':
                selection_end += 1
            start_iter = input_buffer.get_iter_at_offset(selection_start)
            end_iter = input_buffer.get_iter_at_offset(selection_end)
            input_buffer.select_range(start_iter, end_iter)
        insert_to_buffer(output_buffer, token_message)
    insert_to_buffer(output_buffer, 'Lexical analyze was finished.')