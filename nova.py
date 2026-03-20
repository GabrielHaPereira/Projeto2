import tkinter as tk
from tkinter import ttk
from tkinter import *

janela = tk.Tk()
janela.title("Formulario")

# entrada de dados
label_entrada = ttk.Label(janela, text="Nome")
label_entrada.pack()

entrada = tk.Entry(janela)
entrada.pack()

# CHECKBOX
checkbox_var = tk.IntVar()
check = tk.Checkbutton(janela, text="Aceito os termos", variable=checkbox_var)
check.pack()

# opções (
opcao = tk.IntVar()

opc1 = tk.Radiobutton(janela, text="Masculino", variable=opcao, value=1)
opc2 = tk.Radiobutton(janela, text="Feminino", variable=opcao, value=2)
opc3 = tk.Radiobutton(janela, text="Outro", variable=opcao, value=3)

opc1.pack()
opc2.pack()
opc3.pack()

lista = tk.Listbox(janela)
lista.insert(1,"Python")
lista.insert(2,"java")
lista.insert(3,"PHP")
lista.insert(4,"Javascript")
lista.pack()

janela.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import *

janela = tk.Tk()
janela.title("Formulario")

# entrada de dados
label_entrada = ttk.Label(janela, text="Nome")
label_entrada.pack()

entrada = tk.Entry(janela)
entrada.pack()

# CHECKBOX
checkbox_var = tk.IntVar()
check = tk.Checkbutton(janela, text="Aceito os termos", variable=checkbox_var)
check.pack()

# opções (
opcao = tk.IntVar()

opc1 = tk.Radiobutton(janela, text="Masculino", variable=opcao, value=1)
opc2 = tk.Radiobutton(janela, text="Feminino", variable=opcao, value=2)
opc3 = tk.Radiobutton(janela, text="Outro", variable=opcao, value=3)

opc1.pack()
opc2.pack()
opc3.pack()

lista = tk.Listbox(janela)
lista.insert(1,"Python")
lista.insert(2,"java")
lista.insert(3,"PHP")
lista.insert(4,"Javascript")
lista.pack()

janela.mainloop()