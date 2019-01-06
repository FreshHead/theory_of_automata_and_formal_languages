import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from datetime import datetime


def create_table(name, list_store):
    label = Gtk.Label(name)
    tree_view = Gtk.TreeView(list_store)

    for i, col_title in enumerate(["Код", "Слово"]):
        tree_view.append_column(Gtk.TreeViewColumn(col_title, Gtk.CellRendererText(), text=i))

    # placement
    v_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    v_box.add(label)
    v_box.add(tree_view)
    return v_box


def insert_to_buffer(buffer, message):
    timestamp = datetime.now().strftime("%H:%M:%S.%f")
    buffer.insert(buffer.get_end_iter(), '[%s] %s\n' % (timestamp, message))


def populate_list_store(list_store, dictionary):
    for key in dictionary.keys():
        list_store.append((str(hash(key)), dictionary[key]))
