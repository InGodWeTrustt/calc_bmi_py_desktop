import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# Очистить поля ввода данных
def clear_fields():
    weight_entry.delete(0, END)
    height_entry.delete(0, END)

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
            messagebox.showerror(str(e))

root = Tk()
root.geometry('500x500') # ширина и высота в пикселях
root.title('Расчет ИМТ') # название окна

frame = Frame(root).grid(column=0, row=0)

height_lbl = Label(frame, text='Введите ваш рост в см',font=('Arial Bold', 10)).grid(row=3, column=2)
height_entry = Entry(frame)
height_entry.grid(row=3, column=3, columnspan=2)

weight_lbl = Label(frame, text='Введите ваш вес в кг',font=('Arial Bold', 10)).grid(row=4, column=2)
weight_entry = Entry(frame)
weight_entry.grid(row=4, column=3, columnspan=2)

calc_btn = Button(frame,text='Рассчитать ИМТ',command=calc_bmi,bg="green",fg="white",cursor="dot").grid(row=5, column=4)
clearfields_btn = Button(frame, text="Очистить поля",command=clear_fields).grid(row=5, column=3)
opendialog_btn = Button(frame, text="Заполнить из файла",command=fill_from_file).grid(row=5, column=2)

root.mainloop()