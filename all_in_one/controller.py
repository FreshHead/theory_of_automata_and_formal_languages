from transliterator.transliterator import transliterate_symbol
from lexical_analyzer.lexical_analyzer import analyze as lex_analyze
from all_in_one.custom_exceptions import AnalyzeException, LexicalAnalyzeException
from all_in_one.gui_functions import insert_to_buffer
from syntax_analyzer.syntax_analyzer import SyntaxAnalyzer
from lexical_analyzer.lexical_analyzer import to_list, analyze_word


def on_start_clicked(self, source_buffer, message_buffer, result_buffer):
    try:
        message_buffer.delete(message_buffer.get_start_iter(), message_buffer.get_end_iter())
        transliterate(source_buffer, message_buffer)
        lexical_analyze(source_buffer, message_buffer)
        syntax_analyze(source_buffer, message_buffer)
    except AnalyzeException as e:
        insert_to_buffer(message_buffer, "%s: %s" % (e.__class__.__name__, e.args[0]))


def transliterate(input_buffer, output_buffer):
    insert_to_buffer(output_buffer, 'Transliteration started:')
    source = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    for symbol in source:
        token = transliterate_symbol(symbol)
        insert_to_buffer(output_buffer, token.to_string())
    insert_to_buffer(output_buffer, 'Transliteration finished.')


def lexical_analyze(input_buffer, output_buffer):
    insert_to_buffer(output_buffer, 'Lexical analyze started:')
    input_string = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    try:
        for word in to_list(input_string):
            token = analyze_word(word)
            insert_to_buffer(output_buffer, token.to_string())
    except LexicalAnalyzeException as e:
        spaced_string = ' ' + input_string + ' '
        selection_start = spaced_string.find(' ' + e.token.word + ' ')
        selection_end = selection_start
        while spaced_string[selection_end + 1] != ' ':
            selection_end += 1
        start_iter = input_buffer.get_iter_at_offset(selection_start)
        end_iter = input_buffer.get_iter_at_offset(selection_end)
        input_buffer.select_range(start_iter, end_iter)
        raise e

    insert_to_buffer(output_buffer, 'Lexical analyze finished.')


def syntax_analyze(input_buffer, output_buffer):
    input_string = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    insert_to_buffer(output_buffer, 'Syntax analyze started:')
    root_node = SyntaxAnalyzer(input_string).analyze()
    insert_to_buffer(output_buffer, root_node.to_string())
    insert_to_buffer(output_buffer, 'Syntax analyze finished:')
