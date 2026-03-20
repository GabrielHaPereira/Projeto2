import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Login")
janela.geometry("300x200")


def enviar():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    msg = f"Usuário: {usuario}\nSenha: {senha}"
    messagebox.showinfo("Login realizado!", msg)

tk.Label(janela, text="Tela de Login", font=("Arial",20)).grid(column=1, pady = 20)

#entrada de texto Usuário 
tk.Label(janela, text="Usuário:", font=("Arial")).grid(row=1, column=0)
entrada_usuario = tk.Entry(janela, font=("Arial"))
entrada_usuario.grid(row=1, column=1)

#entrada de texto Senha
tk.Label(janela, text="Senha:", font=("Arial")).grid(row=2, column=0)
entrada_senha = tk.Entry(janela, font=("Arial"), show="*")
entrada_senha.grid(row=2, column=1)

#entrada de imagem
imagem = tk.PhotoImage(file="downloads.png")
#imagem = imagem.subsample(3,3)
tk.Label(janela, image=imagem).grid(row=3, column=4)




# Botão
tk.Button(janela, text="Entrar", command=enviar).grid(row=3, column=1, pady=20)

janela.mainloop()