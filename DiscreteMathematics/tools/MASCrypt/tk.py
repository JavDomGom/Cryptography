# from os import getcwd
from tkinter import Tk, IntVar, StringVar, Frame, Label, Entry, Button, Menu
from tkinter.ttk import Combobox, Style
from tkinter import messagebox as MessageBox
import resources.operations as operation

program_name = 'MASCrypt'
program_description = 'Modular Arithmetic Software for Cryptography'
padx = 3
pady = 3
font = ('Courier New', 10)
bg_color = '#C9C9C9'
fg_color = '#000000'


def clear_all_entries():
    ''' Empty all entries when combobox is modified.'''
    ops = [op1, op2, op3, y, module, res]
    for op in ops:
        op.set('')


def set_base(event):
    clear_all_entries()

    b = cb_base.get()

    if b == cb_base_op_base2:
        base.set(2)
    elif b == cb_base_op_base10:
        base.set(10)
    elif b == cb_base_op_base16:
        base.set(16)

    print(f'base.get() = {base.get()}')


def set_operation(event):
    clear_all_entries()

    print(f'cb_operation.get() = {cb_operation.get()}')

    if not any(op in cb_operation.get() for op in [
        'root', 'Module', 'Primality', 'Factorization', 'Discrete Logarithm'
    ]):
        op2_label.grid(row=1, column=0, padx=padx, pady=pady, sticky='e')
        op2_entry.grid(row=1, column=1, padx=padx, pady=pady, sticky='we')
    else:
        op2_label.grid_remove()
        op2_entry.grid_remove()

    if any(op in cb_operation.get() for op in [
        'GCD 3', 'LCM 3'
    ]):
        op3_label.grid(row=2, column=0, padx=padx, pady=pady, sticky='e')
        op3_entry.grid(row=2, column=1, padx=padx, pady=pady, sticky='we')
    else:
        op3_label.grid_remove()
        op3_entry.grid_remove()

    if 'Discrete Logarithm' in cb_operation.get():
        b_label.grid(row=3, column=0, padx=padx, pady=pady, sticky='e')
        b_entry.grid(row=3, column=1, padx=padx, pady=pady, sticky='we')
        y_label.grid(row=4, column=0, padx=padx, pady=pady, sticky='e')
        y_entry.grid(row=4, column=1, padx=padx, pady=pady, sticky='we')
        op1_label.grid_remove()
        op1_entry.grid_remove()
    else:
        y_label.grid_remove()
        y_entry.grid_remove()

    if any(op in cb_operation.get() for op in [
        'Module', 'module', 'Discrete Logarithm'
    ]):
        module_label.grid(row=5, column=0, padx=padx, pady=pady, sticky='e')
        module_entry.grid(row=5, column=1, padx=padx, pady=pady, sticky='we')
    else:
        module_label.grid_remove()
        module_entry.grid_remove()


def calculate(arg_base, arg_op):
    items_with_error = []

    if arg_base == 0:
        items_with_error.append('Base')

    if arg_op == 0:
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
        operation.addition(res, base, op1, op2, module)
    elif op == cb_operation_op_substraction:
        operation.substraction(res, base, op1, op2)
    elif op == cb_operation_op_substraction_module:
        operation.substraction(res, base, op1, op2, module)
    elif op == cb_operation_op_multiplication:
        operation.multiplication(res, base, op1, op2)
    elif op == cb_operation_op_multiplication_module:
        operation.multiplication(res, base, op1, op2, module)
    elif op == cb_operation_op_division:
        operation.division(res, base, op1, op2)
    elif op == cb_operation_op_square_root:
        operation.square_root(res, base, op1)
    elif op == cb_operation_op_primitive_root:
        operation.primitive_root(res, base, op1)
    elif op == cb_operation_op_xor:
        operation.xor(res, base, op1, op2)
    elif op == cb_operation_op_mod_inverse:
        operation.mod_inverse(res, base, op1, module)
    elif op == cb_operation_op_exponentation:
        operation.exponentation(res, base, op1, op2)
    elif op == cb_operation_op_exponentation_module:
        operation.exponentation(res, base, op1, op2, module)
    elif op == cb_operation_op_module:
        operation.module(res, base, op1, module)
    elif op == cb_operation_op_gcd_2:
        operation.gcd(res, base, op1, op2)
    elif op == cb_operation_op_gcd_3:
        operation.gcd(res, base, op1, op2, op3)
    elif op == cb_operation_op_lcm_2:
        operation.lcm(res, base, op1, op2)
    elif op == cb_operation_op_lcm_3:
        operation.lcm(res, base, op1, op2, op3)
    elif op == cb_operation_op_primality:
        operation.primality(res, base, op1)
    elif op == cb_operation_op_factorization:
        operation.factorization(res, base, op1)
    elif op == cb_operation_op_discreteLogarithm:
        operation.discreteLogarithm(res, base, b, y, module)


def about():
    MessageBox.showinfo(f'About {program_name}', f'{program_description}')


root = Tk()
# root.geometry('650x250')
root.title(f'{program_name} - {program_description}')
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

menubar = Menu(root, bg=bg_color, fg=fg_color, borderwidth=1)
root.config(menu=menubar)

options_menu = Menu(menubar, tearoff=0)
options_menu.add_command(label='Configuration')
options_menu.add_separator()
options_menu.add_command(label='Exit', command=root.quit)

help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label='View terms of use')
help_menu.add_command(label='View license')
help_menu.add_command(label='Documentation')
help_menu.add_separator()
help_menu.add_command(label=f'About {program_name}', command=about)

menubar.add_cascade(label='Options', menu=options_menu)
menubar.add_cascade(label='Help', menu=help_menu)

frame1 = Frame(root, cursor='arrow', bg=bg_color, bd=5)
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
cb_operation_op_substraction_module = 'Substraction module'
cb_operation_op_multiplication = 'Multiplication'
cb_operation_op_multiplication_module = 'Multiplication module'
cb_operation_op_division = 'Division'
cb_operation_op_square_root = 'Square root'
cb_operation_op_primitive_root = 'Primitive root'
cb_operation_op_xor = 'XOR'
cb_operation_op_mod_inverse = 'Module inverse'
cb_operation_op_exponentation = 'Exponentation'
cb_operation_op_exponentation_module = 'Exponentation module'
cb_operation_op_module = 'Module'
cb_operation_op_gcd_2 = 'GCD 2 numbers'
cb_operation_op_gcd_3 = 'GCD 3 numbers'
cb_operation_op_lcm_2 = 'LCM 2 numbers'
cb_operation_op_lcm_3 = 'LCM 3 numbers'
cb_operation_op_primality = 'Primality'
cb_operation_op_factorization = 'Factorization'
cb_operation_op_discreteLogarithm = 'Discrete Logarithm'

cb_operation = Combobox(frame1, state='readonly')
cb_operation['values'] = [
    cb_operation_op_default,
    cb_operation_op_addition,
    cb_operation_op_addition_module,
    cb_operation_op_substraction,
    cb_operation_op_substraction_module,
    cb_operation_op_multiplication,
    cb_operation_op_multiplication_module,
    cb_operation_op_division,
    cb_operation_op_square_root,
    cb_operation_op_primitive_root,
    cb_operation_op_xor,
    cb_operation_op_mod_inverse,
    cb_operation_op_exponentation,
    cb_operation_op_exponentation_module,
    cb_operation_op_module,
    cb_operation_op_gcd_2,
    cb_operation_op_gcd_3,
    cb_operation_op_lcm_2,
    cb_operation_op_lcm_3,
    cb_operation_op_primality,
    cb_operation_op_factorization,
    cb_operation_op_discreteLogarithm
]
cb_operation.current(0)
cb_operation.bind('<<ComboboxSelected>>', set_operation)
cb_operation.grid(row=0, column=1, padx=padx, pady=pady, sticky='w')


frame2 = Frame(root, cursor='arrow', bg=bg_color, bd=5)
frame2.pack(expand=True, fill='x')
frame2.grid_columnconfigure(1, weight=1)

op1 = StringVar()
op2 = StringVar()
op3 = StringVar()
b = StringVar()
y = StringVar()
module = StringVar()
res = StringVar()

op1_label = Label(frame2, text='First number', bg=bg_color, fg=fg_color)
op1_label.grid(row=0, column=0, padx=padx, pady=pady, sticky='e')
op1_entry = Entry(frame2, font=font, textvariable=op1)
op1_entry.grid(row=0, column=1, padx=padx, pady=pady, sticky='we')

op2_label = Label(frame2, text='Second number', bg=bg_color, fg=fg_color)
op2_entry = Entry(frame2, font=font, textvariable=op2)

op3_label = Label(frame2, text='Third number', bg=bg_color, fg=fg_color)
op3_entry = Entry(frame2, font=font, textvariable=op3)

b_label = Label(frame2, text='Base', bg=bg_color, fg=fg_color)
b_entry = Entry(frame2, font=font, textvariable=b)

y_label = Label(frame2, text='Y', bg=bg_color, fg=fg_color)
y_entry = Entry(frame2, font=font, textvariable=y)

module_label = Label(frame2, text='Module', bg=bg_color, fg=fg_color)
module_entry = Entry(frame2, font=font, textvariable=module)

label_res = Label(frame2, text='Result', bg=bg_color, fg=fg_color)
label_res.grid(row=6, column=0, padx=padx, pady=pady, sticky='e')
entry_res = Entry(frame2, font=font, textvariable=res,
                  state='readonly', readonlybackground='white')
entry_res.grid(row=6, column=1, padx=padx, pady=pady, sticky='we')

button = Button(frame2,
                text='Calulate',
                command=lambda: calculate(
                    cb_base.current(),
                    cb_operation.current())
                )
button.grid(row=7, column=1, padx=padx, pady=pady, sticky='w')

root.mainloop()
