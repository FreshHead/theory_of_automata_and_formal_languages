from src.lexical_analyzer.lexical_analyzer import analyze
import time


def on_start_clicked(self, input_buffer, output_buffer):
    input_string = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    output_buffer.insert_at_cursor("Analyze started:\n")
    result = analyze(input_string)
    for word_result in result:
        output_buffer.insert_at_cursor("[%s] %s\n" % (str(time.time()), word_result))
        if word_result.find("Error") != -1:
            # selection_start = word_result.find("Type of ") + len("Type of ")
            # selection_end = word_result.find("is: ") - 1
            # start_iter = input_buffer.get_iter_at_offset(selection_start)
            # end_iter = input_buffer.get_iter_at_offset(selection_end)
            # input_buffer.select_range(start_iter, end_iter)
            output_buffer.insert_at_cursor("[%s] %s\n" % (str(time.time()), "Analyzing was stopped due to previous error!"))
            return 1
