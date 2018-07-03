from src.lexical_analyzer.lexical_analyzer import to_list, analyze
from src.gui.view import main


def on_start(source_text, messages_var):
    source_string = source_text.get('1.0', 'end')[:-1]  # [:-1] is removing last '\n' added from Text class
    tokens = analyze(source_string)
    messages = []
    source_text.tag_remove(0.0, 'end')
    for token in tokens:
        messages.append(token.to_string())
    messages_var.set(messages)


main('Лексический анализатор', on_start)
