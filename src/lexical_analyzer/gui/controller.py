from src.lexical_analyzer.lexical_analyzer import to_list, analyze
import time


def on_start_clicked(self, input_buffer, output_buffer):
    input_string = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    output_buffer.insert_at_cursor('Analyze started:\n')
    tokens = analyze(input_string)
    for token in tokens:
        token_message = 'Token: ' + token.word + ' of type: ' + token.type.name
        if token.error:
            token_message += ' has error: ' + token.error + ' \nAnalyze was stopped!'
            spaced_string = ' ' + input_string + ' '
            selection_start = spaced_string.find(' ' + token.word + ' ')
            selection_end = selection_start
            while spaced_string[selection_end + 1] != ' ':
                selection_end += 1
            start_iter = input_buffer.get_iter_at_offset(selection_start)
            end_iter = input_buffer.get_iter_at_offset(selection_end)
            input_buffer.select_range(start_iter, end_iter)
        output_buffer.insert_at_cursor('[%s] %s\n' % (str(time.time()), token_message))




