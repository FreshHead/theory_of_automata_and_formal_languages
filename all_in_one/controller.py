import gi

gi.require_version('Gtk', '3.0')

from transliterator.transliterator import transliterate_symbol
from all_in_one.custom_exceptions import AnalyzeException, LexicalAnalyzeException
from all_in_one.gui_functions import insert_to_buffer, populate_list_store
from syntax_analyzer.refactored_syntax_analazer import analyze as generate_syntax_tree, check_for_duplicates
from lexical_analyzer.lexical_analyzer import to_list, analyze_word
from lexical_analyzer.tokens.token import TokenType


class Model:
    def __init__(self, token_list, digit_dict, identifier_dict, special_dict):
        self.token_list = token_list
        self.digit_dict = digit_dict
        self.identifier_dict = identifier_dict
        self.special_dict = special_dict


class KeyWithType:
    def __init__(self, key, token_type):
        self.key = key
        self.token_type = token_type


def on_start_clicked(self, source_buffer, message_buffer, result_buffer, digit_list_store, identifier_list_store,
                     special_list_store, syntax_tree):
    try:
        syntax_tree.get_model().clear()
        digit_list_store.clear()
        identifier_list_store.clear()
        special_list_store.clear()
        message_buffer.delete(message_buffer.get_start_iter(), message_buffer.get_end_iter())
        result_buffer.delete(result_buffer.get_start_iter(), result_buffer.get_end_iter())

        transliterate(source_buffer, message_buffer)
        model = lexical_analyze(source_buffer, message_buffer, digit_list_store, identifier_list_store,
                                special_list_store)
        syntax_analyze(message_buffer, model, syntax_tree, source_buffer, model.identifier_dict)
        generate(model, source_buffer, message_buffer, result_buffer)
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
            elif token.token_type == TokenType.SPECIAL:
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
    populate_list_store(digit_list_store, digit_dict)
    populate_list_store(identifier_list_store, identifier_dict)
    populate_list_store(special_list_store, special_dict)
    insert_to_buffer(output_buffer, 'Lexical analyze finished.')
    return Model(token_list, digit_dict, identifier_dict, special_dict)


def syntax_analyze(output_buffer, model, syntax_tree, input_buffer, identifier_dict):
    insert_to_buffer(output_buffer, 'Syntax analyze started:')
    source = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    check_for_duplicates(source, identifier_dict)
    root_node = generate_syntax_tree(iter(model.token_list))

    populate_tree_store(syntax_tree.get_model(), root_node, None)
    syntax_tree.expand_all()
    insert_to_buffer(output_buffer, 'Syntax analyze finished:')


def populate_tree_store(tree_store, node, parent_node):
    tree_iter_node = tree_store.append(parent_node, [node.name])
    if node.left:
        populate_tree_store(tree_store, node.left, tree_iter_node)
    if node.middle:
        populate_tree_store(tree_store, node.middle, tree_iter_node)
    if node.right:
        populate_tree_store(tree_store, node.right, tree_iter_node)


def generate(model, input_buffer,message_buffer, result_buffer):
    insert_to_buffer(message_buffer, "Generation started.")
    source_string = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    digit_list = list(model.digit_dict.values())
    result_string = source_string
    for digit in digit_list:
        result_string = result_string.replace(digit, str(int(digit, 2)))
    identifier_list = list(model.identifier_dict.values())
    for identifier in identifier_list:
        result_string = result_string.replace(" " + identifier, " \n" + identifier)
    result_buffer.insert(result_buffer.get_end_iter(), result_string)
    insert_to_buffer(message_buffer, "Generation finished")
