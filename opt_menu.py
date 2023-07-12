import tkinter as tk
from tkinter import ttk

class Option():
    def __init__(self, root):
        self._current_option = tk.StringVar()
        self.units = ('см', 'м')
        self.master = root
        self.create_opt_widjet()
    
    def create_opt_widjet(self):
        opt_menu = ttk.OptionMenu(
            self.master, 
            self._current_option, 
            self.units[0], 
            *self.units,
        )
        opt_menu.grid(row=3, column=6)

    @property
    def current(self):
        return self._current_option.get()