import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from all_in_one.gui_functions import create_table
from all_in_one.controller import on_start_clicked

window = Gtk.Window(title='Теория формальных граматик и автоматов', resizable=False)
window.connect('delete-event', Gtk.main_quit)

source_label = Gtk.Label('Исходный текст:')
source_text_view = Gtk.TextView()
source_window = Gtk.ScrolledWindow()
source_window.set_size_request(500, 100)
source_window.add(source_text_view)

message_label = Gtk.Label('Сообщения:')
message_text_view = Gtk.TextView(editable=False)
message_window = Gtk.ScrolledWindow()
message_window.set_size_request(500, 200)
message_window.add(message_text_view)

result_label = Gtk.Label("Структурированный вывод:")
result_text_view = Gtk.TextView(editable=False)
result_window = Gtk.ScrolledWindow()
result_window.set_size_request(500, 200)
result_window.add(result_text_view)

digit_list_store = Gtk.ListStore(str, str)
digit_box = create_table("Таблица чисел:", digit_list_store)

identifier_list_store = Gtk.ListStore(str, str)
identifier_box = create_table("Таблица идентификаторов:", identifier_list_store)

special_list_store = Gtk.ListStore(str, str)
special_box = create_table("Таблица спец. символов:", special_list_store)

tree_store = Gtk.TreeStore(str)
syntax_tree = Gtk.TreeView(tree_store)

tree_column = Gtk.TreeViewColumn('Синтаксическое дерево:')
syntax_tree.append_column(tree_column)

cell = Gtk.CellRendererText()
tree_column.pack_start(cell, True)
tree_column.add_attribute(cell, 'text', 0)

start_button = Gtk.Button('Запуск!')

start_button.connect('clicked', on_start_clicked, source_text_view.get_buffer(), message_text_view.get_buffer(),
                     result_text_view.get_buffer(), digit_list_store, identifier_list_store, special_list_store,
                     syntax_tree)

# placement
v_box_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
v_box_left.add(source_label)
v_box_left.add(source_window)
v_box_left.add(message_label)
v_box_left.add(message_window)
v_box_left.add(result_label)
v_box_left.add(result_window)

v_box_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
table_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
table_box.add(digit_box)
table_box.add(identifier_box)
table_box.add(special_box)
v_box_right.add(table_box)
v_box_right.add(syntax_tree)

h_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
h_box.add(v_box_left)
h_box.add(v_box_right)
h_box.add(start_button)

window.add(h_box)

window.show_all()
Gtk.main()
