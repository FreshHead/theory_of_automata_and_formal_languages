import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from src.syntax_analyzer.syntax_analyzer import SyntaxAnalyzer


def on_start_clicked(self, input_buffer, output_buffer):
    output_buffer.delete(output_buffer.get_start_iter(), output_buffer.get_end_iter()) # clear buffer
    input_string = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    output_buffer.insert_at_cursor('Analyze started:\n')
    error_mes = SyntaxAnalyzer(input_string).analyze()
    output_buffer.insert_at_cursor('[%s] %s\n' % (str(time.time()), error_mes))
    # TODO: Нарисовать экранчик с синтаксическим деревом
    window2 = Gtk.Window(title='Синтаксическое дерево', resizable=False)
    window2.show_all()



