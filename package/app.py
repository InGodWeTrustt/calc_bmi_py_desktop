import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class App(tk.Tk):
    def __init__(self,*args,  **kwargs):
        super().__init__()
        self.window_size = kwargs.get('window_size', '400x400')

        # Устанавливаем заголовок окна из словапа по ключу "title". 
        # При его отстуствии  cтавим дефолтное значение (2 аргумент)
        self.title(kwargs.get('title', 'Расчет ИМТ'))
        self.config(bg="#9ec9cf")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # При закрытии окна будет срабатывать функция обратного вызова - self.closse_window
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.bind('<Escape>', lambda e: self.close_window(e))
        self.center_window()
        self._main_frame=None

    @property
    def main_frame(self, frame):
        return self_main_frame

    @main_frame.setter
    def main_frame(self, frame):
        self._main_frame = frame

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

    def set_icon(self, file):
        """ Изменить иконку приложения """
        icon = tk.PhotoImage(file=file)
        self.iconphoto(False, icon)

    def close_window(self, e):
        """ Выход из основного приложения"""
        quit = messagebox.askyesno('Выход из приложения', message="Вы действительно хотите выйти из приложения?")
        if quit:
            self._main_frame.save_data()
            self.destroy()
