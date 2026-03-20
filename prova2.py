import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

janela = tk.Tk()
janela.title("Cadastro")


def mostrar_dados():
    n = nome.get()
    s = sobrenome.get()
    nasc = data.get()
    c = cpf.get()
    ce = cep.get()
    sx = sexo.get()
    est = estado.get()
    cid = cidade.get()

    texto = "Dados informados:\n\n"
    texto += "Nome: " + n + " " + s + "\n"
    texto += "Nascimento: " + nasc + "\n"
    texto += "CPF: " + c + "\n"
    texto += "CEP: " + ce + "\n"
    texto += "Sexo: " + sx + "\n"
    texto += "Estado: " + est + "\n"
    texto += "Cidade: " + cid

    messagebox.showinfo("Cadastro", texto)

tk.Label(janela, text="Cadastro", font=("Arial", 18)).pack(pady=10)

# Nome
tk.Label(janela, text="Nome").pack()
nome = tk.Entry(janela)
nome.pack()

# Sobrenome
tk.Label(janela, text="Sobrenome").pack()
sobrenome = tk.Entry(janela)
sobrenome.pack()

# Data
tk.Label(janela, text="Data de nascimento").pack()
data = tk.Entry(janela)
data.pack()

# CPF
tk.Label(janela, text="CPF").pack()
cpf = tk.Entry(janela)
cpf.pack()

# CEP
tk.Label(janela, text="CEP").pack()
cep = tk.Entry(janela)
cep.pack()

# Sexo
tk.Label(janela, text="Sexo").pack()
sexo = ttk.Combobox(janela, values=["Masculino", "Feminino",])
sexo.pack()

# Estado
tk.Label(janela, text="Estado").pack()
estado = tk.Entry(janela)
estado.pack()

# Cidade
tk.Label(janela, text="Cidade").pack()
cidade = tk.Entry(janela)
cidade.pack()


#entrada de imagem
imagem = tk.PhotoImage(file="bolso.png")
imagem = imagem.subsample(3,3)
tk.Label(janela, image=imagem).pack()



# Botão
tk.Button(janela, text="Cadastrar", command=mostrar_dados).pack(pady=15)

janela.mainloop()