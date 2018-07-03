from tkinter import *
from tkinter import ttk
from functools import partial

from src.transliterator.gui.controller import on_start

root = Tk()
root.title("Транслитератор")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Source
source_text = Text(mainframe, width=40, height=10)
source_text.grid(column=1, row=2, sticky=(W, E))

# Source scrollbar
source_scrollbar = ttk.Scrollbar(mainframe, orient=VERTICAL, command=source_text.yview)
source_scrollbar.grid(column=2, row=2, sticky=(N, S))
source_text.configure(yscrollcommand=source_scrollbar.set)

# Message
messages_var = StringVar()

message_listbox = Listbox(mainframe, width=40, height=10, listvariable=messages_var)
message_listbox.grid(column=1, row=4, sticky=(W, E))

# Message scrollbar
message_scrollbar = ttk.Scrollbar(mainframe, orient=VERTICAL, command=message_listbox.yview)
message_scrollbar.grid(column=2, row=4, sticky=(N, S))
message_listbox.configure(yscrollcommand=message_scrollbar.set)

# Labels
ttk.Label(mainframe, text="Текст:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Сообщение:").grid(column=1, row=3, sticky=W)

func_with_args = partial(on_start, source_text, messages_var)

ttk.Button(mainframe, text="Запуск", command=func_with_args).grid(column=1, row=5, sticky=E)

# Padding
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

source_text.focus()

root.mainloop()
