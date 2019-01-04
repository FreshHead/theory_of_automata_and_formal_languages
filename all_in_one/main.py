import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from all_in_one.gui_functions import create_table

window = Gtk.Window(title='Теория формальных граматик и автоматов', resizable=False)
window.connect('delete-event', Gtk.main_quit)

source_label = Gtk.Label('Исходный текст:')
source_text_view = Gtk.TextView()
source_text_view.set_size_request(500, 100)

message_label = Gtk.Label('Сообщения:')
message_text_view = Gtk.TextView(editable=False)
message_text_view.set_size_request(500, 200)

output_label = Gtk.Label("Структурированный вывод:")
output_text_view = Gtk.TextView(editable=False)
output_text_view.set_size_request(500, 200)

digit_list_store = Gtk.ListStore(str, str)
digit_box = create_table("Таблица чисел:", digit_list_store)

identifier_list_store = Gtk.ListStore(str, str)
identifier_box = create_table("Таблица идентификаторов:", identifier_list_store)

special_list_store = Gtk.ListStore(str, str)
special_box = create_table("Таблица спец. символов:", special_list_store)

tree_label = Gtk.Label("Синтаксическое дерево:")
tree_table = Gtk.TreeView()

start_button = Gtk.Button('Запуск!')

# placement
v_box_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
v_box_left.add(source_label)
v_box_left.add(source_text_view)
v_box_left.add(message_label)
v_box_left.add(message_text_view)
v_box_left.add(output_label)
v_box_left.add(output_text_view)

v_box_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
table_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
table_box.add(digit_box)
table_box.add(identifier_box)
table_box.add(special_box)
v_box_right.add(table_box)
v_box_right.add(tree_label)
v_box_right.add(tree_table)

h_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
h_box.add(v_box_left)
h_box.add(v_box_right)
h_box.add(start_button)

window.add(h_box)

window.show_all()
Gtk.main()
