from src.transliterator.transliterator import transliterate_symbol
from src.gui.view import main


def on_start(source_text, message_listbox):
    source = source_text.get('1.0', 'end')[:-1]  # [:-1] is removing last '\n' added from Text class
    for symbol in source:
        token = transliterate_symbol(symbol)
        message_listbox.insert(len(message_listbox.children), token.to_string())


main('Транслитератор', on_start)