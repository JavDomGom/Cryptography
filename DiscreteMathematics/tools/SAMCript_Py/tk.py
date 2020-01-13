from os import getcwd
from tkinter import *


def addition():
    import resources.LogicalAddition as la
    res.set(la.LogicalAddition(2).integerAddition(op1.get(), op2.get()))


def substraction():
    import resources.LogicalSubstraction as ls
    res.set(ls.LogicalSubstraction(2).integerSubtraction(op1.get(), op2.get()))


def multiplication():
    import resources.LogicalMultiplication as lm
    res.set(lm.LogicalMultiplication(2).integerMultiplication(op1.get(), op2.get()))


def division():
    import resources.LogicalDivision as ld
    res.set(ld.LogicalDivision(2).integerDivision(op1.get(), op2.get()))


def header_msg():
    header.config(text=f'Calculations in base {base.get()}')


padx = 3
pady = 3
font = ('Courier New', 10)

root = Tk()
root.title('SAMCript_py - Software de Aritmética Modular para Criptografía')
root.resizable(0,0)
# root.iconbitmap(f'@{getcwd()}/img/icon.xbm')

frame1 = Frame(root)
frame1.pack(fill='both', expand=1)
frame1.config(cursor='arrow', bg='CadetBlue1', bd=5)

header = Label(frame1)
header.grid(row=1)

frame2 = Frame(root)
frame2.pack(fill='both', expand=1)
frame2.config(cursor='arrow', bd=5)

op1 = StringVar()
op2 = StringVar()
res = StringVar()

label1 = Label(frame2, text='First number')
label1.grid(row=0, column=0, padx=padx, pady=pady, sticky='e')
entry1 = Entry(frame2, font=font, textvariable=op1)
entry1.grid(row=0, column=1, padx=padx, pady=pady)

label2 = Label(frame2, text='Second number')
label2.grid(row=1, column=0, padx=padx, pady=pady, sticky='e')
entry2 = Entry(frame2, font=font, textvariable=op2)
entry2.grid(row=1, column=1, padx=padx, pady=pady)

label3 = Label(frame2, text='Result')
label3.grid(row=2, column=0, padx=padx, pady=pady, sticky='e')
entry3 = Entry(frame2, font=font, textvariable=res, state='readonly')
entry3.grid(row=2, column=1, padx=padx, pady=pady)

frame3 = Frame(root)
frame3.pack(fill='both', expand=1)
frame3.config(cursor='arrow', bg='bisque', bd=5)

base = IntVar()

rb1 = Radiobutton(frame3, variable=base, command=header_msg, value=2, text='Binary')
rb1.grid(row=0, column=0)
rb2 = Radiobutton(frame3, variable=base, command=header_msg, value=10, text='Decimal')
rb2.grid(row=0, column=1)
rb3 = Radiobutton(frame3, variable=base, command=header_msg, value=16, text='Hexadecimal')
rb3.grid(row=0, column=2)

frame4 = Frame(root)
frame4.pack(fill='both', expand=1)
frame4.config(cursor='arrow', bg='lightgreen', bd=5)

button1 = Button(frame4, text='Addition', command=addition)
button1.grid(row=0, column=0)
button2 = Button(frame4, text='Substraction', command=substraction)
button2.grid(row=0, column=1)
button3 = Button(frame4, text='Multiplication', command=multiplication)
button3.grid(row=0, column=2)
button4 = Button(frame4, text='Division', command=division)
button4.grid(row=0, column=3)

root.mainloop()
