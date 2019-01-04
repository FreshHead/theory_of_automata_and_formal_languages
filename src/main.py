import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from src.page import Page
from transliterator.gui.controller import on_start_clicked as on_transliterate_clicked
from lexical_analyzer.gui.controller import on_start_clicked as on_lex_analyzer_clicked
from syntax_analyzer.gui.controller import on_start_clicked as on_syn_analyzer_clicked

settings = Gtk.Settings.get_default()
settings.set_property("gtk-theme-name", "Raleigh")
# settings.set_property("gtk-application-prefer-dark-theme", True)  # if you want use dark theme, set second arg to True

window = Gtk.Window(title='Теория формальных граматик и автоматов', resizable=False)
window.connect('delete-event', Gtk.main_quit)

notebook = Gtk.Notebook()
notebook.append_page(Page(on_transliterate_clicked), Gtk.Label("Транслитератор"))
notebook.append_page(Page(on_lex_analyzer_clicked), Gtk.Label("Лехический анализатор"))
notebook.append_page(Page(on_syn_analyzer_clicked), Gtk.Label("Синтаксический анализатор"))

window.add(notebook)
window.show_all()
Gtk.main()
