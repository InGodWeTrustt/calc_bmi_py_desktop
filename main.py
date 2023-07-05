import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import config as cfg

# Очистить поля ввода данных
def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

def update_entry_value(entry, new_value=''):
    entry.delete(0, tk.END)
    entry.insert(0, new_value)

def fill_from_file():
    path = filedialog.askopenfilename()
    # Если файл не выбран или он не текстового формата, завершить выполнение функции
    if path == '' or not path.endswith('.txt'): return 
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            name, value = line.strip().split(' ')
            if name == 'Вес':
                update_entry_value(weight_entry, value)
            else:
                update_entry_value(height_entry, value)
                 
def calc_bmi():
    try:
        kg = float(weight_entry.get())
        m = int(height_entry.get()) / 100
        if kg <=0 or m <= 0:
            raise ValueError('Вес и рост должны быть больше нуля')
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
            messagebox.showerror('Ошибка', str(e))
        
root = tk.Tk()
root.geometry(cfg.app_size)
root.title(cfg.app_title) 
root.config(bg="#9ec9cf")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


frame = tk.Frame(
    root, 
    bg=cfg.main_bg_color, 
    padx=20, 
    pady=20,
    borderwidth=1,
    relief="solid"
)
frame.grid(column=0, row=0)

height_lbl = tk.Label(frame, text='Введите ваш рост в см',font=('Arial Bold', 10), bg=cfg.main_bg_color, fg="white")
height_lbl.grid(row=3, column=2, sticky='W')
height_entry = tk.Entry(frame)
height_entry.grid(row=3, column=3, columnspan=2)

weight_lbl = tk.Label(frame, text='Введите ваш вес в кг',font=('Arial Bold', 10), fg="white", bg=cfg.main_bg_color).grid(row=4, column=2, sticky='W')
weight_entry = tk.Entry(frame)
weight_entry.grid(row=4, column=3, columnspan=2)

calc_btn = tk.Button(frame,text='Рассчитать ИМТ',command=calc_bmi)
calc_btn.grid(row=5, column=4)
clearfields_btn = tk.Button(frame, text="Очистить поля",command=clear_fields).grid(row=5, column=3)
opendialog_btn = tk.Button(frame, text="Заполнить из файла",command=fill_from_file).grid(row=5, column=2, sticky='W')

original_color_btn = calc_btn.cget('bg')

for child in frame.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
    if isinstance(child, tk.Button):
        # <Enter> - при переходе курсора мыши на элемент мы меняем цвет фона на красный, а цвет текста на белый
        # <Leave> - когда курсор мыши покидает данный элеменьт мы меняем все на исходные значения
        # навешиваю обработчики события на каждую кнопку
        child.bind('<Enter>', lambda event : event.widget.config(bg="blue", fg="white"))
        child.bind('<Leave>', lambda event : event.widget.config(bg=original_color_btn, fg="black"))

# calc_bmi будет вызываться каждый раз, когда пользователь нажимает кнопку enter в полях ввода
height_entry.bind('<Return>', lambda x: calc_bmi())
weight_entry.bind('<Return>', lambda x: calc_bmi())

root.mainloop()