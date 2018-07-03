from src.transliterator.transliterator import transliterate_symbol


def on_start(source_text, messages_var):
    source = source_text.get('1.0', 'end')[:-1]  # [:-1] is removing last '\n' added from Text class
    messages = []
    for symbol in source:
        token = transliterate_symbol(symbol)
        messages.append(token.to_string())
    messages_var.set(messages)