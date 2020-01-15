# from os import getcwd
from tkinter import Tk, IntVar, StringVar, Frame, Label, Entry, Button, Menu
from tkinter.ttk import Combobox, Style
from tkinter import messagebox as MessageBox

program_name = 'SAMCript_py'
programa_description = 'Software de Aritmética Modular para Criptografía'
padx = 3
pady = 3
font = ('Courier New', 10)


def set_base(event):
    b = cb_base.get()

    if b == cb_base_op_base2:
        base.set(2)
    elif b == cb_base_op_base10:
        base.set(10)
    elif b == cb_base_op_base16:
        base.set(16)

    print(f'base = {base.get()}')


def set_operation(event):
    operation.set(cb_operation.get())
    print(f'operation = {operation.get()}')


def calculate():
    op = cb_operation.get()

    if op == cb_operation_op_addition:
        addition()
    elif op == cb_operation_op_substraction:
        substraction()
    elif op == cb_operation_op_multiplication:
        multiplication()
    elif op == cb_operation_op_division:
        division()


def addition():
    import resources.LogicalAddition as la
    res.set(
        la.LogicalAddition(base.get())
          .integerAddition(op1.get(), op2.get())
    )


def substraction():
    import resources.LogicalSubstraction as ls
    res.set(
        ls.LogicalSubstraction(base.get())
          .integerSubtraction(op1.get(), op2.get())
    )


def multiplication():
    import resources.LogicalMultiplication as lm
    res.set(
        lm.LogicalMultiplication(base.get())
          .integerMultiplication(op1.get(), op2.get())
    )


def division():
    import resources.LogicalDivision as ld
    res.set(
        ld.LogicalDivision(base.get())
          .integerDivision(op1.get(), op2.get())
    )


def about():
    MessageBox.showinfo(f'About {program_name}', f'{programa_description}')


root = Tk()
root.geometry('650x350')
root.title(f'{program_name} - {programa_description}')
root.resizable(1, 0)
# root.iconbitmap(f'@{getcwd()}/img/icon.xbm')

style = Style()
style.theme_create('custom_style',
                   parent='default',
                   settings={'TCombobox':
                             {'configure':
                              {'selectforeground': 'black',
                               'selectbackground': 'white'}
                              }
                             }
                   )
style.theme_use('custom_style')

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='New file')
filemenu.add_command(label='Open file')
filemenu.add_command(label='Save as')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='View terms of use')
helpmenu.add_command(label='View license')
helpmenu.add_command(label='Documentation')
helpmenu.add_separator()
helpmenu.add_command(label=f'About {program_name}', command=about)


menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Edit', menu=editmenu)
menubar.add_cascade(label='Help', menu=helpmenu)

frame1 = Frame(root)
frame1.pack(fill='both', expand=1)
frame1.config(cursor='arrow', bg='CadetBlue1', bd=5)

base = IntVar()

cb_base_op_default = '-- Select base --'
cb_base_op_base2 = 'Binary (Base-2)'
cb_base_op_base10 = 'Decimal (Base-10)'
cb_base_op_base16 = 'Hexadecimal (Base-16)'

cb_base = Combobox(frame1, state='readonly')
cb_base['values'] = [
    cb_base_op_default,
    cb_base_op_base2,
    cb_base_op_base10,
    cb_base_op_base16
]
cb_base.current(0)
cb_base.bind('<<ComboboxSelected>>', set_base)
cb_base.grid(row=0, column=0, padx=padx, pady=pady, sticky='w')

operation = StringVar()

cb_operation_op_default = '-- Select operation --'
cb_operation_op_addition = 'Addition'
cb_operation_op_substraction = 'Substraction'
cb_operation_op_multiplication = 'Multiplication'
cb_operation_op_division = 'Division'

cb_operation = Combobox(frame1, state='readonly')
cb_operation['values'] = [
    cb_operation_op_default,
    cb_operation_op_addition,
    cb_operation_op_substraction,
    cb_operation_op_multiplication,
    cb_operation_op_division,
]
cb_operation.current(0)
cb_operation.bind('<<ComboboxSelected>>', set_operation)
cb_operation.grid(row=0, column=1, padx=padx, pady=pady, sticky='w')


frame2 = Frame(root)
frame2.pack(fill='both', expand=1)
frame2.config(cursor='arrow', bd=5)

op1 = StringVar()
op2 = StringVar()
res = StringVar()

root.grid_columnconfigure(1, weight=0)

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

button = Button(frame2, text='Calulate', command=calculate)
button.grid(row=3, column=1, padx=padx, pady=pady, sticky='w')

root.mainloop()
