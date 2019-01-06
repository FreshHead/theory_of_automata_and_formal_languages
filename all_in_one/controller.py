from transliterator.transliterator import transliterate_symbol
from all_in_one.custom_exceptions import AnalyzeException, LexicalAnalyzeException
from all_in_one.gui_functions import insert_to_buffer, populate_list_store
from syntax_analyzer.refactored_syntax_analazer import analyze as generate_syntax_tree
from lexical_analyzer.lexical_analyzer import to_list, analyze_word
from lexical_analyzer.tokens.token import TokenType


class KeyWithType:
    def __init__(self, key, token_type):
        self.key = key
        self.token_type = token_type


def on_start_clicked(self, source_buffer, message_buffer, result_buffer, digit_list_store, identifier_list_store,
                     special_list_store):
    try:
        message_buffer.delete(message_buffer.get_start_iter(), message_buffer.get_end_iter())
        transliterate(source_buffer, message_buffer)
        token_list = lexical_analyze(source_buffer, message_buffer, digit_list_store, identifier_list_store,
                                     special_list_store)
        syntax_analyze(source_buffer, message_buffer, token_list)
    except AnalyzeException as e:
        insert_to_buffer(message_buffer, "%s: %s" % (e.__class__.__name__, e.args[0]))


def transliterate(input_buffer, output_buffer):
    insert_to_buffer(output_buffer, 'Transliteration started:')
    source = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    for symbol in source:
        token = transliterate_symbol(symbol)
        insert_to_buffer(output_buffer, token.to_string())
    insert_to_buffer(output_buffer, 'Transliteration finished.')


def lexical_analyze(input_buffer, output_buffer, digit_list_store, identifier_list_store, special_list_store):
    insert_to_buffer(output_buffer, 'Lexical analyze started:')
    input_string = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    digit_dict = {}
    identifier_dict = {}
    special_dict = {}
    token_list = []
    try:
        for word in to_list(input_string):
            token = analyze_word(word)
            key = token.word
            value = token.word
            if token.token_type == TokenType.FIRST:
                digit_dict[key] = value
            elif token.token_type == TokenType.SECOND:
                identifier_dict[key] = value
            else:
                special_dict[key] = value
            token_list.append(KeyWithType(key, token.token_type))
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
    print(digit_dict)
    print(identifier_dict)
    print(special_dict)
    print(token_list)
    populate_list_store(digit_list_store, digit_dict)
    populate_list_store(identifier_list_store, identifier_dict)
    populate_list_store(special_list_store, special_dict)
    insert_to_buffer(output_buffer, 'Lexical analyze finished.')
    return token_list


def syntax_analyze(input_buffer, output_buffer, token_list):
    insert_to_buffer(output_buffer, 'Syntax analyze started:')
    root_node = generate_syntax_tree(iter(token_list))
    insert_to_buffer(output_buffer, root_node.to_string())
    insert_to_buffer(output_buffer, 'Syntax analyze finished:')
