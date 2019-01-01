import time
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from src.syntax_analyzer.syntax_analyzer import SyntaxAnalyzer


def on_start_clicked(self, input_buffer, output_buffer):
    output_buffer.delete(output_buffer.get_start_iter(), output_buffer.get_end_iter())
    input_string = input_buffer.get_text(input_buffer.get_start_iter(), input_buffer.get_end_iter(), False)
    output_buffer.insert_at_cursor('Analyze started:\n')
    try:
        root_node = SyntaxAnalyzer(input_string).analyze()
        result_mes = root_node.to_string()
        popup_window = Gtk.Window(title='Синтаксическое дерево', resizable=False)
        drawing_area = Gtk.DrawingArea()
        drawing_area.connect("draw", on_draw, root_node)
        popup_window.add(drawing_area)
        popup_window.show_all()
    except Exception as e:
        result_mes = e.args[0]

    output_buffer.insert_at_cursor('[%s] %s\n' % (str(time.time()), result_mes))


def on_draw(wid, cr, root_node):
    cr.set_line_width(0.5)
    draw_node_name(root_node, cr, 50, 50, 1)


def draw_node_name(node, cr, x, y, level):
    cr.move_to(x, y)
    cr.show_text(node.name)
    print(node.name, x, y)
    width_space = 40
    height_space = 20
    if node.left:
        if node.middle:
            draw_node_name(node.left, cr, x - width_space / level, y + height_space - 1, level + 2)
            cr.move_to(x, y)
            cr.line_to(x - width_space / level, y + height_space - 7)
            cr.stroke()
        else:
            draw_node_name(node.left, cr, x, y + height_space, level + 2)
            cr.move_to(x, y)
            cr.line_to(x, y + height_space - 7)
            cr.stroke()
    if node.middle:
        draw_node_name(node.middle, cr, x, y + height_space, level + 2)
        cr.move_to(x, y)
        cr.line_to(x, y + height_space - 7)
        cr.stroke()
    if node.right:
        draw_node_name(node.right, cr, x + width_space / level, y + height_space, level + 2)
        cr.move_to(x, y)
        cr.line_to(x + width_space / level, y + height_space - 7)
        cr.stroke()
