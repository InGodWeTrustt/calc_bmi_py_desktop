import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class App(tk.Tk):
    def __init__(self, window_size, icon_img, title="Расчет ИМТ"):
        super().__init__()
        self.window_size = window_size
        self.title = title
        self.config(bg="#9ec9cf")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.center_window()
        # self.change_icon(icon_img)

    def center_window(self):
        """ Отцентрировать окно приложения """
        
        # Получить ширину и высоту экрана
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Высчитать  x и y координаты центра окна приложения
        width, height = self.window_size.split('x')
        x = (screen_width - int(width)) // 2
        y = (screen_height - int(height)) // 2

        self.geometry(f"{self.window_size}+{x}+{y}")

    def change_icon(self, file):
        """ Изменить иконку приложения """
        icon = tk.PhotoImage(file)
        self.iconphoto(False, file)

    def close_window(self):
        """ Выход из основного приложения"""
        quit = messagebox.askyesno('Выход из приложения', message="Вы действительно хотите выйти из приложения?")
        if quit:
            self.destroy()
