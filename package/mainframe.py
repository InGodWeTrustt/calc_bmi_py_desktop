import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import package.config as cfg
from package.opt_menu import Option as OptionMenu

class MainFrame(tk.Frame):
    def __init__(self, container,*args, **kw):
        super().__init__(container, *args, **kw)
        self.grid(column=0, row=0)
        self.create_widgets()
        self.create_option_menu()
        self.events()
        self.original_color_btn = self.calc_btn.cget('bg')

    def create_widgets(self):
        # Отображение метки "Введите ваш рост"
        self.height_lbl = tk.Label(self, text='Введите ваш рост',font=('Arial Bold', 10),bg=cfg.MAIN_BG_COLOR, fg="white")
        self.height_lbl.grid(row=3, column=2, sticky='W')
        
        # Поле для ввода роста
        self.height_entry = tk.Entry(self)
        self.height_entry.grid(row=3, column=3, columnspan=2)

        self.weight_lbl = tk.Label(self, text='Введите ваш вес',font=('Arial Bold', 10), fg="white", bg=cfg.MAIN_BG_COLOR).grid(row=4, column=2, sticky='W')
        
        # Поле для ввода веса
        self.weight_entry = tk.Entry(self)
        
        # Размещение элемента
        self.weight_entry.grid(row=4, column=3, columnspan=2)
        
        # Метка с надписью "кг"
        self.weight_lbl_units = tk.Label(self, text="кг").grid(row=4, column=6)

        self.calc_btn = tk.Button(self,text='Рассчитать ИМТ',command=self.calc_bmi)
        self.calc_btn.grid(row=5, column=4)
        self.clearfields_btn = tk.Button(self, text="Очистить поля",command=lambda event=None: self.clear_fields(event), state=tk.DISABLED)
        self.clearfields_btn.grid(row=5, column=3)
        self.opendialog_btn = tk.Button(self, text="Заполнить из файла",command=self.fill_from_file).grid(row=5, column=2, sticky='W')

        self.load_data()

    def events(self):
        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
            if isinstance(child, tk.Button):
                # <Enter> - при переходе курсора мыши на элемент мы меняем цвет фона на красный, а цвет текста на белый
                # <Leave> - когда курсор мыши покидает данный элеменьт мы меняем все на исходные значения
                # навешиваю обработчики события на каждую кнопку
                child.bind('<Enter>', self.hover_in)
                child.bind('<Leave>', self.hover_out)

        # calc_bmi будет вызываться каждый раз, когда пользователь нажимает кнопку enter в полях ввода
        self.height_entry.bind('<Return>', lambda x: self.calc_bmi())
        self.weight_entry.bind('<Return>', lambda x: self.calc_bmi())

        self.height_entry.bind('<KeyRelease>', self.check_entry_fields)
        self.weight_entry.bind('<KeyRelease>', self.check_entry_fields)
    
    def create_option_menu(self):
        self.option_menu = OptionMenu(self)

    def calc_bmi(self):
        try:
            kg = float(self.weight_entry.get())
            m = float(self.height_entry.get())
        
            if kg <=0 or m <= 0:
                raise ValueError('Вес и рост должны быть больше нуля')
            
            cur_opt = self.option_menu.current
            m = m if cur_opt == 'м' else m / 100

            bmi = kg/(m*m)
            bmi = round(bmi, 1)
            
            if bmi < 18.5:
                messagebox.showinfo('Итог', f'ИМТ = {bmi} соответствует недостаточному весу')
            elif (bmi > 18.5) and (bmi < 24.9):
                messagebox.showinfo('Итог', f'ИМТ = {bmi} соответствует нормальному весу')
            elif (bmi > 24.9) and (bmi < 29.9):
                messagebox.showinfo('Итог', f'ИМТ = {bmi} соответствует избыточному весу')
            else:
                messagebox.showinfo('Итог', f'ИМТ = {bmi} соответствует ожирению') 
        except ValueError as e:
                messagebox.showerror(title='Ошибка', message=str(e))

    def fill_from_file(self):
        """ Заполнить поля ввода данных из текстового файла """
        
        path = filedialog.askopenfilename()
        # Если файл не выбран или он не текстового формата, завершить выполнение функции
        if path == '' or not path.endswith('.txt'): return 
        
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                name, value = line.strip().split(' ')
                if name == 'Вес':
                    self.update_entry_value(self.weight_entry, value)
                else:
                    self.update_entry_value(self.height_entry, value)
    
    def check_entry_fields(self,event):
        if self.height_entry.get() or self.weight_entry.get():
            self.clearfields_btn.config(state=tk.NORMAL)

    def hover_in(self,event):
        if event.widget['state'] != 'disabled':
            event.widget.config(bg="blue", fg="white")

    def hover_out(self,event):
        if event.widget['state'] != 'disabled':
            event.widget.config(bg=self.original_color_btn, fg="black")

    def clear_fields(self,event):
        """ Очистить поля ввода данных """
        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.clearfields_btn.config(state=tk.DISABLED, bg=self.original_color_btn, fg="black")

    def update_entry_value(self,entry, new_value=''):
        entry.delete(0, tk.END)
        entry.insert(0, new_value)

    def save_data(self):
        weight_entry = self.weight_entry.get()
        height_entry = self.height_entry.get()

        try:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS measurements (id INTEGER, weight REAL, height REAL)")
            c.execute('SELECT COUNT(*) FROM measurements')
            result = c.fetchone()

            if result[0] > 0:
                 c.execute("UPDATE measurements SET weight = ?, height = ? WHERE id = 1", (weight_entry, height_entry))
            else:
                c.execute("INSERT INTO measurements VALUES (?, ?, ?)", (1, weight_entry, height_entry))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Error", str(e))
    
    def load_data(self):
        try:
            conn = sqlite3.connect("data.db")
            c = conn.cursor()
            c.execute("SELECT * FROM measurements")
            data = c.fetchone()
            conn.close()

            if data:
                id, weight, height = data
                self.weight_entry.insert(0, weight)
                self.height_entry.insert(0, height)
        except sqlite3.Error as e:
            pass
            # messagebox.showerror("Error", str(e))