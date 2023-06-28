import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

# Очистить поля ввода данных
def clear_fields():
    update_entry_value(weight_entry)
    update_entry_value(height_entry)

def update_entry_value(entry, new_value=''):
    entry.delete(0, END)
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
        kg = int(weight_entry.get())
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
            messagebox.showerror('Ошибка ввода данных', str(e))

window = Tk()
# ширина и высота в пикселях
window.geometry('400x400')
# название окна
window.title('Расчет ИМТ')

frame = Frame(
    window, 
    padx=10,  # задаем отступ по горизонтали
    pady=10   # задаем отступ по вертикали
)

frame.pack(expand=True)

height_lbl = Label(
    frame, 
    text='Введите ваш рост в см',
    font=('Arial Bold', 10)
)
# установим позицию элемента в окне
height_lbl.grid(row=3, column=2)

height_entry = Entry(
    frame,
)
height_entry.grid(row=3, column=3)

weight_lbl = Label(
    frame, 
    text='Введите ваш вес в кг',
    font=('Arial Bold', 10)
)
weight_lbl.grid(row=4, column=2)

weight_entry = Entry(
    frame,
)
weight_entry.grid(row=4, column=3)

calc_btn = Button(
    frame,
    text='Рассчитать ИМТ',
    command=calc_bmi
)

calc_btn.grid(row=5, column=3)

# диалоговое окно
opendialog_btn = Button(
   frame, 
   text="Заполнить из текстового файла",
   command=fill_from_file
)

opendialog_btn.grid(row=5, column=2)

# диалоговое окно
clearfields_btn = Button(
   frame, 
   text="Очистить поля ввода данных",
   command=clear_fields
)

clearfields_btn.grid(row=6, column=2)

window.mainloop()