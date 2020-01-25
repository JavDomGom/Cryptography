import resources.operations as operation
# from os import getcwd
from tkinter import Tk, Menu, Scrollbar, END, IntVar, StringVar
from tkinter import Frame, Grid, Label, Entry, Text, Checkbutton, Button
from tkinter import messagebox as MessageBox

program_name = 'MASCrypt'
program_description = 'Modular Arithmetic Software for Cryptography'
frame_height = 150
label_width = 14
label_anchor = 'e'
label_sticky = 'e'
entry_sticky = 'we'
padx = 3
pady = 3
font = ('Courier New', 10)
bg_color = '#C9C9C9'
fg_color = '#000000'

# All available operations.
op_addition = ('Addition', '+')
op_substraction = ('Substraction', '-')
op_multiplication = ('Multiplication', 'x')
op_division = ('Division', '/')
op_square_root = ('Square root', '√')
op_primitive_root = ('Primitive root', '∝')
op_xor = ('XOR', 'XOR')
op_mod_inverse = ('Module inverse', 'Inv')
op_exponentation = ('Exponentation', 'a^b')
op_module = ('Module', 'mod')
op_gcd = ('GCD', 'GDC')
op_lcm = ('LCM', 'LCM')
op_primality = ('Primality', 'Prime')
op_factorization = ('Factorization', 'Fact')
op_discreteLogarithm = ('Discrete Logarithm', 'DLP')


def clear_all_entries():
    ''' Empty all entries.'''
    ops = [op1, op2, op3, mod, res]
    for op in ops:
        op.set('')
    op3_active.set(0)
    set_op3()
    mod_active.set(0)
    set_module()


def clear_all_widgets():
    ''' Clear all widgets in grid.'''
    clear_all_entries()
    widgets = [
        op1_label, op1_entry,
        op2_label, op2_entry,
        op3_label, op3_entry, op3_check,
        module_label, module_entry, module_check,
        res_label, res_entry
    ]
    for widget in widgets:
        widget.grid_remove()


def set_base(selected_base):
    clear_all_entries()

    if 'Binary' in selected_base:
        base.set(2)
    elif 'Decimal' in selected_base:
        base.set(10)
    elif 'Hexadecimal' in selected_base:
        base.set(16)

    print(f'base.get() = {base.get()}')


def set_module():
    if mod_active.get():
        module_entry.config(state='normal')
    else:
        module_entry.config(state='disabled')


def set_op3():
    if op3_active.get():
        op3_entry.config(state='normal')
    else:
        op3_entry.config(state='disabled')


def set_operation(selected_op):
    clear_all_widgets()

    # All operations include op1, res and bt_calculate widgets.
    op1_label.grid(
        row=0,
        column=0,
        padx=padx,
        pady=pady,
        sticky=label_sticky
    )
    op1_entry.grid(
        row=0,
        column=1,
        padx=padx,
        pady=pady,
        sticky=entry_sticky
    )

    res_label.grid(
        row=4,
        column=0,
        padx=padx,
        pady=pady,
        sticky=label_sticky
    )
    res_entry.grid(
        row=4,
        column=1,
        padx=padx,
        pady=pady,
        sticky=entry_sticky
    )

    # Operations that use op2 widgets.
    if selected_op in [
        op_addition[0],
        op_substraction[0],
        op_multiplication[0],
        op_division[0],
        op_xor[0],
        op_exponentation[0],
        op_gcd[0],
        op_lcm[0],
        op_discreteLogarithm[0]
    ]:
        op2_label.grid(
            row=1,
            column=0,
            padx=padx,
            pady=pady,
            sticky=label_sticky
        )
        op2_entry.grid(
            row=1,
            column=1,
            padx=padx,
            pady=pady,
            sticky=entry_sticky
        )

    # Operations that use op3 widgets.
    if selected_op in [
        op_gcd[0],
        op_lcm[0]
    ]:
        op3_check.grid(
            row=2,
            column=0,
            padx=padx-1,
            sticky=label_sticky
        )
        op3_entry.grid(
            row=2,
            column=1,
            padx=padx,
            pady=pady,
            sticky=entry_sticky
        )

    # Base and Y widgets only for Discrete Logarithm operation.
    if selected_op == op_discreteLogarithm[0]:
        op1_label['text'] = 'Base'
        op2_label['text'] = 'Y'
    else:
        op1_label['text'] = 'First operator'
        op2_label['text'] = 'Second operator'

    # Operations that use module widgets.
    if selected_op in [
        op_addition[0],
        op_substraction[0],
        op_multiplication[0],
        op_exponentation[0],
        op_mod_inverse[0],
        op_module[0],
        op_discreteLogarithm[0]
    ]:
        if selected_op in [
            op_addition[0],
            op_substraction[0],
            op_multiplication[0],
            op_exponentation[0]
        ]:
            module_check.grid(
                row=3,
                column=0,
                padx=padx-1,
                sticky=label_sticky
            )
        elif selected_op in [
            op_mod_inverse[0],
            op_module[0],
            op_discreteLogarithm[0]
        ]:
            module_label.grid(
                row=3,
                column=0,
                padx=padx,
                pady=pady,
                sticky=label_sticky
            )
            module_entry.config(state='normal')

        module_entry.grid(
            row=3,
            column=1,
            padx=padx,
            pady=pady,
            sticky=entry_sticky
        )

    oper.set(selected_op)

    print(f'oper.get() = {oper.get()}')


def calculate():
    items_with_error = []
    op = oper.get()

    if base.get() == 0:
        items_with_error.append('Base')

    if op == 0:
        items_with_error.append('Operation')

    if len(items_with_error) != 0:
        MessageBox.showerror(
            title=f'Missing information:',
            message=f'You must select the following items:\
            \n\n{", ".join(items_with_error)}'
        )
        return

    if op == op_addition[0]:
        if mod_active.get():
            operation.addition(res, base, op1, op2, mod)
            history.insert(
                END, f'{op1.get()} + {op2.get()} mod {mod.get()} = {res.get()}\n'
            )
        else:
            operation.addition(res, base, op1, op2)
            history.insert(
                END, f'{op1.get()} + {op2.get()} = {res.get()}\n'
            )
    elif op == op_substraction[0]:
        if mod_active.get():
            operation.substraction(res, base, op1, op2, mod)
            history.insert(
                END, f'{op1.get()} - {op2.get()} mod {mod.get()} = {res.get()}\n'
            )
        else:
            operation.substraction(res, base, op1, op2)
            history.insert(
                END, f'{op1.get()} - {op2.get()} = {res.get()}\n'
            )
    elif op == op_multiplication[0]:
        if mod_active.get():
            operation.multiplication(res, base, op1, op2, mod)
            history.insert(
                END, f'{op1.get()} x {op2.get()} mod {mod.get()} = {res.get()}\n'
            )
        else:
            operation.multiplication(res, base, op1, op2)
            history.insert(
                END, f'{op1.get()} x {op2.get()} = {res.get()}\n'
            )
    elif op == op_division[0]:
        operation.division(res, base, op1, op2)
        history.insert(
            END, f'{op1.get()}/{op2.get()} = {res.get()}\n'
        )
    elif op == op_square_root[0]:
        operation.square_root(res, base, op1)
        history.insert(
            END, f'√{op1.get()} = {res.get()}\n'
        )
    elif op == op_primitive_root[0]:
        operation.primitive_root(res, base, op1)
        history.insert(
            END, f'|∝|={len(eval(res.get()))}, {op1.get()} = {res.get()}\n'
        )
    elif op == op_xor[0]:
        operation.xor(res, base, op1, op2)
        history.insert(
            END, f'{op1.get()} XOR {op2.get()} = {res.get()}\n'
        )
    elif op == op_mod_inverse[0]:
        operation.mod_inverse(res, base, op1, mod)
        history.insert(
            END, f'inv({op1.get()}, {mod.get()}) = {res.get()}\n'
        )
    elif op == op_exponentation[0]:
        if mod_active.get():
            operation.exponentation(res, base, op1, op2, mod)
            history.insert(
                END, f'{op1.get()}^{op2.get()} mod {mod.get()} = {res.get()}\n'
            )
        else:
            operation.exponentation(res, base, op1, op2)
            history.insert(
                END, f'{op1.get()}^{op2.get()} = {res.get()}\n'
            )
    elif op == op_module[0]:
        operation.module(res, base, op1, mod)
        history.insert(
            END, f'{op1.get()} mod {mod.get()} = {res.get()}\n'
        )
    elif op == op_gcd[0]:
        if op3_active.get():
            operation.gcd(res, base, op1, op2, op3)
            history.insert(
                END, f'gdc({op1.get()}, {op2.get()}, {op3.get()}) = {res.get()}\n'
            )
        else:
            operation.gcd(res, base, op1, op2)
            history.insert(
                END, f'gdc({op1.get()}, {op2.get()}) = {res.get()}\n'
            )
    elif op == op_lcm[0]:
        if op3_active.get():
            operation.lcm(res, base, op1, op2, op3)
            history.insert(
                END, f'lcm({op1.get()}, {op2.get()}, {op3.get()}) = {res.get()}\n'
            )
        else:
            operation.lcm(res, base, op1, op2)
            history.insert(
                END, f'lcm({op1.get()}, {op2.get()}) = {res.get()}\n'
            )
    elif op == op_primality[0]:
        operation.primality(res, base, op1)
        history.insert(
            END, f'{op1.get()} {res.get().lower()}\n'
        )
    elif op == op_factorization[0]:
        operation.factorization(res, base, op1)
        history.insert(
            END, f'{op1.get()} = {res.get()}\n'
        )
    elif op == op_discreteLogarithm[0]:
        operation.discreteLogarithm(res, base, op1, op2, mod)
        history.insert(
            END, f'{op1.get()}^{res.get()} = {op2.get()} mod {mod.get()}\n'
        )

    history.see(END)


def about():
    MessageBox.showinfo(f'About {program_name}', f'{program_description}')


root = Tk()
# root.geometry('650x250')
root.title(f'{program_name} - {program_description}')
root.resizable(1, 0)
# root.iconbitmap(f'@{getcwd()}/img/icon.xbm')

menubar = Menu(root, bg=bg_color, fg=fg_color, borderwidth=1)
root.config(menu=menubar)

options_menu = Menu(menubar, tearoff=0)
options_menu.add_command(label='Configuration')
options_menu.add_separator()
options_menu.add_command(label='Exit', command=root.quit)

base_list = [
    'Base-2 (Binary)',
    'Base-10 (Decimal)',
    'Base-16 (Hexadecimal)'
]

base_menu = Menu(menubar, tearoff=0)

for b in base_list:
    base_menu.add_command(
        label=f'{b}', command=lambda b=b: set_base(b)
    )

operation_list = [
    op_addition,
    op_substraction,
    op_multiplication,
    op_division,
    op_square_root,
    op_primitive_root,
    op_xor,
    op_mod_inverse,
    op_exponentation,
    op_module,
    op_gcd,
    op_lcm,
    op_primality,
    op_factorization,
    op_discreteLogarithm
]

operations_menu = Menu(menubar, tearoff=0)

for op in operation_list:
    operations_menu.add_command(
        label=f'{op[0]}', command=lambda op=op[0]: set_operation(op)
    )

help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label='View terms of use')
help_menu.add_command(label='View license')
help_menu.add_command(label='Documentation')
help_menu.add_separator()
help_menu.add_command(label=f'About {program_name}', command=about)

menubar.add_cascade(label='Options', menu=options_menu)
menubar.add_cascade(label='Base', menu=base_menu)
menubar.add_cascade(label='Operations', menu=operations_menu)
menubar.add_cascade(label='Help', menu=help_menu)

base = IntVar()
history = StringVar()
oper = StringVar()
op1 = StringVar()
op2 = StringVar()
op3_active = IntVar()
op3 = StringVar()
mod_active = IntVar()
mod = StringVar()
res = StringVar()

frame_L = Frame(
    root,
    bg='#00ff00',
    bd=5,
    height=frame_height
)
frame_L.pack(side='left', expand=True, fill='both')
frame_L.grid_propagate(False)
frame_L.grid_columnconfigure(1, weight=1)

frame_R = Frame(
    root,
    bg='#0000ff',
    bd=5,
    width=50,
    height=frame_height
)
frame_R.pack(side='right', expand=True, fill='both')
frame_R.grid_propagate(False)
frame_R.grid_columnconfigure(0, weight=1)
frame_R.grid_rowconfigure(0, weight=1)

history = Text(
    frame_R,
    font=font,
    state='normal',
    yscrollcommand='sdvaerg'
)
scrollb = Scrollbar(frame_R)
scrollb.config(command=history.yview)
history.config(yscrollcommand=scrollb.set)
scrollb.grid(row=0, column=1, sticky='ns')
history.grid(row=0, column=0, sticky='nsew')

frame_L1 = Frame(
    frame_L,
    bg='#ffff00',
    bd=5,
    width=350,
    height=frame_height
)
frame_L1.pack(expand=True, fill='both')
frame_L1.grid_propagate(False)
frame_L1.grid_columnconfigure(1, weight=1)

op1_label = Label(
    frame_L1,
    anchor=label_anchor,
    text='First operator',
    width=label_width,
    bg=bg_color,
    fg=fg_color
)
op1_entry = Entry(
    frame_L1,
    font=font,
    textvariable=op1
)

op2_label = Label(
    frame_L1,
    anchor=label_anchor,
    text='Second operator',
    width=label_width,
    bg=bg_color,
    fg=fg_color
)
op2_entry = Entry(
    frame_L1,
    font=font,
    textvariable=op2
)

op3_check = Checkbutton(
    frame_L1,
    anchor=label_anchor,
    text='Third operator',
    width=label_width-3,
    bg=bg_color,
    fg=fg_color,
    variable=op3_active,
    command=set_op3
)
op3_label = Label(
    frame_L1,
    anchor=label_anchor,
    text='Third operator',
    width=label_width,
    bg=bg_color,
    fg=fg_color
)
op3_entry = Entry(
    frame_L1,
    font=font,
    textvariable=op3
)

module_check = Checkbutton(
    frame_L1,
    anchor=label_anchor,
    text='Module',
    width=label_width-3,
    bg=bg_color,
    fg=fg_color,
    variable=mod_active,
    command=set_module
)
module_label = Label(
    frame_L1,
    anchor=label_anchor,
    text='Module',
    width=label_width,
    bg=bg_color,
    fg=fg_color
)
module_entry = Entry(
    frame_L1,
    state='disabled',
    font=font,
    textvariable=mod
)

res_label = Label(
    frame_L1,
    anchor=label_anchor,
    text='Result',
    width=label_width,
    bg=bg_color,
    fg=fg_color
)
res_entry = Entry(
    frame_L1,
    font=font,
    textvariable=res,
    state='readonly',
    readonlybackground='white'
)

frame_L2 = Frame(
    frame_L,
    bg='#00ffff',
    bd=5
)
frame_L2.pack(expand=True, fill='both')
frame_L2.grid_columnconfigure(1, weight=1)

bt_calculate = Button(
    frame_L2,
    text='Calulate',
    command=lambda: calculate()
)
bt_calculate.grid(row=0, column=0, padx=padx, pady=pady, sticky='w')

bt_clear_history = Button(
    frame_L2,
    text='Clear history',
    command=lambda: history.delete('1.0', END)
)
bt_clear_history.grid(row=0, column=1, padx=padx, pady=pady, sticky='w')

frame_L3 = Frame(
    frame_L,
    bg=bg_color,
    bd=5
)
frame_L3.pack(expand=True, fill='both')
frame_L3.grid_columnconfigure(1, weight=1)

# Grid for buttons
rows = 3
cols = 5
for i in range(rows):
    for x, o in enumerate(operation_list[cols*i:cols*(i+1)]):
        Grid.columnconfigure(frame_L3, x, weight=1)
        op_btn = Button(
            frame_L3,
            text=o[1],
            command=lambda o=o[0]: set_operation(o)
        )
        op_btn.grid(row=i, column=x, padx=padx, pady=pady, sticky='nsew')

root.mainloop()
