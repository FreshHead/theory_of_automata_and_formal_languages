import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


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
