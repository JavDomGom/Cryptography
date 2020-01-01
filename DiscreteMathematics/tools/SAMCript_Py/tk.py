from os import getcwd
from tkinter import *

root = Tk()

root.title('SAMCript_py - Software de Aritmética Modular para Criptografía')
root.resizable(1,1)
# root.iconbitmap(f'@{getcwd()}/img/book.xbm')

frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand=1)
frame.config(cursor='arrow')
frame.config(bg='lightblue')
frame.config(bd=25)
frame.config(relief='sunken')
# frame.pack(side=RIGHT)   # a la derecha al medio
# frame.pack(anchor=SE)    # sudeste, abajo a la derecha

root.config(cursor='arrow')
root.config(bg='blue')
root.config(bd=15)
root.config(relief='ridge')

root.mainloop()
