# from os import getcwd
from tkinter import Tk, IntVar, StringVar, Frame, Label, Entry, Button, Menu
from tkinter.ttk import Combobox, Style
from tkinter import messagebox as MessageBox
import resources.operations as operation

program_name = 'MASCrypt'
programa_description = 'Modular Arithmetic Software for Cryptography'
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

    print(f'base.get() = {base.get()}')


def set_operation(event):
    print(f'cb_operation.get() = {cb_operation.get()}')

    if cb_operation.current() == 2:
        label3.grid(row=2, column=0, padx=padx, pady=pady, sticky='e')
        entry3.grid(row=2, column=1, padx=padx, pady=pady, sticky='we')
    else:
        label3.grid_remove()
        entry3.grid_remove()


def calculate():
    items_with_error = []

    if cb_base.current() == 0:
        items_with_error.append('Base')

    if cb_operation.current() == 0:
        items_with_error.append('Operation')

    if len(items_with_error) != 0:
        MessageBox.showerror(
            title=f'Missing information:',
            message=f'You have to select the following items from combo boxes:\
            \n\n{", ".join(items_with_error)}'
        )
        return

    op = cb_operation.get()

    if op == cb_operation_op_addition:
        operation.addition(res, base, op1, op2)
    elif op == cb_operation_op_addition_module:
        operation.addition(res, base, op1, op2, op3)
    elif op == cb_operation_op_substraction:
        operation.substraction(res, base, op1, op2)
    elif op == cb_operation_op_multiplication:
        operation.multiplication(res, base, op1, op2)
    elif op == cb_operation_op_division:
        operation.division(res, base, op1, op2)


def about():
    MessageBox.showinfo(f'About {program_name}', f'{programa_description}')


root = Tk()
# root.geometry('650x250')
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

frame1 = Frame(root, cursor='arrow', bg='#00ff00', bd=5)
frame1.pack(expand=True, fill='x')

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

cb_operation_op_default = '-- Select operation --'
cb_operation_op_addition = 'Addition'
cb_operation_op_addition_module = 'Addition module'
cb_operation_op_substraction = 'Substraction'
cb_operation_op_multiplication = 'Multiplication'
cb_operation_op_division = 'Division'

cb_operation = Combobox(frame1, state='readonly')
cb_operation['values'] = [
    cb_operation_op_default,
    cb_operation_op_addition,
    cb_operation_op_addition_module,
    cb_operation_op_substraction,
    cb_operation_op_multiplication,
    cb_operation_op_division,
]
cb_operation.current(0)
cb_operation.bind('<<ComboboxSelected>>', set_operation)
cb_operation.grid(row=0, column=1, padx=padx, pady=pady, sticky='w')


frame2 = Frame(root, cursor='arrow', bg='#ff0000', bd=5)
frame2.pack(expand=True, fill='x')
frame2.grid_columnconfigure(1, weight=1)

op1 = StringVar()
op2 = StringVar()
op3 = StringVar()
res = StringVar()

label1 = Label(frame2, text='First number')
label1.grid(row=0, column=0, padx=padx, pady=pady, sticky='e')
entry1 = Entry(frame2, font=font, textvariable=op1)
entry1.grid(row=0, column=1, padx=padx, pady=pady, sticky='we')

label2 = Label(frame2, text='Second number')
label2.grid(row=1, column=0, padx=padx, pady=pady, sticky='e')
entry2 = Entry(frame2, font=font, textvariable=op2)
entry2.grid(row=1, column=1, padx=padx, pady=pady, sticky='we')

label3 = Label(frame2, text='Module')
entry3 = Entry(frame2, font=font, textvariable=op3)

label_res = Label(frame2, text='Result')
label_res.grid(row=3, column=0, padx=padx, pady=pady, sticky='e')
entry_res = Entry(frame2, font=font, textvariable=res,
                  state='readonly', readonlybackground='white')
entry_res.grid(row=3, column=1, padx=padx, pady=pady, sticky='we')

button = Button(frame2, text='Calulate', command=calculate)
button.grid(row=4, column=1, padx=padx, pady=pady, sticky='w')

root.mainloop()
