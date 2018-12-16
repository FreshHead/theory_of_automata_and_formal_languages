import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Page(Gtk.VBox):
    def __init__(self, on_start_clicked):
        super().__init__()

        source_label = Gtk.Label('Текст:')

        source_text_view = Gtk.TextView()
        source_text_view.set_size_request(500, 200)

        message_label = Gtk.Label('Сообщения:')

        message_text_view = Gtk.TextView()
        message_text_view.set_size_request(500, 200)

        start_button = Gtk.Button('Запуск!')
        source_buffer = source_text_view.get_buffer()
        message_buffer = message_text_view.get_buffer()
        start_button.connect('clicked', on_start_clicked, source_buffer, message_buffer)

        # placement
        h_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        h_box.add(source_text_view)
        h_box.add(start_button)

        source_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        source_box.add(source_label)
        source_box.add(h_box)

        message_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        message_box.add(message_label)
        message_box.add(message_text_view)

        self.pack_start(source_box, False, False, 0)
        self.pack_start(message_box, False, False, 0)