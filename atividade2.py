import tkinter as tk
from tkinter import ttk 

def enviar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    escolaridade = combo_escolaridade.get()
    area = area_var.get()

    mensagem = f"""DADOS PESSOAIS:
Nome: {nome}
Idade: {idade}

DADOS PROFISSIONAIS:
Escolaridade: {escolaridade}
Área de atuação: {area}
"""

    
#janela
janela = tk.Tk()
janela.title("Formulário de Cadastro")
janela.geometry("400x350")

#DADOS PESSOAIS
label_pessoal = tk.Label(janela, text="DADOS PESSOAIS", font=("Arial", 12, "bold"))
label_pessoal.pack(pady=5)

#Nome
tk.Label(janela, text="Nome:").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

#Idade
tk.Label(janela, text="Idade:").pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()

#DADOS PROFISSIONAIS
label_profissional = tk.Label(janela, text="DADOS PROFISSIONAIS", font=("Arial", 12, "bold"))
label_profissional.pack(pady=10)

#Escolaridade
tk.Label(janela, text="Escolaridade:").pack()
combo_escolaridade = tk.StringVar()
opcoes = ["Ensino Fundamental", "Ensino Médio", "Ensino Superior", "Pós-graduação"]
combo = tk.OptionMenu(janela, combo_escolaridade, *opcoes)
combo.pack()

#Área de atuação
tk.Label(janela, text="Área de atuação:").pack()
area_var = tk.StringVar()
area_var.set("Tecnologia")

tk.Radiobutton(janela, text="Tecnologia", variable=area_var, value="Tecnologia").pack()
tk.Radiobutton(janela, text="Saúde", variable=area_var, value="Saúde").pack()
tk.Radiobutton(janela, text="Educação", variable=area_var, value="Educação").pack()

#Botão enviar
botao = tk.Button(janela, text="Enviar", command=enviar_dados)
botao.pack(pady=15)

#Executando
janela.mainloop()